from django.shortcuts import render, redirect
from . import util
import markdown2
import markdown
import random


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
            "entry": markdown.markdown(content)
        })
    else:
        return render(request, 'encyclopedia/404.html', status=404)


def search_results(request, search_query):
    search_results_list = []
    for entry in util.list_entries():
        if search_query in entry:
            search_results_list.append(entry)
    return render(request, "encyclopedia/search_results.html", {
        "search_results_list": search_results_list
    })


def search(request):
    search_query = request.POST['search_query']
    if search_query in util.list_entries():
        return redirect('entry_page', title=search_query)
    for entry in util.list_entries():
        if search_query in entry:
            return redirect('search_results', search_query=search_query)
    else:
        return redirect('entry_page', title=search_query)


def new_page(request):
    return render(request, "encyclopedia/new_page.html")


def save_page(request):
    title = request.POST['title']
    content = request.POST['content']
    if title in util.list_entries():
        return render(request, "encyclopedia/new_page.html", {
            "message": "Title already exist. Try another.", "title": title, "content": content})
    elif title == "" or content == "":
        return render(request, "encyclopedia/new_page.html", {
            "message": "Please fill all empty fields."})
    else:
        util.save_entry(title, content)
        return redirect('entry_page', title=title)


def edit_page(request, title):
    return render(request, "encyclopedia/edit_page.html", {
        "content": util.get_entry(title),
        "title": title
    })


def random_page(request):
    return redirect('entry_page', title=random.choice(util.list_entries()))
