from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about_view, name='about'),
	path('projects/', views.projects_view, name='projects'),
    path('experience/', views.experience_view, name='experience'),
    path('skills/', views.skills_view, name='skills'),
	path('contact/', views.contact_view, name='contact'),
	path('dashboard/', views.dashboard_view, name='dashboard'),
]