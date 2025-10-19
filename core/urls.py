from django.urls import path
from core.views import me

urlpatterns = [
    path('me/', me, name='get_profile'), 
]
