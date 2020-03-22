from django.shortcuts import render
from django.http import HttpResponse

from basic_app.forms import ShopKeeperRegistrationForm,UserProfileInfoForm,UserFeedbackForm


# for login we are importing following
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'basic_app/index.html',)


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def ShopKeeper_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    '''
    user_form = ShopKeeperRegistrationForm()
    profile_form = UserProfileInfoForm()
    '''

    if request.method == "POST":
        user_form = ShopKeeperRegistrationForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user 

            if 'number' in request.FILES:
                profile.number = request.FILES['phone_number']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = ShopKeeperRegistrationForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def ShopKeeper_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                #return HttpResponseRedirect(reverse('conformation_login'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request,'basic_app/login.html',{})


def UserFeedback(request):

    form = UserFeedbackForm()

    if request.method == 'POST':
        
        form = UserFeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error Form!")

    else:
        return render(request,'basic_app/UserFeedback.html',{'form':form})


'''

def conformation_login(request):
    return HttpResponse("You are logged in!")
'''