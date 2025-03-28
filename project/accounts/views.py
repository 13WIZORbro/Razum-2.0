from django.shortcuts import render

# Create your views here.
def logout(request):
    return render(request, "account/logout.html")