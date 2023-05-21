from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user.save()
        return user

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_login_view(self, request, **kwargs):
        view = super().get_login_view(request, **kwargs)
        view.template_name = 'my_github_login.html'
        return view