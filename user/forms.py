from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='Kullanıcı Adı Giriniz :',required=True)
    password = forms.CharField(max_length=50,label='Şifrenizi Giriniz :',required=True,widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username   = forms.CharField(max_length=100,label='Kullanıcı Adı :')
    email      = forms.EmailField(max_length=300,label='Email Giriniz :  ')
    password   = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(),label='Parolanızı Giriniz :')
    repassword = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(),label='Parolanızı Onaylayınız :')
    def clean(self):
        username    = self.cleaned_data.get('username')
        email       = self.cleaned_data.get('email')
        password    = self.cleaned_data.get('password')
        repassword  = self.cleaned_data.get('repassword')

        if password and repassword and password !=repassword:
            return forms.ValidationError('Parolalar eşleşmiyor.')
        values = {
            'username': username,
            'email': email,
            'password':password
        }
        return values

    