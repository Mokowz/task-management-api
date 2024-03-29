# from allauth.account.signals import user_signed_up, user_logged_in
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from accounts.models import CustomUser
from django.db.models.signals import post_save

# @receiver(user_logged_in)
# def send_welcome_email(sender, request, user, **kwargs):
#     subject = "Welcome to Task Management API"
#     body = f'{user.username} logged in'
#     message = render_to_string(
#         'accounts/welcome_email.html',
#         {'user': user}
#     )
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [user.email, ]
#     send_mail(subject=subject, message = body,from_email=from_email, recipient_list=recipient_list, html_message=message)

@receiver(post_save, sender=CustomUser)
def send_reg_email(sender, instance, created, **kwargs):
    try:
        if created:
            subject = "Welcome to Task Management API"
            body = f'{instance.username} signed up'
            message = render_to_string(
                'accounts/welcome_email.html',
                {'user': instance}
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail(subject=subject, 
                      message = body,
                      from_email=from_email, 
                      recipient_list=recipient_list, 
                      html_message=message)
    except SystemError as err:
        print(err)