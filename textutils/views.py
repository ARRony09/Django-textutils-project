# This file is created by Rony

from django.http import HttpResponse
from django.shortcuts import render
import re


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', "off")
    fullcaps = request.POST.get('fullcaps', "off")
    newlineremover = request.POST.get('newlineremover', "off")
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', "off")
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Punctuations', 'analyzed_text': analyzed}
        # this is for using multibutton funtionality
        djtext = analyzed

    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'All Capital letter', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
                else:
                    print("no")
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = re.sub(" +", " ", djtext)
        params = {'purpose': 'Remove extra lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext) - djtext.count(" ")
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse('Please select some button')

    return render(request, 'analyze.html', params)

