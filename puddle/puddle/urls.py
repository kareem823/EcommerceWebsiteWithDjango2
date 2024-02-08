"""
URL configuration for puddle project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core.views import index, contact

from django.conf.urls.static import static



#left off at 1hr:15mins in vid https://www.youtube.com/watch?v=ZxMB6Njs3ck&ab_channel=freeCodeCamp.org
'''>python3 -m venv env  
> python -m venv .\env
> .\env\Scripts\Activate  
> pip install django   
> django-admin startproject puddle  
> ls
> cd puddle 
> python manage.py startapp core  
> python manage.py runserver  
'''
urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
