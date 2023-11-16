from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    # path('login/', view=views.login_user, name='login'),
    path('logout', view=views.logout_user, name='logout'),
    path('register', view=views.register_user, name='register'),
]
