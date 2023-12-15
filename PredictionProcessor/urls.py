from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

# app_name = 'Bot'
urlpatterns = [
        path('', views.Index, name="home"),
path('reports', views.get_reports, name='reports'),
# path('', views.Index, name='home'),
#     path('chat', views.create_post, name="chat"),

#     #  path('complete', views.CompleteView.as_view(), name='complete'),
#     path('reset-chat', views.reset_chat, name='reset-chat',),
]

