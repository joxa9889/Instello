from django.contrib import admin
from .models import UserModel, Page, Teg, Comment, Back_Img

# Register your models here.

admin.site.register(Comment)
admin.site.register(Teg)
admin.site.register(UserModel)
admin.site.register(Page)
admin.site.register(Back_Img)
