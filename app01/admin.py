from django.contrib import admin
from .models import UserProfile, Article, Comment, Card

admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Card)