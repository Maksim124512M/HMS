from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'hms_site/home.html'
