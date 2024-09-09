from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, send_mail, mail_admins, mail_managers


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class CustomSignUpForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject = 'Добро пожаловать в наш новостной портал!'
        text = f'{user.username}, вы успешно зарегистрировались!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/news">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
#        authors_group = Group.objects.get(name="authors")
#        user.groups.add(authors_group)
        return user

