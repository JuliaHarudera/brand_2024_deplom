from django.urls import path
#from .views import main
from .views import IndexPage

app_name = 'brand'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
]
