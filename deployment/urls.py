"""
URL configuration for deployment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView
#from allauth.account.decorators import secure_admin_login
#admin.autodiscover()
#admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai.urls')),
    path('accounts/', include('allauth.urls')),
    path("_allauth/", include("allauth.headless.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("Protect.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
