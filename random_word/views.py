from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not "count" in request.session:
        request.session["count"] = 0
    else: request.session["count"] += 1
    context = {
        "random" : get_random_string(length=14, allowed_chars="HELLO")
    }
    return render(request, "random_word\index.html", context);

def reset(request):
    del request.session["count"]
    return render(request, "random_word\index.html");
