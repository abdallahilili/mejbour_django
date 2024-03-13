from django.urls import include, path

from mejbour import admin
from .views import InscriptionView, home, objet_detail, propre, signalement_objet,supprimer_objet,submit_form_view,user_profile,marquer_objet_trouve, modifier_objet


from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', home, name='home'),
    
        path('propre/', propre, name='propre'),

    path('objet/<int:objet_perdu_id>/', objet_detail, name='objet_detail'),
    path('signalement/', signalement_objet, name='signalement_objet'),

        path('modifier_objet/<int:objet_id>/', modifier_objet, name='modifier_objet'),


    path('supprimer_objet/<int:objet_id>/', supprimer_objet, name='supprimer_objet'),


    path('submit-form/', submit_form_view, name='submit-form'),

    path('profile/', user_profile, name='user_profile'),
    path('marquer-objet-trouve/<int:objet_id>/', marquer_objet_trouve, name='marquer_objet_trouve'),


    

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),

    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


   
#----------------------------------------------------------------
    # path('accounts/login/', LoginView.as_view(), name='account_login'),
    # path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    # path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    

   
    # path('accounts/', include('allauth.urls')),
    # path('home/', TemplateView.as_view(template_name='mejbour/home.html'), name='home')
]