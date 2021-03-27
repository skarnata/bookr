from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def search(request):
    cari = request.GET.get('search', '')
    context = {'cari': cari}
    return render(request, 'search.html', context)
