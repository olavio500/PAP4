
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def cadast(request):

    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'your account has been successfuy created ')
        return redirect('login')
    
    return render(request,'cadastro.html')

def logar(request):
    return render(request,'login.html')
def principal(request):
    return render(request, 'index.html') 
def lognout(request):
    return render(request, 'lognout.html')   
            
