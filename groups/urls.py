from django.conf.urls import url
from groups import views

app_name = 'groups'
urlpatterns = [
    url(r'^$', views.GroupListView.as_view(), name='index'),
    url(r'^add_group/$', views.GroupCreateView.as_view(), name='add'),
    url(r'^edit_group/(?P<pk>\d+)/$', views.GroupUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='detail'),
    url(r'^delete_group/(?P<pk>\d+)/$', views.GroupDeleteView.as_view(), name='delete'),
]
