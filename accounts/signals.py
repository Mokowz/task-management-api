# from allauth.account.signals import user_signed_up, user_logged_in
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(user_logged_in)
def send_welcome_email(sender, request, user, **kwargs):
    subject = "Welcome to Task Management API"
    message = f"Dear {user.username}, karibu sana"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, from_email, recipient_list)