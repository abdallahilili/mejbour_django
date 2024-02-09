from django.urls import include, path

from mejbour import admin
from .views import home, objet_detail, signalement_objet
from django.views.generic import TemplateView
from allauth.account.views import LoginView,LogoutView



urlpatterns = [
    path('', home, name='home'),
    path('objet/<int:objet_perdu_id>/', objet_detail, name='objet_detail'),
    path('signalement/', signalement_objet, name='signalement_objet'),

    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    # path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    

    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='mejbour/home.html'), name='home')
]