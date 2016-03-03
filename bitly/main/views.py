from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from models import UrlRedirect


def index(request):
    template = loader.get_template('index.html')
    context = {
        'short_url': None,
        'message': None
    }

    if request.method == 'POST':
        new_url = UrlRedirect()
        new_url.set_url(request.POST['url'])
        if new_url.is_valid():
            new_url.make_shortened_url()
            new_url.save()
            context['short_url'] = request.build_absolute_uri(new_url.shortened_url)
        else:
            context['message'] = "URL was not valid"

    return HttpResponse(template.render(context, request))


def redirect(request, short_url):
    url_object = UrlRedirect.objects.get(shortened_url=short_url)
    return HttpResponseRedirect(url_object.original_url)
