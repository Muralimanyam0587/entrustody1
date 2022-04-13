from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User ,auth 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import BookForm ,CreateUserForm
from .models import Book
def clientlogin(request):
    return render(request, 'clientlogin.html')
def clientlogout(request):
     return render(request, 'clientlogout.html')
def home(request):
    return render(request, 'home.html')
def homelogin(request):
    if request.method =='POST':
        
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        
            
            
      


        if User.objects.filter(username=username).exists():
                messages.info(request, 'username existed')
                return redirect('homelogin')

        elif User.objects.filter(email=email).exists():
             messages.info(request, ' email exists')
             return redirect('homelogin')
        else:
         user =User.objects.create_user(username=username, password=password, email=email, )
         user.save();
        return redirect('auth_login')
   



    return render(request , 'homelogin.html')

def individual(request):
   return render(request, 'individual.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request ,'product.html')

def auth_login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('afterlogin')

        else: 
            messages.info(request,'invalid details')
            return redirect('auth_login' )
       

      

     return render(request,'auth_login.html')


def auth_client_login(request):
  if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('home')
  else:
        form = CreateUserForm()
        context = {
        'form': form
    }
  return render(request, 'auth_client_login.html', context)

 

@login_required
def afterlogin(request):
     return render(request, 'afterlogin.html')


def contactus(request):
    return render(request, 'contactus.html')

def logo(request):
    return render(request, 'logo.html')

from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {
        'users': users
    })



@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

@login_required
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


@login_required
def update_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.edit()
    return redirect('book_list')



class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'

# @login_required
class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
@login_required
def regup(request):
    return render('requp.html')

def logout(request):

    auth.logout(request)
    return render(request, 'auth_login.html')