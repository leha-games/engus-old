from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin


class HomeView(TemplateView):

    template_name = 'home.html'


class AppView(LoginRequiredMixin, TemplateView):

    template_name = 'app.html'