from django.http import HttpResponse
from django.shortcuts import render_to_response

from trackQueue.databaseIO import IO
from django.template import loader
from trackQueue.models import Track
from trackQueue.databaseIO import IO


def index(request):
    """
    passes all track database objects to index.html
    :param request: 
    :return: 
    """
    # io = IO()
    # # latest_question_list = Track.objects.order_by('-pub_date')[:5]
    # trackDetails = io.getTrackDetails()
    # template = loader.get_template('trackQueue/index.html')
    # context = {
    #     'latest_track_queue': trackDetails,
    # }
    # return HttpResponse(template.render(context, request))
    return render_to_response('trackQueue/index.html', {'obj': Track.objects.all()})

# io = IO()
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the trackQueue index.")
#
# def trackList(request):
#     trackDetailsDict = io.getTrackDetails()
#     return HttpResponse(trackDetailsDict)
