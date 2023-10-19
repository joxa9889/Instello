from django.shortcuts import render, redirect
from .models import Page, UserModel, Comment, Teg, Back_Img
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def main(request):
    if request.user.is_authenticated:
        obj = Page.objects.all()
        obj = reversed(obj)

        return render(request, 'index-2.html', context={
            'obj': obj
        })
    return redirect('log_in')


def full_page(request, pk):
    if request.user.is_authenticated:
        obj = Page.objects.filter(pk=pk)
        obj1 = Comment.objects.filter(page_id=pk)
        bj = Page.objects.get(pk=pk)
        is_user = str(bj.author.user_name)==str(request.user)


        if request.method == 'POST' and request.POST['comment'].strip() != '':
            comment = request.POST['comment']
            user = UserModel.objects.get(user_name=request.user.username)

            coment = Comment(title=comment, page_id=pk, author=user)
            coment.save()

        return render(request, 'blog-single.html', context={
            'obj': obj,
            'obj1': obj1,
            'is_user': is_user,
        })
    return redirect('log_in')


def blog(request):
    if request.user.is_authenticated:
        obj = Page.objects.all()
        obj = reversed(obj)
        return render(request, 'blog.html', context={
            'obj': obj
        })

    return redirect('log_in')


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        avatar = request.FILES['avatar']
        bio = request.POST['bio']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['pwd']

        new_book = UserModel(first_name=first_name, last_name=last_name, avatar=avatar, bio=bio, user_name=user_name,
                             email=email, password=password)
        new_book.save()

        new_user = User.objects.create_user(user_name, email, password)
        new_user.save()
        return redirect('log_in')

    return render(request, 'sign_up.html')


def log_in(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('main')
        else:
            message = 'User not found or password is not correct'

    return render(request, 'sign_in.html', context={
        'message': message
    })


def log_out(request):
    logout(request)
    return redirect('log_in')


def profile(request):
    if request.user.is_authenticated:
        user = UserModel.objects.get(user_name=request.user)
        posts = Page.objects.filter(author_id=user.pk)
        reversed(posts)
        imgs = []
        try:
            imgs = Back_Img.objects.get(user=user)
        except:
            pass

        return render(request, 'profile.html', context={
            'user': user,
            'obj': posts,
            'imgs': imgs,
        })

    return redirect('log_in')


def add_post(request):
    if request.user.is_authenticated:
        teg = Teg.objects.all()

        if request.method == "POST":
            title = request.POST['title']
            img = request.FILES['img']
            description = request.POST['description']
            aurhor = UserModel.objects.get(user_name=request.user)

            post = Page(title=title, img=img, description=description, author=aurhor)
            post.save()

            return redirect('profile')

        return render(request, 'add_post.html', context={
            'teg': teg
        })
    return redirect('log_in')


def change_img(request):
    if request.user.is_authenticated:
        user = UserModel.objects.get(user_name=request.user)

        try:
            imge = Back_Img.objects.get(user=user)
        except:
            pass

        if request.method == "POST":
            img = request.FILES['image']
            user = UserModel.objects.get(user_name=request.user)

            try:
                add = Back_Img(back_img=img, user=user)
                add.save()
            except:
                imge.delete()
                add = Back_Img(back_img=img, user=user)
                add.save()

            return redirect('profile')

        return render(request, 'change_back.html')
    return redirect('log_in')

def edit_page(request, pk):
    if request.user.is_authenticated:

        page_info = Page.objects.get(pk=pk)

        if request.method == 'POST':
            if 'img' in request.FILES:
                page_info.img = request.FILES['img']
            page_info.title = request.POST['title']
            page_info.description = request.POST['descript']

            page_info.save()
            bj = Page.objects.get(pk=pk)
            return redirect('full_page', bj.id)

        return render(request, 'edit_page.html', context={
            'page_info': page_info
        })

    return redirect('log_in')

def delete_page(request, pk):
    page_info = Page.objects.get(pk=pk)
    if request.method == 'POST':
        page_info.delete()
        return redirect('profile')

    return render(request, 'delete.html', context={
        'page_info': page_info
    })