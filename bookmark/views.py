from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

def tabularBookmark(request):
    bookmarks = Bookmark.objects.all().order_by('id')
    return render(request, 'bookmark/tabular_list.html', {'bookmarks': bookmarks})