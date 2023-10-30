from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def confirm_email(request, email, auth_token):
    subject = 'verify your account'
    html_content = render_to_string('email/confirm_account.html', {'auth_token': auth_token})
    msg = EmailMultiAlternatives(subject, 'Please verify your account', settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()