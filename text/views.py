from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'Name': 'Rahul', 'Place': 'Sagar, MP'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinereover = request.POST.get('newlinereover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Upper', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlinereover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter == "on":
        analyzed = djtext
        params = {'purpose': 'The Number of Characters in Given String is - ', 'analyzed_text': len(analyzed)}

    if removepunc != 'on' and fullcaps != 'on' and newlinereover != 'on' and extraspaceremover != 'on' and charcounter != 'on':
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


def contactus(request):
    return render(request, 'contactus.html')
