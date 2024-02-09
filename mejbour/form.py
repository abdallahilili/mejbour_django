from django import forms
from .models import ObjetPerdu,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ObjetPerduForm(forms.ModelForm):
    nom_utilisateur = forms.CharField(max_length=100, label='Nom')
    coordonnees_utilisateur = forms.CharField(max_length=255, label='Coordonnées')
    
    class Meta:
        model = ObjetPerdu
        fields = ['nom_utilisateur', 'coordonnees_utilisateur', 'nom', 'description', 'lieu_trouve', 'coordonnees', 'image']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']