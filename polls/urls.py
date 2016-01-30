from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
   # url(r'^$', views.post_list, name='post_list'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
