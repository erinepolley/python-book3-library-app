from django.urls import include, path
from .views import *


app_name = "libraryapp"

#the name makes it so that you can just reference a path.
#kind of like a variable name.
#decoupling--don't have to hard code route in other files.
#so when you change the name of a route, don't have to change the route path wherever it's referenced.

urlpatterns = [
    path('', book_list, name='home'),
    path('books/', book_list, name='books'),
    #already built into Python, don't have to build them, just using them
    path('accounts/', include('django.contrib.auth.urls')), 
    # path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),  
]