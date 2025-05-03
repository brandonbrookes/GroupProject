# Create your views here.
from django.shortcuts import render
from django.template import loader


from django.http import HttpResponse

def postCodeLookUp(request):
    template = loader.get_template('postCodeLookUp.html')
    return HttpResponse(template.render())
