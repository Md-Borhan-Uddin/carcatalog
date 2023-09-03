from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView,UpdateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View


from accounts.forms import LoginForm, RegisterForm, UserUpdateForm
from accounts.models import User
# Create your views here.


class AdminDashboardView(View):
    template_name = 'accounts/admin.html'
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)

class UserProfileView(UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    form_class = UserUpdateForm
    pk_url_kwarg = 'pk'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['user'] = User.objects.get(id=self.kwargs.get('pk'))
        return context
    
    
    def form_valid(self, form):
        print('form data')
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print('form error')
        print(form.cleaned_data)
        return super().form_invalid(form)


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
        
        return render(request,self.tamplates_name,{'form':form})

class LogoutView(LogoutView):
    def get_success_url(self,*args, **kwargs):
        return reverse_lazy('home')