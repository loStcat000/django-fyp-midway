from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



from .forms import SignUpForm


# '''forgot password'''
# class MyPasswordResetView(PasswordResetView):
#     template_name = 'forgotpassword/password_reset.html'
#     success_url = reverse_lazy('forgotpassword/password_reset_done')
#     email_template_name = 'forgotpassword/password_reset_email.html'
#     subject_template_name = 'forgotpassword/password_reset_subject.txt'

# class MyPasswordResetDoneView(PasswordResetDoneView):
#     template_name = 'forgotpassword/password_reset_done.html'

# class MyPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'forgotpassword/password_reset_confirm.html'
#     success_url = reverse_lazy('forgotpassword/password_reset_complete')

# class MyPasswordResetCompleteView(PasswordResetCompleteView):
#     template_name = 'forgotpassword/password_reset_complete.html'


@login_required
def changepassword(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            # Check if old password is correct
            old_password = password_form.cleaned_data.get('old_password')
            if not request.user.check_password(old_password):
                password_form.add_error('old_password', 'Incorrect old password.')
            else:
                # Save new password and redirect
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/food/list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'profile.html', {'password_form': password_form})


#registration function

def signup_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "This email is already registered.")
            else:
                user = form.save(commit=False)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
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
from django.contrib import messages

def login_request(request):
    if request.user.is_authenticated:
        return redirect('/food/list')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('food_list')
                else:
                    messages.error(request, "Your account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
            return redirect('/login')
        else:
            return render(request, "login.html", context={})



#logout function
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')

