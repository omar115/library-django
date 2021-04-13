
# Use include() to add URLS from the catalog application and authentication system
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('',RedirectView.as_view(url='catalog/', permanent=True))
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
