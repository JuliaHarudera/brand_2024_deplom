"""
URL configuration for brand_2024_deplom project.

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
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from brand_2024_deplom import settings
from brand.views import category_detail
from django.urls import include
from account.views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("brand.urls")),
    path('category/<int:category_id>/', category_detail, name='category-detail'),
    path('manager/', include('manager.urls')),

    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
