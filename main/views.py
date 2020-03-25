from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import CreateNewList, CreateNewItem


# Create your views here.
def index(response):
    return HttpResponse("<h1>Hitesh Wadhwa</h1>")


def base(response):
    return render(response, 'main/base.html', {})


def passing(response, id):
    ls = ToDo.objects.get(id=id)
    items = list(ls.item_set.all())
    for i in range(len(items)):
        items[i] = items[i].text
    return HttpResponse("<h1>%s</h1><br><h3>%s</h3>" % (ls.name, items))


def home(response):
    return render(response, 'main/home.html')


def displaylist(response, id):
    ls = ToDo.objects.get(id=id)
    if ls in response.user.todo.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for i in ls.item_set.all():
                    if response.POST.get("c" + str(i.id)) == "clicked":
                        i.complete = True
                    else:
                        i.complete = False
                    i.save()
            elif response.POST.get("NewEntry"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    if not txt.isdigit():
                        if txt not in [x.text for x in ls.item_set.all()]:
                            ls.item_set.create(text=txt)
                        else:
                            print("Item already present")
                    else:
                        print("Only numbers cannot be A ToDO Item")
                else:
                    print("Invalid item")
            elif response.POST.get('Back'):
                return HttpResponseRedirect('http://127.0.0.1:8000/lists/')
            elif response.POST.get('DeleteItem'):
                return HttpResponseRedirect('http://127.0.0.1:8000/'+response.POST.get('DeleteItem'))
            elif response.POST.get('deleteAll'):
                ls.delete()
                return HttpResponseRedirect('http://127.0.0.1:8000/create/')
        return render(response, 'main/list.html', {"ls": ls})
    else:
        return HttpResponseRedirect('/lists')


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            if len(n) > 1 and not n.isdigit():
                t = ToDo(user=response.user,name=n)
                t.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/lists")
            else:
                print("List name cannot be that short")
    form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})


def lists(response):
    ls = response.user.todo.all()
    if response.method == "POST":
        if response.POST.get('DeleteList'):
            return HttpResponseRedirect('http://127.0.0.1:8000/' + response.POST.get('DeleteList'))
    return render(response, 'main/lists.html', {"ls": ls})


def deleteList(response):
    ls = ToDo.objects.all()
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("DeleteList"):
            for item in ls:
                if response.POST.get("l" + str(item.id)):
                    item.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/lists')
    ls = ToDo.objects.all()
    return render(response, 'main/deleteL.html', {"ls": ls})


def deleteItem(response, id):
    ls = ToDo.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("DeleteItem"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)):
                    item.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/'+str(ls.id))
    ls = ToDo.objects.get(id=id)
    return render(response, 'main/deleteI.html', {"ls": ls})

