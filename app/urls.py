from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include(('bases.urls','bases'), namespace='bases')),
    path('elim/',include(('elim.urls','elim'), namespace='elim')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('viviana/',include(('viviana.urls','viviana'), namespace='viviana')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
