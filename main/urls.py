from django.urls import path
from .views import main, full_page, blog, sign_up, log_in, log_out, profile, add_post, change_img, edit_page, delete_page

urlpatterns = [
    path('', main, name='main'),
    path('post/<int:pk>/', full_page, name='full_page'),
    path('blog/', blog, name='blog'),
    path('sign_up/', sign_up, name='sign_up'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('profile/', profile, name='profile'),
    path('add_post/', add_post, name='add_post'),
    path('change_back_img/', change_img, name='change_back'),
    path('edit_page/<int:pk>/', edit_page, name='edit_page'),
    path('delete_page/<int:pk>/', delete_page, name='del_page')
]