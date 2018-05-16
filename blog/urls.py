from django.conf.urls import include, url
from django.contrib import admin
from blog.views import post_detail, post_list, ListView, post_share
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}
urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$', post_detail, name='post_detail'),
    # url(r'^$', ListView.as_view(), name='post_list'),
    url(r'^(?P<post_id>\d+)/share/$', post_share, name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', post_list, name='post_list_by_tag'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
