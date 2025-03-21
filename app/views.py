import json
import webbrowser

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from app.models import Url
from django.views.decorators.csrf import csrf_exempt

import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "app/shorten.html", {})

@csrf_exempt
def shorten_url(request):
    if request.method == "POST":
        data = json.loads(request.body)
        original_url = data["url"]
        custom_url = data["custom_url"].strip()
        short_url = custom_url
        if custom_url and Url.objects.filter(short_url=custom_url).exists():
            return JsonResponse({'error': "Custom URL is taken. Please try again."}, status=400)
        url = Url.objects.create(original_url=original_url)
        url.short_url = short_url or Url.create_short_url(original_url) 
        url.save(update_fields=['short_url']) 
        return JsonResponse({'short_url': url.short_url})

def redirect(request, short_url):
    url = Url.objects.get(short_url=short_url)
    if url:
        original_url = url.original_url 
        webbrowser.open(original_url)
        return HttpResponse("Redirecting")
    raise Http404("Short url does not exist")
