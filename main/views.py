from rest_framework.generics import CreateAPIView,ListAPIView
from .models import Category,Post
from .serializers import CategorySerializer,CategoryEditSerializer,PostEditSerializer,PostSerializer
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CategoryView(ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = None
    queryset = Category.objects.all()

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).order_by('id')

class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryEditSerializer
    queryset = Category.objects.all()

class PostView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset).order_by('-id')

        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = queryset.filter(category_id=pk)

        return queryset

class PostCreateView(CreateAPIView):
    serializer_class = PostEditSerializer
    queryset = Post.objects.all()

class LikeView(APIView):
    def get(self,request,post_id,type):
        with transaction.atomic():
            post = Post.objects.select_for_update().get(id=post_id)

            if type == "like":
                post.like +=1
            else:
                post.dislike +=1

            post.save()
            return Response()


