from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def send_gmail(sender, instance, created, **kwargs):
    send_mail(
        'Wellcome to goodreads clone',
        f'Hi {instance.username}, wellcome to goodreads clone, Enjoy read or review',
        'demo2001.uz@gmail.com',
        ['yewejay800@mevori.com']
    )
