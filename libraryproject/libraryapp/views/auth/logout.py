from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    #makes http request, telling which route we want to go to.
    #just a reference to the route
    return redirect(reverse('libraryapp:home'))