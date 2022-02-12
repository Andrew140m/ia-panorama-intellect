from django.urls import path
from . import views

urlpatterns = [
    path('', views.usermode, name='usermode'),
    path('main.html', views.usermode, name='usermode'),
	path('mailru-domain7pthe8weV04kn7WS.html', views.mail, name='usermode')
]
