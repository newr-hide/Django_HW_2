import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    with open(r'D:\Projects\django_HW\2_HW\Django_HW_2\pagination\data-398-2018-08-30.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        stansion_list =[]
        for row in reader:
            stansion_tmp = {k: row[k] for k in row.keys() if k in ['Name', 'Street', 'District']}

            stansion_list.append(stansion_tmp)
            page_number = request.GET.get('page',1)
            paginator = Paginator(stansion_list, 20)
            page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

