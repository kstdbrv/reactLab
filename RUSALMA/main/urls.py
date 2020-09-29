from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/post/<int:pk>', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('chat-bots/', views.chat_bots, name='chat-bots'),
    path('usability/', views.usability, name='usability'),
]