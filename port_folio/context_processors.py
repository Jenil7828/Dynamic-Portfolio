from .models import SocialLinks, SiteSettings, ContactInfo

def global_settings(request):
    return {
        'social': SocialLinks.objects.first(),
        'settings': SiteSettings.objects.first()
    }

def contact_info(request):
    contact = ContactInfo.objects.first()  # Assuming only one entry
    return {'contact_info': contact}


def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
    except:
        settings = None
    return {'settings': settings}