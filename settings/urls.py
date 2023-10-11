from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
# from settings import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu_app.urls')),
]

# if base.DEBUG:
    # urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
