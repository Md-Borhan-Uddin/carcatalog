from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.messages.views import SuccessMessageMixin


from accounts.forms import LoginForm, RegisterForm
from accounts.models import User
# Create your views here.

class UserCreateView(SuccessMessageMixin,CreateView):
    model = User
    template_name = "accounts/registration.html"
    form_class = RegisterForm
    success_message = "User Create successfully now you can login"


class UserLoginView(View):
    tamplates_name = 'accounts/login.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.tamplates_name,{'form':LoginForm(request=request)})
    
    def post(self,request, *args, **kwargs):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse_lazy('home'))
        print(form)
        return render(request,self.tamplates_name,{'form':form})
        