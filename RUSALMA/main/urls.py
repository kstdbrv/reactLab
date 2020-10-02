from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/post/<int:pk>', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('chat-bots/', views.chat_bots, name='chat-bots'),
    path('portfolio/', views.portfolio, name='portfolio'),

    path('internet-marketing/', views.internet_marketing, name='internet_marketing'),
    path('internet-marketing/digital-strategy/', views.digital_strategy, name='digital_strategy'),
    path('internet-marketing/usability/', views.usability, name='usability'),
    path('internet-marketing/seo/', views.seo, name='seo'),
    path('internet-marketing/context-advert/', views.context_advert, name='context_advert'),

    path('web-development/chat-bots/', views.chat_bots, name='chat_bots'),
    path('web-development/support/', views.support, name='support'),


]