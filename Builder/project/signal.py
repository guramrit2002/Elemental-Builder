from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Page
from .handlers.html_handler import HTMLhandler

@receiver(post_save, sender=Page)
def save_html(sender, instance, created, **kwargs):
    try:
        if created:
            html_obj = HTMLhandler()
            Page.objects.filter(pk=instance.pk).update(
                html = html_obj.get_html(instance.content)
            )
            print("********* HTML is saved *********")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error saving HTML: {e}")
        raise Exception(f"Error saving HTML: {e}")