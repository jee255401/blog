from django.shortcuts import render
from .models import Bookmark
# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

def tabularBookmark(request):
    bookmarks = Bookmark.objects.all().order_by('id')
    return render(request, 'bookmark/tabular_list.html', {'bookmarks': bookmarks})

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark