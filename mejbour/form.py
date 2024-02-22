from django import forms
from .models import ObjetPerdu,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ObjetPerduForm(forms.ModelForm):
    nom_visiteur = forms.CharField(max_length=100, label='Nom')
    coordonnees = forms.CharField(max_length=255, label='Coordonnées')
    
    class Meta:
        model = ObjetPerdu
        exclude = ['utilisateur'] 
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


