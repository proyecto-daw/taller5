from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.models import Autor, Libro, Rating


def list_books(request):
    return render(request, "list_books.html")


@login_required
def user_profile(request):
    return render(request, "profile.html", {"ratings": request.user.ratings})


def book_detail(request, pk):
    l = get_object_or_404(Libro, pk=pk)
    calificable = request.user.is_authenticated and Rating.objects.filter(libro=l, user=request.user).count() == 0
    return render(request, "book.html", {"pk": pk, "calif_hist": _get_calif_hist(l), "calificable": calificable})


def list_authors(request):
    return render(request, "list_authors.html")


def _get_calif_hist(libro):
    import pymongo

    print(f"Getting data for book {libro.titulo}")
    client = pymongo.MongoClient(
        "mongodb://root:root@cluster0-shard-00-00-pmsyg.mongodb.net:27017,cluster0-shard-00-01-pmsyg.mongodb.net:27017,cluster0-shard-00-02-pmsyg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    libros = client.testdb.libros
    return libros.find_one({"isbn": libro.isbn})["calificacion_promedio"]


def author_detail(request, pk):
    author = get_object_or_404(Autor, pk=pk)
    books = list(author.libros.all())
    califs = [_get_calif_hist(libro) for libro in books]
    ordenados = [list(x) for x in zip(*sorted(zip(califs, books), key=lambda pair: pair[0]))]
    print(zip(reversed(ordenados[0]), reversed(ordenados[1])))
    # ordenados = [x for x in sorted(zip(books, califs))]
    return render(request, "author.html",
                  {"autor": author, "books": zip(reversed(ordenados[0]), reversed(ordenados[1]))})
