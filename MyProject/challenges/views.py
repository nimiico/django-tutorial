from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

days = {
    'saturday': 'this is saturday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is fiday in dictionary',
}

def days_list(request):

    days_list = list(days.keys())
    list_items = ""

    for day in days_list:
        url_path = reverse('days-of-week', args=[day])
        list_items += f'<li> <a href="{url_path}"> {day} </a> </li>\n'

    content = f'<ul>\n{list_items}\n</ul>'
    

    return HttpResponse(content)


def dynamic_days_by_number(request, day):
    days_name = list(days.keys())

    if day > len(days_name):
        return HttpResponseNotFound('day does not exist')

    redirect_day = days_name[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)

def dynamic_days(request, day):
    day_data = days.get(day)

    if day_data is not None:
        response_data = f'<h1 style="color:red">day is : {day} and data is : {day_data}</h1>'
        return HttpResponse(response_data)
    
    return HttpResponseNotFound('day does not exist')