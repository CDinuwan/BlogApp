from django.conf.urls import url
from . import view

app_name='accounts'

urlpatterns=[
    url(r'^signup/$',view.signup_view,name="signup"),
    url(r'^login/$',view.login_view,name="login"),
]
