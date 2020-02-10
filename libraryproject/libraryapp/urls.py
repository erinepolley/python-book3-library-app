from django.urls import include, path
from .views import *


app_name = "libraryapp"

#the name makes it so that you can just reference a path.
#kind of like a variable name.
#decoupling--don't have to hard code route in other files.
#so when you change the name of a route, don't have to change the route path wherever it's referenced.

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    #already built into Python, don't have to build them, just using themn
    path('accounts/', include('django.contrib.auth.urls')),

    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),

    path('librarians/', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),

    path('libraries/form', library_form, name='library_form'),
    path('libraries/', list_libraries, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library'),


    path('logout/', logout_user, name='logout'),  
]