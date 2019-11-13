from django.conf import settings
from django.core.mail import send_mail

from .models import EmailRequest


def send_email(email_request):
    subject = "Online form"
    message = "Thank you! We've got your message"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_request]
    send_mail(subject, message, email_from, recipient_list)


def save_email(email_request):
    email = EmailRequest.objects.create(name=email_request)
