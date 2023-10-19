from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=70)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Back_Img(models.Model):
    back_img = models.ImageField(upload_to='back/', null=True, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.back_img}'


class Teg(models.Model):
    teg = models.CharField(max_length=40)

    def __str__(self):
        return self.teg


class Page(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    teg = models.ManyToManyField(Teg, null=True, blank=True)

    def edit_page(self, img, title, description):
        self.title = title
        self.img = img
        self.description = description

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=300)
    page = models.ForeignKey(Page, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
