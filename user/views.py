from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, TemplateView
from .forms import UserSignUp
from .models import User

# Create your views here.
class UserSignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = UserSignUp
    success_url = reverse_lazy('login')

class UserDetailView(DetailView):
    template_name = 'user/detail.html'
    model = User

class UserScannerView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'user/scanner.html'

    def test_func(self):
        return self.request.user.is_staff