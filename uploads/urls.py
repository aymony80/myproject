from django.conf import settings
from django.conf.urls.static import static
from uploads import views
from django.urls import path

urlpatterns = [
    path('', views.model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
