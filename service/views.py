from django.shortcuts import render

def service(request):
    context = {
        'title': 'sevice'
    }
    return render(request, 'service.html', context)

# Create your views here.
