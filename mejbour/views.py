from django.shortcuts import render, get_object_or_404, redirect

from mejbour.form import ObjetPerduForm
from .models import ObjetPerdu, ObjetVole
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    objets_perdus = ObjetPerdu.objects.all()
    return render(request, 'mejbour/home.html', {'objets_perdus': objets_perdus})

def objet_detail(request, objet_perdu_id):
    objet_perdu = get_object_or_404(ObjetPerdu, pk=objet_perdu_id)
    return render(request, 'mejbour/objet_detail.html', {'objet_perdu': objet_perdu})

def signalement_objet(request):
    if request.method == 'POST':
        form = ObjetPerduForm(request.POST, request.FILES)
        if form.is_valid():
            nom_utilisateur = form.cleaned_data['nom_utilisateur']
            coordonnees_utilisateur = form.cleaned_data['coordonnees_utilisateur']
            nom = form.cleaned_data['nom']
            description = form.cleaned_data['description']
            lieu_trouve = form.cleaned_data['lieu_trouve']
            coordonnees = form.cleaned_data['coordonnees']
            image = form.cleaned_data['image']
            
            objet_perdu = ObjetPerdu.objects.create(
                nom=nom,
                description=description,
                lieu_trouve=lieu_trouve,
                nom_visiteur=nom_utilisateur,
                coordonnees=coordonnees_utilisateur,
                image=image
            )
            objet_perdu.save()
            return redirect('home')
    else:
        form = ObjetPerduForm()
    
    return render(request, 'mejbour/signalement_objet.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirigez vers la page de connexion après l'inscription
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  # Redirigez vers la page d'accueil après la connexion
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def login(request):
#     return render(request, 'login.html')
# @login_required

# def user_logout(request):
#     logout(request)
#     return redirect('home')  # Redirigez vers la page d'accueil après la déconnexion