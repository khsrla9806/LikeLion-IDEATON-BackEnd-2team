from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('team_intro/', views.team_intro, name = 'team_intro'),
    path('post_list/', views.post_list, name = 'post_list'),
    path('post_list/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post_create/', views.PostCreate.as_view(), name = 'post_create'),
    path('company_list/', views.company_list, name = 'company_list'),
    path('company_detail/', views.company_detail, name = 'company_detail'),
    path('new_create/<int:pk>', views.new_comment,name='new_comment'), #댓글구현
    path('<int:detail_pk>/comment_update/<int:comment_pk>', views.comment_update, name='comment_update'),#댓글수정
    path('<int:detail_pk>/comment_delete/<int:comment_pk>', views.comment_delete, name='comment_delete')#댓글수정
]
