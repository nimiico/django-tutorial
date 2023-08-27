from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

days = {
    'saturday': 'this is saturday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': None
}

def dynamic_days(request, day):
    day_data = days.get(day)

    if day_data is None:
        raise Http404()
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)

    context = {
        "data": day_data,
        "day": f'selected day is {day}',
    }
    return render(request, 'challenges/challenge.html', context)
    # response_data = render_to_string('challenges/challenge.html')
    # return HttpResponse(response_data)

def days_list(request):

    days_list = list(days.keys())
    context = {
        'days': days_list
    }
    return render(request, "challenges/index.html", context)


def dynamic_days_by_number(request, day): 
    days_name = list(days.keys())

    if day > len(days_name):
        return HttpResponseNotFound('day does not exist')

    redirect_day = days_name[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)
