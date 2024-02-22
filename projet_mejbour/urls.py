
from django.urls import path, include
from django.contrib import admin
from mejbour.urls import urlpatterns as mejbour_urls
from projet_mejbour import settings
from django.conf.urls.static import static  # Assurez-vous d'importer static


urlpatterns = [

    path("admin/", admin.site.urls),
    path('', include('mejbour.urls')),

     path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('allauth.urls')),
    
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
