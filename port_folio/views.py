from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import  *
from django.contrib.auth.decorators import login_required
from .forms import SkillForm
from django.shortcuts import render
from django.db.models import Count
# Create your views here.
def index(request):
	hero = HeroSection.objects.first()
	about = AboutSection.objects.first()
	social = SocialLinks.objects.first()
	brands = Brand.objects.all()
	skills = Skill.objects.all()
	projects = Project.objects.all()
	categories = ProjectCategory.objects.all()
	education_items = Education.objects.all()
	try:
		experience_info = ExperienceInfo.objects.latest('id')
	except ExperienceInfo.DoesNotExist:
		experience_info = None
	context = {
        'name': hero.name,
        'designation': hero.designation,
        'email': hero.email,
        'resume_url': hero.resume.url,
		'about': about,
		'social': social,
		'brands': brands,
		'experience_info': experience_info,
		'skills': skills,
		'projects': projects,
		'categories': categories,
		'education_items': education_items
	}
	return render(request, 'portfolio/index.html', context)


def contact_view(request):
	contact_info = ContactInfo.objects.first()
	context = {'contact_info': contact_info}
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		subject = request.POST.get('subject')
		Message.objects.create(name=name, email= email, subject=subject, message=message)

		send_mail(
			subject=f"New Contact Form Submission: {subject}",
			message=f"From: {name} <{email}>\n\nMessage:\n{message}",
			from_email='jenilrathod478@gmail.com',
			recipient_list=['jenilrathod478@gmail.com'],  # or any list of recipients
			fail_silently=False,
		)
		messages.success(request, "Your message was sent successfully")
		return redirect('contact')
	return render(request, 'portfolio/contact.html', context)

def experience_view(request):
	brands = Brand.objects.all()
	try:
		experience_info = ExperienceInfo.objects.latest('id')
	except ExperienceInfo.DoesNotExist:
		experience_info = None
	return render(request, 'portfolio/experience.html', {
        'brands': brands,
        'experience_info': experience_info
    })

def dashboard_view(request):
	return render(request, '<h1>Welcome to the Dashboard</h1>')

def about_view(request):
	about = AboutSection.objects.first()
	brands = Brand.objects.all()
	try:
		experience_info = ExperienceInfo.objects.latest('id')
	except ExperienceInfo.DoesNotExist:
		experience_info = None
	education_items = Education.objects.all()
	context = {
		'about': about,
		'brands': brands,
		'experience_info': experience_info,
		'education_items': education_items
	}
	return render(request, 'portfolio/about.html', context)



def projects_view(request):
	projects = Project.objects.all()
	categories = ProjectCategory.objects.all()
	context = {
		'projects': projects,
		'categories': categories
	}
	return render(request, 'portfolio/portfolio.html', context)


def skills_view(request):
	skills = Skill.objects.all()
	education_items = Education.objects.all()

	context = {
		'skills': skills,
		'education_items': education_items
	}
	return render(request, 'portfolio/services.html', context)






@login_required
def dashboard_view(request):
	total_projects = Project.objects.count()
	total_messages = Message.objects.count()
	total_skills = Skill.objects.count()
	total_education = Education.objects.count()

	# For graph data: Projects by category
	category_counts = (
		Project.objects.values('category__name')
		.annotate(count=Count('id'))
		.order_by('category__name')
	)

	messages = Message.objects.order_by('-created_at')  # latest 6 messages

	context = {
		'total_projects': total_projects,
		'total_messages': total_messages,
		'total_skills': total_skills,
		'total_education': total_education,
		'category_counts': category_counts,
		'messages': messages
	}

	return render(request, 'portfolio/dashboard.html', context)
