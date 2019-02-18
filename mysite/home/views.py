from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
def index(request):
    return render(request, 'home/index.html')

def signUp(request):

 
    
    username = request.POST['name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'home/index.html')
    else:
          user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
          user.save()

    return HttpResponseRedirect(reverse('home:index'))


