from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.
app_name = "task"
def index(request): 
    return render(request, "task/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "task/add.html")