from django.urls import path  # import the path from the django urls module
# all the views could be imported in this urls.py using this import statement
from . import views

# This is known as url configuration. You will need to import it in the main url configuration

# note that the urlpatters should always be lower case
# use the path function to call the urls. pass the route as a string and return a view on it. So basically path(request=urlpatter, response=view)
# if the playground keyword is added in the main url config you dont need to add the entire url here. just add the url pattern
urlpatterns = [
    path('hello/', views.say_hello)
]
