from django.shortcuts import render, redirect
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


def search_results(request):
    return render(request, "encyclopedia/search_results.html")


def search(request):
    search_query = request.POST['search_query']
    if search_query in util.list_entries():
        return redirect('entry_page', title=search_query)
    for entry in util.list_entries():
        if search_query in entry:
            return redirect('search_results')
