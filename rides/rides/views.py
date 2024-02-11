from django.shortcuts import render


# def index(request):
#     context = {
#         "page_title": "Search and apply for jobs in the UK"
#     }
        
#     return render(request, "index.html", context)

def about(request):
    context = {
        "page_title": "About"
    }
        
    return render(request, "about.html", context)

def contact(request):
    context = {
        "page_title": "Contact"
    }
        
    return render(request, "contact.html", context)