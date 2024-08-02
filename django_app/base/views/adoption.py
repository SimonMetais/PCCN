from django.shortcuts import render


def adoption(request):
    return render(request, 'adoption.html')
