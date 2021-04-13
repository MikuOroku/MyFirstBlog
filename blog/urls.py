"""
path関数、blogappの全てビューをインポートする
"""
from django.urls import path
from . import views

# Webサイト(http://127.0.0.1:8000/)へのアクセスがあれば
# views.post_listへ
urlpatterns = [
    path('', views.post_list, name='post_list')
]