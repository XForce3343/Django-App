from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from .forms import RegisterForm

def welcome(request):
    context = {}
    return render(request, 'htm/welcome.html', context)

def register(request):
    # Creamos un formulario de autenticacion vacio
    form = RegisterForm()
    # Si queremos borrar los campos de consulta
    #form.fields['username'].help_text = None
    #form.fields['password1'].help_text = None
    #form.fields['password2'].help_text = None
    if request.method == "POST":
        # Añadimos los datos recibidis del formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es valido...
        if form.is_valid():
            #Creamos la cuenta del usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos login automaticamente
                do_login(request, user)
                # Y direccionamos a la portada
                return redirect('/')
    # Si llegamos al final renderizamos el formulario
    return render(request, 'htm/register.html', {'form': form})
def login(request):
    # Creamos el formulario de autenticacion vacio
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        #Si el formulario es valido...
        if form.is_valid():
            # Recuperamos las credenciales validas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Verificamos las credenciales del usuario
            if user is not None:
                # Hacemos login manualmente
                do_login(request, user)
                # Y redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'htm/login.html', {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/register')
