from mrjob.job import MRJob

class salarioPromedioSector(MRJob):

    def mapper(self, _, line):    
        idemp, sector,salary,year = line.split(',')
        yield sector, int(salary)

    def reducer(self, sector, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield sector, avg

class salarioPromedioEmpleado(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, int(salary)

    def reducer(self, idemp, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield idemp, avg

class sectorEmpleado(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, values):
        l = list(values)
        ln = 'Numero de sectores: ',len(l)
        yield idemp, ln

if __name__ == '__main__':
    print("")
    print("--------------------Salario Promedio por Sector: --------------------")
    print("")
    salarioPromedioSector.run()
    print("")
    print("--------------------Salario Promedio por Empleado: --------------------")
    print("")
    salarioPromedioEmpleado.run()
    print("")
    print("--------------------Sectores por Empleado: --------------------")
    print("")
    sectorEmpleado.run()