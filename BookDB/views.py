# coding=gbk
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book, Author
from django.template import Context
from django.http import HttpResponseRedirect
# Create your views here.
#show, book_details, add, renew,seachAuthor
def show(request):
    if "seach_author" in request.GET:
        books=seach(request)
    elif "new_book" in request.GET:
        return HttpResponseRedirect("/add/")
    else:
        books=Book.objects.all()
    c = Context({"books":books})
    return render_to_response("shumu.html", c)
def delete(request):
    if "d_id" in request.GET:
        Book.objects.filter(ISBN=request.GET["d_id"]).delete()
        books=books=Book.objects.all()
        c = Context({"books":books})
        return render_to_response("shumu.html", c)

def book_details(request):
    if "book_ISBN" in request.GET:
        book = Book.objects.get(ISBN=request.GET["book_ISBN"])
        #book = books=Book.objects.all()[0]
        c = Context({"book":book})
        return render_to_response("book_details.html", c)
    if "seach_author" in request.GET:
        books=seach(request)
        c = Context({"books":books})
        
        return render_to_response("shumu.html", c)
        
def seach_form(request):
    return render_to_response('seach_form.htlm')
def seach(request):
    if 'q'in request.GET and request.GET['q']:
        q=request.GET['q']
        books=Book.objects.filter(Authorname__icontains=q)
        return render_to_response('seach_result.html',
                                  {'books':books,'query':q})
                                  
    else:
         return HttpResponse('please submit a seach term')


# Create your views here.
