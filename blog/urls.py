from django.contrib import admin
from django.urls import path,include
from blog import views
from django.conf.urls import url, include




urlpatterns = [
    path('',views.Aboutview,name='about'),
    path('post',views.PostListView.as_view(),name='post_list'),
    path(r'^post/(?P<pk>\d+)$',views.PostView.as_view(),name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(),name='post_new'),
    path(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='post_edit'),
    path(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete_confirm'),
    path('drafts/',views.DraftlistView.as_view(),name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/add_comment_to_post/$',views.add_comment_to_post,name='add_comment'),
    path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    path(r'^comment/(?P<pk>\d+)/comment_delete/$',views.comment_delete,name='comment_delete'),
    path('post/(?P<pk>\d+)>/publish/', views.post_publish, name='post_publish'),
]
