from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile
import datetime

#from main import views

class RegisterForm(UserCreationForm):
    prof = (
        ('1','Matemático (a)'),
        ('2','Físico (a)')
    )
    email = forms.EmailField()
    cui = forms.IntegerField()
    profesion = forms.ChoiceField(choices=prof)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'cui', 'profesion']

    def save(self, commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            fecha = str(datetime.date.today().day) + '/' + str(datetime.date.today().month) + '/' + str(datetime.date.today().year)
            horario = str(datetime.datetime.now().time())
            send_mail('Hola, %s. Hay un nuevo inicio de sesión con tu cuenta.'%(user.username), 'Has iniciado sesión en la plataforma de Práctica III de Programación Matemática II.'
                                                                                                'Tu fecha y hora de inicio son %s a las %s.'%(fecha, horario),
                      'correosdeprogramacion@gmail.com',
                      [user.email], fail_silently=False)
            user.save()
        return user


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('Email has been used')

    def clean_nickname(self):
        nickname = self.cleaned_data['username']
        try:
            User.objects.get(username = nickname)
        except User.DoesNotExist:
            return nickname

        raise forms.ValidationError('El nickname ya ha sido usado')

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Usuario',max_length=150,help_text='')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    profesion =  forms.ChoiceField(choices=(('1', 'Matemática'), ('2','Física')))
    cui = forms.CharField(label='CUI', max_length=13,help_text='')
    class Meta:
        model = Profile
        fields = ['profesion', 'cui']
