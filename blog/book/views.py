from django.shortcuts import render

from book.models import Book


def book(request):
    '''
    Render the book page
    '''
    book = Book.objects.all()
    context = {'book':book}
    return render(request, 'book/book.html', context)

def bookCreate(request):
    pass