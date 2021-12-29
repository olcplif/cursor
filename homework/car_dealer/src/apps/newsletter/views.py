from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.http import HttpResponse

from src.apps.newsletter.forms import NewsLetterModelForm
from src.apps.newsletter.models import NewsLetter


def success_view(request):
    return render(request, 'newsletter/success.html')


class NewsLetterView(FormView):
    newsletter = NewsLetter()
    # fields = ['email']
    template_name = 'newsletter/add_subscribe.html'
    form_class = NewsLetterModelForm
    success_url = '/subscribe/success'

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse("Your email isn't valid")
