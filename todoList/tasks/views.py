from django.shortcuts import render
from django import forms
from django.http import request


# Create your views here.

class NewtaskForm(forms.Form):
    task = forms.CharField(label="")


tasks = []


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    if request.method == "POST":
        form = NewtaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
        else:
            return render(request, "tasks/index.html", {
                "form": form
            })
        
    return render(request, "tasks/index.html", {
                "tasks": request.session["tasks"], "formContent": NewtaskForm()
        })
    
    return render(request, "tasks/index.html", {
        "tasks": tasks, "formContent": NewtaskForm()
    })