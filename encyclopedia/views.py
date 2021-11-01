from django.shortcuts import render
from . import util


def error_404_view(request, exception):
    return render(request, 'encyclopedia/404.html')


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/entry_page.html", {
            "title": title,
            "entry": util.get_entry(title)
        })
    else:
        return render(request, 'encyclopedia/404.html', status=404)
