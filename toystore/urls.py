"""toystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from products import views 
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def root_redirect(request):
  return redirect(reverse_lazy('index'))
  



urlpatterns = [
  path('',root_redirect), path('admin/',admin.site.urls),
               path('products/',views.index,name='index'),
  path('products/<int:product_id>',views.show,name='show')
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)