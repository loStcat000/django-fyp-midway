from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User


from .forms import SignUpForm


#registration function
def signup_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend' # Set the backend attribute
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/food/list")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})



#login function
def login_request(request):
	if request.user.is_authenticated:
    		return redirect('/food/list')
	else:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('food_list')
			else:
				messages.error(request,"Invalid username or password.")
				return redirect('login.html')
		else:	
			return render(request, "login.html", context={})

#logout function
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')