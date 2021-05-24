#Web 服务器网关接口   帮助Django提供它创建的文件  按照这个规则实现socket 用什么socker  默认用wsgiref  ,  uwsgi
"""
WSGI config for learning_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_blog.settings')

application = get_wsgi_application()
