from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateList
# most likely relative importing


# Create your views here.

def index(response):
    return HttpResponseRedirect("/home/")


def test2(response):
    # return HttpResponse("<h1>HAHA, I caught you this time?</h1>")
    # dictionaries can be created and passed before the return clause
    return render(response, 'main/home.html', {})
    # you can modify them as headers too if you feel like it
    # when adding name placeholders to the base.html file, it is supposed to reflect in the others of they extend it
    # but, if the dictionary is empty i.e the {} sign, the webpage turns up blank


def index2(response, ind):
    ls = ToDoList.objects.get(id=ind)
    # print("The value of ls is", ls)
    if ls in response.user.todolist.all():
        # print(response.user.todolist.all())
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("check" + str(item.id)) == "clicked":
                        item.completed = True
                    else:
                        item.completed = False

                    item.save()
            elif response.POST.get("addItem"):
                txt = response.POST.get("Item")

                if 0 < len(txt) < 3 or txt == '':
                    messages.warning(response, "Invalid entry: Too short")

                elif txt in str([x for x in ls.item_set.all()]):
                    messages.error(response, 'An entry with this content already exists!')
                else:
                    messages.success(response, 'Entry added')
                    ls.item_set.create(text=txt, completed=False)
        # item = ls.item_set.get(id=1)
        # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % ls.name)
        # return HttpResponse("<h1>%s</h1>" % ls.name)
        return render(response, 'main/list.html', {"ls": ls})
    return render(response, 'main/view.html', {})


def create(response):
    if response.method == "POST":
        form = response.POST.get("input")
        # form = CreateList(response.POST)
        # checks whether form is from a POST request or a GET request
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     new_user = form.cleaned_data["name"]
        # for ls in response.user.todolist.all():
        #     print(ls)
        if 0 < len(form) < 3 or form == '':
            messages.info(response, "Name must be more than 3 characters")

        elif form in str([ls for ls in response.user.todolist.all()]):
            messages.error(response, 'A list with this name already exists!')
        else:
            list0 = ToDoList(name=form)
            list0.save()
            response.user.todolist.add(list0)
            messages.success(response, "List created successfully!")

    else:
        redirect("/create/")
    return render(response, 'main/create.html', {})


def view2(response):
    if response.method == "POST":
        for ls in response.user.todolist.all():
            deleted = False
            if response.POST.get("check" + str(ls)) == "mainclicked":
                # if ls.list_complete:
                ls.delete()
                deleted = True
            else:
                for item in ls.item_set.all():
                    if response.POST.get(str(item.id) + "check" + str(ls)) == "clicked":
                        item.completed = True
                        print(item.text)
                        item.save()
                        print(ls.item_set.filter(completed=True).delete())
                        deleted = True
            if deleted:
                messages.success(response, "Successfully deleted")
            else:
                messages.info(response, "Nothing to delete")
    return render(response, "main/delete.html", {})


def view(response):
    if response.method == "POST":
        for ls in response.user.todolist.all():
            # print(ls)
            todolist_complete = True
            if response.POST.get("save" + str(ls)):
                for item in ls.item_set.all():
                    # print("Item set is ", len(ls.item_set.all()))
                    # item.update(str(response.POST.get("text" + str(item.id))))
                    item.text = response.POST.get("text" + str(item.id))
                    if response.POST.get("check" + str(item.id)) == "clicked":
                        # print(response.POST.get("check" + str(item.id)))
                        item.completed = True
                        todolist_complete = todolist_complete and item.completed
                    else:
                        item.completed = False
                        todolist_complete = todolist_complete and item.completed
                        # print(response.POST.get("check" + str(item.id)))
                    item.save()
                    # print(ls.item_set.filter(completed=False).delete())
                    # if 0 < len(item.text) < 3 or item.text == '':
                    #     messages.warning(response, "Invalid entry: Too short")
                    #
                    # elif item.text in str([x for x in ls.item_set.all()]):
                    #     messages.error(response, 'An entry with this content already exists!')
                    # else:
                    #     messages.success(response, 'Entry updated')
                    # print(item).
                    ls.list_complete = todolist_complete
                    ls.save()

            elif response.POST.get("addItem" + str(ls)):
                txt = response.POST.get("Item" + str(ls))

                if 0 < len(txt) < 3 or txt == '':
                    messages.warning(response, "Invalid entry: Too short")

                elif txt in str([x for x in ls.item_set.all()]):
                    messages.error(response, 'An entry with this content already exists!')
                else:
                    messages.success(response, 'Entry added')
                    ls.item_set.create(text=txt, completed=False)
                    for item in ls.item_set.all():
                        # print("Item set is ", len(ls.item_set.all()))
                        # item.update(str(response.POST.get("text" + str(item.id))))
                        if response.POST.get("check" + str(item.id)) == "clicked":
                            # print(response.POST.get("check" + str(item.id)))
                            item.completed = True
                            todolist_complete = todolist_complete and item.completed
                        else:
                            item.completed = False
                            todolist_complete = todolist_complete and item.completed
                            # print(response.POST.get("check" + str(item.id)))
                    ls.list_complete = todolist_complete
                    ls.save()
                    # ls.list_complete = False
            # if not ls.list_complete:
            #     ls.delete()
    return render(response, "main/view.html", {})


def profile(response):
    if response.method == "POST":
        for pr in response.user.profile.all():
            pass
    return render(response, 'main/profile.html', {})