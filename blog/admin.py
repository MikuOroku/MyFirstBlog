"""
ポストを追加、編集、削除する
"""
from django.contrib import admin
from .models import Post

# Postモデルを管理画面(Adminページ)で見えるようにする
admin.site.register(Post)