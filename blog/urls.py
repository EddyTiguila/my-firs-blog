from django.conf.urls import include, url
from .  import views

urlpatterns =[
url(r'^$', views.listado, name="listado"),
url(r'^post/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
url(r'^post/nuevo/$', views.nuevoPost, name='nuevoPost'),
url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
