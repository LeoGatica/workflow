from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Rol
from django import forms


  

class RegisterForm(UserCreationForm):
 
    class Meta:
        model = Usuario
        fields = ["rut", "nombres", "apellidos" , "telefono", "direccion","correo", "password1", "password2", "rol"]
        widgets={  
        
            'rut' :  forms.TextInput(attrs={'placeholder': 'Ingresar Rut'}),
            'nombres' :  forms.TextInput(attrs={'placeholder': 'Ingresar Nombres'}),
            'apellidos' :  forms.TextInput(attrs={'placeholder': 'Ingresar Apellidos'}),
            'telefono' :  forms.TextInput(attrs={'placeholder': 'Ingresar Telefono'}),
            'direccion' :  forms.TextInput(attrs={'placeholder': 'Ingresar Direccion'}),
            'correo' :  forms.TextInput(attrs={'placeholder': 'Ingresar Correo Electronico'}),
            'password1' :  forms.PasswordInput(attrs={'placeholder': 'Ingresar Contraseña'}),
            'password2' :  forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}),
            'rol': forms.Select(attrs={'class':'form-control', 'onchange' : 'Cambiar()'} ),
             
        }


    
    
    
  
   