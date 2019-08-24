import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://root:root@cluster0-pmsyg.mongodb.net/test?retryWrites=true&w=majority")
libros = client.testdb.libros

with open("historico.txt") as f:
    next(f)  # Skip header
    for line in f:
        d = line.strip().split("|")
        libros.insert_one({"titulo": d[0], "autores": d[1], "isbn": d[2], "calificacion_promedio": float(d[3])})
