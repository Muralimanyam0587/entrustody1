from django.contrib import admin
from django.urls import path,include
from pip import main
from .import views
urlpatterns = [

    path('', views.home ,name='home'),
    path('homelogin',views.homelogin, name="homelogin"),
    path('individual',views.individual,name='individual'),
    path('auth_login',views.auth_login, name='auth_login'),
    path('product',views.product , name='product'),
    path('contact',views.contact, name='contact'),
    path('contatus',views.contactus, name='contatcus'),
    path('logo', views.logo, name='logo'),
    path('auth_client_login', views.auth_client_login, name ='auth_client_login'),
    path('clientlogin',views.clientlogin, name='clientlogin'),
    path('clientlogut',views.clientlogout,name='clientlogout'),
    path('afterlogin', views.afterlogin , name='afterlogin'),
    path('logout',views.logout, name='logout'),
    path('user_list',views.user_list,name="user_list"),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/<int:pk>/', views.update_book, name='update_book'),
    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('regup',views.regup, name='regup'),
    

]