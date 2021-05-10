from django.urls import path, re_path
from . import views
from registro import views as v

urlpatterns = [
    path('<int:id>', views.index, name = 'index'),
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('home/', views.home, name = 'home'),
    path('salir/', views.logged_out, name = 'logged_out'),
    path('editar_datos/', views.editar, name = 'editar'),
    path('accounts/login/', views.home, name = 'home'),
    path('profile/<str:nom>', views.profile, name='profile' ),
    path('actualizar/<str:nom>/',views.actualizar_datos, name='actualizar'),
]