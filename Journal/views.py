from django.shortcuts import render
from .models import Articles,Releases,Authors,Genres
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'index.html', context)

def our_authors(request):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'our_authors.html', context)

def archive(request):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'archive.html', context)

def glvrd(request):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'glvrd.html', context)

def auth(request):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'auth.html', context)

def GetArticle(request, id):
    return render(request, 'article.html', {'data': {
        'article': Articles.objects.filter(id=id)[0],
    }})

def GetAuthor(request, id):
    articles = Articles.objects.all()
    releases = Releases.objects.all()
    authors = Authors.objects.all()
    genres = Genres.objects.all()
    context = {
        'articles': articles,
        'releases': releases,
        'authors': authors,
        'genres': genres,
        'data': {
            'author': Authors.objects.filter(id=id)[0],
        }
    }
    return render(request, 'authorz.html', context)

def relez(request, id):
    release = Releases.objects.get(id=id)
    if request.method == "POST":
        release.actual = request.POST.get("name")
        release.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "releases.html", {"release": release})

def create(request):
    if request.method == "POST":
        rel = Releases()
        rel.quantity= request.POST.get("number_rel")
        rel.actual=request.POST.get("actual_rel")
        rel.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "new.html")

def createauthor(request):
    if request.method == "POST":
        aut = Authors()
        aut.name = request.POST.get("name")
        aut.info = request.POST.get("info")
        aut.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "createnewauthor.html")

def newarticle(request, id):
    genres = Genres.objects.all()
    author = Authors.objects.get(id=id)
    releases = Releases.objects.all()
    context = {
        'genres': genres,
        'releases': releases,
    }
    if request.method == "POST":
        article = Articles()
        article.name = request.POST.get("name")
        article.text = request.POST.get("text")
        article.genre_id = request.POST.get("genre")
        article.author = author
        article.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "newarticle.html",context)