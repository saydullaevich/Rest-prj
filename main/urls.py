from django.urls import path
from .views import CategoryView,CategoryCreateView
from .views import PostView,PostCreateView,LikeView

app_name = 'main'

urlpatterns = [
   path('categories/',CategoryView.as_view(),name = "categories"),
   path('category/',CategoryCreateView.as_view(), name = "category"),

   path('posts/',PostView.as_view(),name='posts'),
   path('posts/<int:pk>/',PostView.as_view(),name = "posts-by-category"),

   path('post/',PostCreateView.as_view(),name="post-category"),
   path('post/<str:type>/<int:post_id>/',LikeView.as_view(),name='like')
]
