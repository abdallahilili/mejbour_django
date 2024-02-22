from django.db import models

# objets_perdus/models.py
from django.db import models
from django.contrib.auth.models import User

class ObjetPerdu(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    lieu_trouve = models.CharField(max_length=255)
    nom_visiteur = models.CharField(max_length=100)
    coordonnees = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/objets_perdus/', null=True, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Associer l'objet perdu à un utilisateur
    objet_trouve = models.BooleanField(default=False)  # Nouveau champ pour indiquer si l'objet est trouvé ou non



    def __str__(self):
        return self.nom

class ObjetVole(models.Model):
    objet_perdu = models.OneToOneField(ObjetPerdu, on_delete=models.CASCADE)
    signale_par = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_signalement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ObjetVolé: {self.objet_perdu.nom} - Signalé par: {self.signale_par}"
