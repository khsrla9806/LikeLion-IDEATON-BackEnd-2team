from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('team_intro/', views.team_intro, name = 'team_intro'),
    path('post_list/', views.post_list, name = 'post_list'),
    path('post_list/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post_create/', views.PostCreate.as_view(), name = 'post_create'),
    path('post_edit/<int:pk>', views.post_edit, name = 'post_edit'),
    path('post_list/post_delete/<int:pk>/', views.post_delete, name = 'post_delete'),
    path('company_list/', views.company_list, name = 'company_list'),
    path('company_detail/', views.company_detail, name = 'company_detail'),
]
