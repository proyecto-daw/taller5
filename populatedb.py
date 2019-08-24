from core.models import Libro, Autor

autores = {}
with open("historico.txt") as f:
    next(f)  # Skip header
    for line in f:
        d = line.strip().split("|")
        l = Libro.objects.create(titulo=d[0], isbn=d[2])
        for autor in d[1].split("-"):
            if autor in autores:
                a = autores[autor]
            else:
                a, _ = Autor.objects.get_or_create(nombre=autor)
                autores[autor] = a
            l.authors.add(a)
