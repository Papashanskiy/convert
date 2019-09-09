from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext

from .models import MyModel

from .forms import MyForm


class HomePage(TemplateView):
    template_name = 'home.html'


def home_page(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():

    else:
        form = MyForm()

    img = MyModel.objects.latest('id')

    return render_to_response(
        'home.html',
        {'img': img, 'form': form},
        context_instance=RequestContext(request)
    )
