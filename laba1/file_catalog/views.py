from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.db.models import Q

from file_catalog.forms import FileForm
from file_catalog.models import File

def start_page(request):
    return render(request, 'templates/base.html')


def searchfile(request):
    query= request.POST.get('search', '')
    
    stop_mess = str()
    forbid_sym = tuple('.,?!-\/+=\"\"\'')
    file_list = []
    is_empty = True

    if query in forbid_sym:
        stop_mess = 'Wrong characters'

    if query:
        is_empty = False
        result = File.objects.filter(Q(description__icontains=query) | Q(my_file__icontains=query))
        for i in result:
            file_list.append(i)
    
    results = {
        'result':file_list,
        'mess': stop_mess,
        'empty': is_empty
    }

    return render(request, 'templates/search.html', results)


def upload_book(request):
    form = {}
    if request.method == 'POST':
        temp = request.POST
        request.POST = ''
        form = FileForm(temp, request.FILES)
        if form.is_valid():
            form.save()
    if request.method == 'GET':
        my_file = FileForm()
    return render(request, 'templates/upload_book.html',
        {
             'form':form
        }
    )
