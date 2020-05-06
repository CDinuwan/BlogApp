from django.urls import path
from . import view
from django.conf.urls import url

app_name='articles'

urlpatterns = [
    url(r'^$',view.article_list,name="list"),
    url(r'^create/$',view.article_create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$',view.article_detail,name="detail"),
]
