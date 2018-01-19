from django.shortcuts import render


def index(request):
    return render(request, 'plantapp/home.html')

def edit(request):
    return render(request, 'plantapp/plantlist.html')

def contact(request):
    return render(request, 'plantapp/basic.html', {'content':['You can contact me at','rastogiunm@gmail.com']})