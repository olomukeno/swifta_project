"""
django-admin startproject <name> - required to create a new site

To run the server, cd into the manage.py directory and call 'python manage.py runserver'.
By default this runs on port 8000, so if you wanna change the port it runs on add the port no. in front of runserver

At this stage only the frame where the service will be run has been created. As a result, it would be necessary to
create the app and this can be done by the command python manage.py startapp <name>

within the app folder you will create previously, there will be a number of files that will be created; one of which is
views.py. This is essential in handling httprequest in showing up things in the website

Within urls.py(created within the app folder), the paths to the different webpages are formed
there is no limit to the number of apps than can be created.

In the main project folder, the urls.py page there controls the navigation of the website to different pages. There the
links are formed. In doing this, there two parameters needed: the path and the .py file to be redirected to

Later on you'll move to the settings.py in the main project directory to add the app we're working on and tell django
that this needs to be configured when configurations are made

When modifying the models.py file, to tell django that modifications have been made we use
python manage.py makemigrations <name of app>. To apply those migrations, python manage.py migrate

Nest is to add things to the database. To do this we call python manage.py shell. This is cause:
Most common cause of this is that you're just running python instead of using python manage.py shell, which means you
need to manually set the DJANGO_SETTINGS_MODULE environment variable so Django knows where to find your settings
(manage.py shell does that for you automatically).

**using the code
from test_site.main.models import Item, ToDoList
list0 = ToDoList(name="Kenny\'s List")
list0.save()
ToDoList.objects.all()
# returns a queryset of all created objects

ToDoList.objects.get(id=1)
# used to get only 1 object based on id

ToDoList.objects.get(name="Kenny's List")
# returns the name of a list based on given name

list0.item_set.all()
# since there is a relation between items (that ForeignKey defined at the beginning of the Item class) and todolist each
 list automatically has a set that can store different items

list0.item_set.create(text="Believe in yourself more", completed=False)
# creates a new item, all variables must be supplied
list0.item_set.get(id=1)
# gets an item on the list through an id number
# NOTE TO SELF IT IS AN ACTUAL LIST... MAYBE?
# NB: You can also do stuff like x = ToDoList.objects so you don't need to keep typing over and over again

# Filtering also works here
ToDoList.objects.filter(name__startswith="<:argument>")
# ToDoList.objects.filter(id=<num>) # can be shortened to t = ToDoList.objects
# Can also filter with the id number

# To delete an object, we use
ToDoList.objects.get(id=<num>).delete() # Remember can also be shortened

# To create a user on the admin page we use python manage.py createsuperuser
# For any created databases, we'll have to add them directly to the user admin page
# To do this, you'll go to the admin.py file and register the list

# In reality, typing html directly to the code isn't a good way to create a website and therefore it is much better
practice to create templates and then render them unto the website
# On this topic, each website normally has a base template that all other webpages have. Therefore, we can apply this to
 any other html file by applying this at the top of the file: {% extends <location> %}
"""