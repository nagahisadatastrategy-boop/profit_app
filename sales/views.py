from django.shortcuts import render, redirect
from .forms import SalesForm
from .models import Sales

def index(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SalesForm()

    sales_list = Sales.objects.all().order_by('-date')

    return render(request, 'sales/index.html', {
        'form': form,
        'sales_list': sales_list,
    })