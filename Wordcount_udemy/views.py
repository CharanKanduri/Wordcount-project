from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    f=request.GET['fulltext']
    wordlist=f.split()

    worddict={}


    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    
    return render(request,'count.html', {"fulltext":f , "count":len(wordlist),'worddict':worddict.items() })

def about(request):
    return render(request,'about.html')


