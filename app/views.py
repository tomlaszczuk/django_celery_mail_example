from django.core.mail import send_mail

from django.http import HttpResponse


def mail(request):
    send_mail('Subject', 'Message', 'example@gmail.com', ['recipient@gmail.com'])
    return HttpResponse("")
