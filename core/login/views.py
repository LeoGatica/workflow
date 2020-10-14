from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from core.mainwork.views import logged_in
from django.contrib import messages



class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context


def Registro(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        rut = response.POST['rut'] 
        email = response.POST['correo'] 
        password1 = response.POST['password1']
        password2 = response.POST['password2']

        form.is_valid()
        print(form.errors)

      
        if form.is_valid():     
            form.save()

        return redirect(Registro)    
    else:
        form = RegisterForm()

    return render(response, "Registro/RegistrarUsuario.html", {"form":form} )        
# Create your views here.

