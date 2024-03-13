from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from mejbour.form import CustomUserCreationForm, ObjetPerduForm
from .models import ObjetPerdu, ObjetVole
# from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy


from django.core.paginator import Paginator

# from django.shortcuts import render, redirect
from django.contrib import messages  # Importez le module messages



def home(request):
    # Récupérer tous les objets perdus et les trier par date de signalement la plus récente
    objets_perdus_list = ObjetPerdu.objects.all().order_by('-date_signalement')

    # Paginer les objets perdus avec 10 objets par page
    paginator = Paginator(objets_perdus_list, 10)
    page_number = request.GET.get('page')
    objets_perdus = paginator.get_page(page_number)

    return render(request, 'mejbour/home.html', {'objets_perdus': objets_perdus})

def propre(request):
    return render(request, 'info.html')

def objet_detail(request, objet_perdu_id):
    objet_perdu = get_object_or_404(ObjetPerdu, pk=objet_perdu_id)
    return render(request, 'mejbour/objet_detail.html', {'objet_perdu': objet_perdu})


def signalement_objet(request):
    if request.method == 'POST':
        form = ObjetPerduForm(request.POST, request.FILES)
        if form.is_valid():
            # Pas besoin de récupérer utilisateur à partir des données du formulaire
            objet_perdu = form.save(commit=False)
            
            # Ajouter l'utilisateur connecté à l'objet perdu
            objet_perdu.utilisateur = request.user
            
            # Enregistrer l'objet perdu avec les informations complètes
            objet_perdu.save()
            
            # Afficher un message de succès
            messages.success(request, 'L\'objet a été ajouté avec succès.')
            
            # Rediriger vers la page d'accueil ou une autre vue
            return redirect('home')
    else:
        form = ObjetPerduForm(initial={'nom_visiteur': request.user.username})
    
    # Afficher le formulaire dans le template
    return render(request, 'mejbour/signalement_objet.html', {'form': form})



def modifier_objet(request, objet_id):
    objet = get_object_or_404(ObjetPerdu, id=objet_id)
    if request.method == 'POST':
        form = ObjetPerduForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Rediriger vers la page de profil de l'utilisateur
    else:
        form = ObjetPerduForm(instance=objet)
    return render(request, 'modifier_objet.html', {'form': form, 'objet': objet})


def supprimer_objet(request, objet_id):
    objet = get_object_or_404(ObjetPerdu, pk=objet_id)
    if request.method == 'POST':
        objet.delete()
        return JsonResponse({'message': 'L\'objet a été supprimé avec succès'}, status=200)
    else:
        return JsonResponse({'message': 'La requête doit être de type POST'}, status=400)

def submit_form_view(request):
    if request.method == 'POST':
        form = ObjetPerduForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or return a response
    else:
        form = ObjetPerduForm()
    return render(request, 'submit_form.html', {'form': form})




def user_profile(request):
    # Récupérer les informations de l'utilisateur connecté
    user = request.user
    
    # Récupérer les objets signalés par l'utilisateur
    objet_perdu = ObjetPerdu.objects.filter(utilisateur=user).order_by('-date_signalement')
    
    context = {
        'user': user,
        'objets_signales': objet_perdu
    }
    return render(request, 'user_profile.html', context)




def marquer_objet_trouve(request, objet_id):
    # Récupérer l'objet signalé à l'aide de son identifiant (objet_id)
    objet = get_object_or_404(ObjetPerdu, id=objet_id)
    
    # Marquer l'objet comme trouvé ou non trouvé en fonction de son état actuel
    objet.objet_trouve = not objet.objet_trouve
    
    # Enregistrer les modifications dans la base de données
    objet.save()
    
    # Rediriger vers la page de profil de l'utilisateur ou une autre vue
    return redirect('user_profile') 





class InscriptionView(CreateView):
    form_class = CustomUserCreationForm 
    template_name = 'inscription.html'  # Le nom du template d'inscription que vous devez créer
    success_url = reverse_lazy('login')  # Redirige 
# ----------------------------------------------------------------
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    #     form = ObjetPerduForm()
    
    # return render(request, 'mejbour/signalement_objet.html', {'form': form})

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