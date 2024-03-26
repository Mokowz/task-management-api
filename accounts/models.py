from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your models here.
class CustomUser(AbstractUser):
    pass


# @receiver(post_save, sender=CustomUser)
# def send_reg_email(sender, instance, created, **kwargs):
#     try:
#         if created:
#             subject = "Welcome to Task Management API"
#             body = f'{instance.username} signed up'
#             message = render_to_string(
#                 'accounts/welcome_email.html',
#                 {'user': instance}
#             )
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [instance.email, ]
#             send_mail(subject=subject, message = body,from_email=from_email, recipient_list=recipient_list, html_message=message)
#     except SystemError as err:
#         print(err)