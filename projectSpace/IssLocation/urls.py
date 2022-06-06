from django.urls import path
from . import views


urlpatterns = [
    path('', views.say_hello, name = 'home'),
    path('ISSlocation/', views.ISSlocation),
    path('humanInSpace/', views.humanInSpace),
    # path('iss_location/', views.iss_location, name = 'issLocation'),
]