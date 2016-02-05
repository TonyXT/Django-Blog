from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
            max_length=20,
            initial='',
            label=u'Username',
            widget=forms.TextInput(attrs={'class': 'full-width has-padding has-border ',
                                          'id': 'signup-username',
                                          'placeholder': 'Please input your username'}),
    )

    email = forms.EmailField(
            max_length=50,
            label=u'E-mail',
            initial='',
            widget=forms.TextInput(attrs={'class': 'full-width has-padding has-border',
                                          'id': 'signup-email',
                                          'placeholder': 'Please input your E-mail address'

                                          })
    )

    password = forms.CharField(
            max_length=20,
            label=u'Password',
            initial='',
            widget=forms.PasswordInput(attrs={'class': 'full-width has-padding has-border',
                                              'id': 'signup-password',
                                              'placeholder': 'Please input your password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username or '@' in username:
            raise forms.ValidationError(u'Username cannot include @ or blank')
        res = User.objects.filter(username=username)
        if len(res) != 0:
            raise forms.ValidationError(u'This username has been registered already,please pick a new one')
        return username

    def save(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        email=self.cleaned_data['email']
        user=User.objects.create_user(username,email,password)
        user.save()


    def clean_email(self):
        email = self.cleaned_data['email']
        res = User.objects.filter(email=email)
        if len(res) != 0:
            raise forms.ValidationError(u'This E-mail address has been registered already, please pick a new one')
        return email