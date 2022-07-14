from django.urls import path
from . import views
app_name = 'search' # 템플릿과 urls.py에서 이용할 수 있도록 지정
# ?: (urls.W005) URL namespace 'search' isn't unique. You may not be able to reverse all URLs in this namespace 오류 발생함.

urlpatterns =[
    path('',views.searchResult, name='searchResult'),
    
]