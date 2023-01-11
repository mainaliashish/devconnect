from django.urls import path
from . import views

# URL patterns for users app
urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
]
