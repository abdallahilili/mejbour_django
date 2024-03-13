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
    email = forms.EmailField(label='Adresse email', max_length=254, help_text='Required. Must be a valid email address.')
    username = forms.CharField(label='Nom d\'utilisateur', max_length=150, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    password1 = forms.CharField(label='Mot de passe', strip=False, widget=forms.PasswordInput, help_text='Your password must contain at least 8 characters, and can\'t be entirely numeric.')
    password2 = forms.CharField(label='Confirmer le mot de passe', strip=False, widget=forms.PasswordInput, help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


