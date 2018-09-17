from .models import Contact
from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    template_name = "fortytwoapps/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context