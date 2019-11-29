from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView, GroupView, CommentView

group_list = GroupView.as_view({
    'get': 'list'
})
group_detail = GroupView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

post_list = PostView.as_view({
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentView.as_view({
    'get': 'list',
})
comment_detail = CommentView.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('group/', group_list, name='group_list'),
    path('group/<int:pk>/', group_detail, name='group_detail'),

    path('posts/<int:group>/', post_list, name='post_list'),
    path('posts/<int:group>/<int:pk>/', post_detail, name='post_detail'),

    path('posts/<int:group>/<int:post>/comment',
         comment_list, name='comment_list'),
    path('posts/<int:group>/<int:post>/comment/<int:pk>',
         comment_detail, name='comment_detail'),
])