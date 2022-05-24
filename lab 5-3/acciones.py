from mrjob.job import MRJob
from mrjob.step import MRStep


class diasBajosAltos(MRJob):

    def mapper(self, _, line):    
        company, price,date = line.split(',')
        yield company, (price, date)

    def reducer(self, company, values):
            l = list(values)
            mini = 'Minimo: ',min(l)
            maxi = 'Maximo: ', max(l)
            yield company, (mini, maxi)

class AccionesEstables(MRJob):

    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, price

    def reducer(self, company, values):
        l=list(values)
        limite=len(l)
        i=1
        while(i<limite):
            if(l[i]>=l[i-1]):
                estado=1
            else:
                estado=0
                break
            i+=1
        if(estado==1):
            yield company, "Estable"

if __name__ == '__main__':
    print("")
    print("--------------------Precios maximos y minimos por acción: --------------------")
    print("")
    diasBajosAltos.run()
    print("")
    print("--------------------Acciones estables: --------------------")
    print("")
    AccionesEstables.run()
