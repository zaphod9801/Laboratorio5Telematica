from mrjob.job import MRJob
from mrjob.step import MRStep

class PeliculasPorUsuario(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield user,(movie,rating)

    def reducer(self, user, values):
        l = list(values)
        vistas=len(l)
        i=0
        suma=0

        while(i<vistas):
            suma+=int(l[i][1])
            i+=1
        
        ratingPromedio=suma/vistas

        yield user, (vistas,ratingPromedio)


class FechaMax(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, movie

    def reducer(self, date, values):
        l=list(values)
        peliculas=len(l)
        
        yield None, (date, peliculas)

    def reducer2(self, _, values):
        l=list(values)
        limite=len(l)
        
        peliculas=l[0][1]
        i=0
        while(i<limite):
            if((l[i][1]>=peliculas)):
                peliculas=l[i][1]
                fechaMaxima=l[i][0]
            i=i+1

        yield "Fecha: ",fechaMaxima

    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]

class FechaMin(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, movie

    def reducer(self, date, values):
        l=list(values)
        peliculas=len(l)
        
        yield None, (date, peliculas)

    def reducer2(self, _, values):
        l=list(values)
        limite=len(l)
        
        peliculas=l[0][1]
        i=0
        while(i<limite):
            if((l[i][1]<=peliculas)):
                peliculas=l[i][1]
                fechaMinima=l[i][0]
            i=i+1

        yield "Fecha: ",fechaMinima

    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]

class UsuariosPorPelicula(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield movie,(user,rating)

    def reducer(self, movie, values):
        l = list(values)
        usuarios=len(l)
        i=0
        suma=0

        while(i<usuarios):
            suma+=int(l[i][1])
            i+=1
        
        ratingPromedio=suma/usuarios

        yield movie, (usuarios,ratingPromedio)

class MinRating(MRJob):
    
    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date,int(rating)

    def reducer(self, movie, values):
        l = list(values)
        Promedio=sum(l)/len(l)        
        yield None, (movie,Promedio)

    def reducer2(self, _, values):
        l=list(values)
        limite=len(l)
        minPromedio=l[0][1]
        i=0

        while(i<limite):
            if((l[i][1]<=minPromedio)):
                minPromedio=l[i][1]
                fecha=l[i][0]
            i+=1

        yield "Rating: " , (fecha,minPromedio)


    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]


class MaxRating(MRJob):
    
    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date,int(rating)

    def reducer(self, movie, values):
        l = list(values)
        Promedio=sum(l)/len(l)        
        yield None, (movie,Promedio)

    def reducer2(self, _, values):
        l=list(values)
        limite=len(l)
        maxPromedio=l[0][1]
        i=0
        
        while(i<limite):
            if((l[i][1]>=maxPromedio)):
                maxPromedio=l[i][1]
                fecha=l[i][0]
            i+=1

        yield "Rating: " , (fecha,maxPromedio)


    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]


if __name__ == '__main__':
    print("")
    print("--------------------Peliculas por usuario mas rating promedio: --------------------")
    print("")
    PeliculasPorUsuario.run()
    print("")
    print("--------------------Fecha con mas peliculas: --------------------")
    print("")
    FechaMax.run()
    print("")
    print("--------------------Fecha con menos peliculas: --------------------")
    print("")
    FechaMin.run()
    print("")
    print("--------------------Usuarios por pelicula mas rating promedio: --------------------")
    print("")
    UsuariosPorPelicula.run()
    print("")
    print("--------------------Fecha del rating promedio más bajo: --------------------")
    print("")
    MinRating.run()
    print("")
    print("--------------------Fecha del rating promedio más alto: --------------------")
    print("")
    MaxRating.run()