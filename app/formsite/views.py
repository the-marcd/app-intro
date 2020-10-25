from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import UserDataForm
from .models import UserData

def submitform(request):
    form = UserDataForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/list/')

    context= {'form': form }
        
    return render(request, 'form.html', context)

class UserListView(ListView):
    model = UserData
    template_name = 'list.html'
