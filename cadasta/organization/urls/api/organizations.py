from django.conf.urls import include, url

from ...views import api

urlpatterns = [
    url(
        r'^$',
        api.OrganizationList.as_view(),
        name='list'),
    url(
        r'^(?P<slug>[-\w]+)/$',
        api.OrganizationDetail.as_view(),
        name='detail'),
    url(
        r'^(?P<slug>[-\w]+)/users/$',
        api.OrganizationUsers.as_view(),
        name='users'),
    url(
        r'^(?P<slug>[-\w]+)/users/(?P<username>[-\w]+)/$',
        api.OrganizationUsersDetail.as_view(),
        name='users_detail'),
    url(
        r'^(?P<slug>[-\w]+)/projects/$',
        api.OrganizationProjectList.as_view(),
        name='project_list'),
    url(
        r'^(?P<organization>[-\w]+)/projects/(?P<project>[-\w]+)/$',
        api.ProjectDetail.as_view(),
        name='project_detail'),
    url(
        r'^(?P<organization>[-\w]+)/projects/(?P<project>[-\w]+)/users/$',
        api.ProjectUsers.as_view(),
        name='project_users'),
    url(
        r'^(?P<organization>[-\w]+)/projects/'
        '(?P<project>[-\w]+)/users/(?P<username>[-\w]+)/$',
        api.ProjectUsersDetail.as_view(),
        name='project_users_detail'),
    url(
        r'^(?P<organization>[-\w]+)/projects/'
        '(?P<project_slug>[-\w]+)/spatial/',
        include('spatial.urls.api.spatial', namespace='spatial_urls')),
]