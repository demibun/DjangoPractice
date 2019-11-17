from django.shortcuts import render, redirect
from django import forms
from django.views.generic import View
from .models import Name

class NameForm(forms.Form):
    your_name = forms.CharField(label='Favorite Name', max_length=100)


class Get_name(View):
    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['your_name']
            print('new name = ', new_name)
            names = Name(name = new_name)
            names.save()
            return redirect('result/')

    def get(self, request):
            form = NameForm()
            return render(request, 'polls/name.html', {'form': form})


def result(request):
    names = Name.objects.all()
    return render(request, 'polls/result.html', {'names' : names})
