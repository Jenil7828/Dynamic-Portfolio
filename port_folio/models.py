from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)  # <- added this line
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name


# models.py
class ContactInfo(models.Model):
    address_title = models.CharField(max_length=255, default="Palghar, India")
    address_details = models.CharField(max_length=255, default="Rathod Bhavan Bldg., 1st Floor Next to Tembhode Road")

    latitude = models.FloatField(default=19.6976)  # Palghar Latitude
    longitude = models.FloatField(default=72.7656)  # Palghar Longitude

    phone = models.CharField(max_length=50, default="+91 8983672417")
    phone_note = models.CharField(max_length=100, default="Mon to Fri 9am to 6 pm")

    email = models.EmailField(default="jenilgrathod@gmail.com")
    email_note = models.CharField(max_length=100, default="Send us your query anytime!")

    def __str__(self):
        return "Contact Info"


class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="Introduce about myself")
    paragraph1 = models.TextField()
    paragraph2 = models.TextField(blank=True)
    cv_file = models.FileField(upload_to='resume/', blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}'s About Me"


class SocialLinks(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Social Links"

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', null=False, blank=False, default='default/logo.png')
    site_title = models.CharField(max_length=255, default="My Portfolio")
    footer_title = models.CharField(max_length=255, default="Follow Me")

    def __str__(self):
        return "Site Settings"

class ContactInfo(models.Model):
    address_title = models.CharField(max_length=255, default="Palghar, India")
    address_details = models.CharField(max_length=255, default="Rathod Bhavan Bldg., 1st Floor Next to Tembhode Road")

    phone = models.CharField(max_length=50, default="+91 8983672417")
    phone_note = models.CharField(max_length=100, default="Mon to Fri 9am to 6 pm")

    email = models.EmailField(default="jenilgrathod@gmail.com")
    email_note = models.CharField(max_length=100, default="Send us your query anytime!")

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return "Contact Info"

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name

class ExperienceInfo(models.Model):
    years_of_experience = models.PositiveIntegerField(default=0)
    call_text = models.CharField(max_length=100, default='call us now')
    phone_number = models.CharField(max_length=20, default='(+1)-800-555-6789')

    def __str__(self):
        return f"{self.years_of_experience} years experience"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skills/')  # Store in MEDIA_ROOT/skills/

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Machine Learning", "Web", etc.
    slug = models.SlugField(unique=True)  # e.g., "ml", "web", "upcoming"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    detail_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


from django.db import models


class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True)

    start_month = models.CharField(max_length=20)
    start_year = models.IntegerField()
    end_month = models.CharField(max_length=20)
    end_year = models.IntegerField()

    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    activities = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='education_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.school} - {self.degree}"
