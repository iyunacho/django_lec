from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def activities(request):
    return render(request, 'pages/activities.html')

def summer(request):
    return render(request, 'pages/summer.html')

def winter(request):
    return render(request, 'pages/winter.html')

def culture(request):
    return render(request, 'pages/culture.html')

def cities(request):
    return render(request, 'pages/cities.html')

def vienna(request):
    return render(request, 'pages/vienna.html')

def graz(request):
    return render(request, 'pages/graz.html')

def salzburg(request):
    return render(request, 'pages/salzburg.html')