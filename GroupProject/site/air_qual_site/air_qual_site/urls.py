"""
URL configuration for air_qual_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
#for adding static in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]

#using include() to add paths from the website application
#urlpatterns += [
#    path('website/', include('website.urls')),
#]

# adding URL maps to redirect the base URL to the application
#urlpatterns += [
#    path('', RedirectView.as_view(url='website/', permanent=True)),
#]



