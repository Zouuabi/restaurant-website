# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from django.http import HttpResponse
from .models import Menu
#


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu (request):
    try:
        menu_data = Menu.objects.all()
    except Menu.DoesNotExist:
        pass 
    main_data = {'menu': menu_data}
    
    return render(request,'menu.html',context=main_data)

def item_description(request,pk=None):
    if(pk != None):
        item = Menu.objects.get(pk = pk )
    else:
        item = ''
    return render(request,'item.html',{'item':item})