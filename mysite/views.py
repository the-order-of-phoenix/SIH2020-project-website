from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from . import forms
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm

    template_name = 'accounts/signup.html'
    def get_success_url(self):
        return reverse('mysite:sendmail', kwargs={'pk': self.object.pk})

def sendmail(request,pk):
    time = User.objects.get(pk=pk)
    subject = 'Visitor Came To Meet'
    #message="Hi"
    message = "Welcome to Registration"
    email_from = settings.EMAIL_HOST_USER
    print(time.email)
    recipient_list = [str(time.email),]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponseRedirect(reverse('mysite:login'))
