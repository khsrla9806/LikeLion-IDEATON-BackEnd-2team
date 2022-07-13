from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('team_intro/', views.team_intro, name = 'team_intro'), #팀소개
    path('post_list/', views.post_list, name = 'post_list'), #게시글목록
    path('post_list/<int:pk>/', views.post_detail, name = 'post_detail'), #게시글상세
    path('post_create/', views.post_create, name = 'post_create'), #게시글생성
    path('post_edit/<int:pk>', views.post_edit, name = 'post_edit'), #게시글수정
    path('post_list/post_delete/<int:pk>/', views.post_delete, name = 'post_delete'), #게시글삭제
    path('company_list/', views.company_list, name = 'company_list'), #기업목록
    path('company_detail/', views.company_detail, name = 'company_detail'), #기업상세
    path('new_create/<int:pk>', views.new_comment,name='new_comment'), #댓글구현
    path('<int:detail_pk>/comment_update/<int:comment_pk>', views.comment_update, name='comment_update'),#댓글수정
    path('<int:detail_pk>/comment_delete/<int:comment_pk>', views.comment_delete, name='comment_delete'), #댓글수정
]
