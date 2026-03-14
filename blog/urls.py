from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView 

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='Post_create'),
     path(' <int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('int:pk>/delete/', PostDetailView.as_view(), name='post_delete'),
]