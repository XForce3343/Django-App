from django import forms

class RegisterForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electronico', 'id': 'Email', 'name': 'Email'}))
    username = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña', 'id': 'password', 'class': 'password'}))
    confirm_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu Cotraseña', 'id': 'confirm_password'}))
