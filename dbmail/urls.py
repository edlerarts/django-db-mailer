# -*- encoding: utf-8 -*-

from django.conf.urls import url

from .views import send_by_dbmail, mail_read_tracker


urlpatterns = [
    url(r'^api/', send_by_dbmail, name='db-mail-api'),
    url(r'^mail_read_tracker/(.*?)/$',
        mail_read_tracker, name='db-mail-tracker'),
]
