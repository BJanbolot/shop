from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import RegistrationForm

# Create your views here.
User = get_user_model()

class RegisterView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form(self.get_form_class())
        return context

    
class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('product_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.get_form(self.get_form_class())
        return context

def activate(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True
    user.activation_code = ''
    user.save()
    return redirect(reverse_lazy('login'))