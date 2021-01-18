from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb


def index(request):
    bbs = Bb.objects.all('published')
    # template = loader.get_template('bboard/index.html')
    # return HttpResponse(template.render({'bbs': bbs}, request))
    return render(request, 'bboard/index.html', {'bbs': bbs})
