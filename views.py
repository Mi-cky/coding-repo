from http.client import responses
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from authentication.forms import NewUserForm





# from authentication.models import UserProfile

# Create your views here.
# url = reverse('login')
def home(request):
    return render(request,'registration/home.html')

def signup(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return render("authentication:login.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    # if request.method == "POST":
        
    # if request.method == "POST":
	#     form = NewUserForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		login(request, user)
	# 		messages.success(request, "Registration successful." )
	# 		return render("authentication:login.html")
	# 	messages.error(request, "Unsuccessful registration. Invalid information.")
	# form = NewUserForm()
	# return render (request=request, template_name="authentication/signup.html", context={"signup_form":form})


        # username = request.POST['user']
        # fname = request.POST['fname']
        # lname = request.POST['lname']
        # email = request.POST['email']
        # password = request.POST['pass1']
        # pass2 = request.POST['pass2']
        

        # myuser = User.objects.create_user(username, email, password)
        # # profile = UserProfile.objects.create(myuser=myuser, custom_attribute='some value')
        # myuser.first_name = fname
        # myuser.second_name = lname

        # myuser.save()

        # messages.success(request, f"Your account has been successfully created.")

        # return redirect('login')        

    



    return render(request, 'registration/signup.html')



def login_user(request):
    
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass1']
        
        userv = authenticate(username = username, password=password)
        
        if userv is not None:
            login(request,userv)
            return render(request, "registration/show.html")
        else:
            messages.error("Wrong credentials")
            return redirect("home")
    
    
    
    return render(request, 'registration/login.html')


def show(request):
    return render(request, 'registration/show.html')

def about(request):
    return render(request, 'registration/about.asp')

def signout(request):
    pass