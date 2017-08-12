#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', include('users.urls', namespace='users')),
    url(r'', include('learning_log.urls', namespace='learning_logs')),

    #登陆页面
    rl(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]
