import os.path
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import get_language


class Category(models.Model):
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/")

    @property
    def name(self):
        return getattr(self, 'name_{}'.format(get_language()))


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.RESTRICT)
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    subject = models.CharField(max_length=200)
    file = models.FileField(upload_to="post/")
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def ext(self):
        return os.path.splitext(self.file.path)[1][1:].lower()

    @property
    def is_image(self):
        return self.ext in ["jpeg","jpg","png","gif"]

    @property
    def is_video(self):
        return self.ext in ["mov","mp4"]

    @property
    def is_audio(self):
        return self.ext in ["wav","mp3"]