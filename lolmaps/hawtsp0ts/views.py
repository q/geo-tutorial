from django.shortcuts import render_to_response
from django.conf import settings

from lolmaps.hawtsp0ts.models import sp0t

def index(request):
    cloudmade_api = getattr(settings, "CLOUDMADE_API", "NO_CLOUDMADE_API_SET")
    points = sp0t.objects.all()
    return render_to_response('hawtsp0ts/index.html', {'cloudmade_api':cloudmade_api, 'points':points})


