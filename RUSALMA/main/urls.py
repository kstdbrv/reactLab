from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/post/<int:pk>', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('chat-bots/', views.chat_bots, name='chat-bots'),
    path('usability/', views.usability, name='usability'),
    path('internet-marketing/portfolio', views.internet_portfolio, name='internet_portfolio'),
    path('web-development/portfolio', views.web_development_portfolio, name='web_development_portfolio'),
    path('internet-marketing/', views.internet_marketing, name='internet_marketing'),
]