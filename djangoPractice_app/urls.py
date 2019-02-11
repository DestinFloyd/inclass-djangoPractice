from django.urls import path
from .views import *

urlpatterns = [
    path('', helloIndex),
    path('<int:banana_id>/', showBananaPage)
]