from django.shortcuts import render
from util import get_entry
from . import util


def error_404_view(request, exception):
    return render(request, '404.html')


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "entry": get_entry(title)
    })
