from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from wish import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishlist/', include('wishlist.urls')),
    path('', views.index, name='index'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)