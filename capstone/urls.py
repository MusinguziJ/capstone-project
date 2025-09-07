from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('facilities/', include('facilities.urls')),
    path('participants/', include('participants.urls')),
    path('programs/', include('programs.urls')),
    path('projects/', include('projects.urls')),
    path('equipment/', include('equipment.urls')),
    path('outcomes/', include('outcomes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)