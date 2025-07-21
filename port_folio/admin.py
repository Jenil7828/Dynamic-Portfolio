from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at')
	search_fields = ('name', 'email', 'message')
	list_filter = ('created_at',)
	readonly_fields = ('name', 'email', 'message', 'created_at')

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'designation')

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
	list_display = ('title',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ('address_title', 'phone', 'email')


class SiteSettingsAdmin(admin.ModelAdmin):
	def logo_preview(self, obj):
		return format_html('<img src="{}" width="100" />', obj.logo.url if obj.logo else '')
	readonly_fields = ['logo_preview']
	list_display = ['site_title', 'logo_preview']


from django.contrib import admin
from .models import Skill, Brand, ExperienceInfo

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Brand)
admin.site.register(ExperienceInfo)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(SocialLinks)