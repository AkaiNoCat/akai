from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', first_index, name='firstIndex'),
]
