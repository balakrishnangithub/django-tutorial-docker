from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(
        r'^$',
        views.IndexView.as_view(),  # IndexView inherits `generic.ListView`
        name='index'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',  # `generic.DetailView` expects the primary key value
        views.DetailView.as_view(),  # DetailView inherits `generic.DetailView`
        name='detail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(),
        name='results'
    ),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
