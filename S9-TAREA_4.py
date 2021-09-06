class Empresa:
    def __init__(self,id=1,empresa="Extermix",ruc="0999959844",telf="064684165",dir="nice to me too",nomEmp='',empleado='',departamento='ciecias'):
        self.__id=id
        self.nombreEmpresa=empresa
        self.ruc=ruc
        self.telefono=telf
        self.direccion=dir
        self.nombreEmpleado=nomEmp
        self.empleado=empleado
        self.departamento=departamento

    @property
    def id(self):
        return self.__id

    def mostrarEmpresa(self):
        print('Id:[{}]   Empresa:{:15} Ruc:{:15} Telefono:{:15} Direccion:{}'.format(self.__id,self.nombreEmpresa,self.ruc,self.telefono,self.direccion))


class Departamento:
    def __init__(self, id=1, empleado='', descripcion=''):
        self.__id = id
        self.empleado = empleado
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def mostrarDepartamento(self):
        print('Id:[{}]   Departamento: {:20} Empleado: {:12}'.format(self.__id, self.descripcion, self.empleado))


class Empleado:
    def __init__(self,id=1,nombre='',cedula='',ingreso='',sueldo=0,depa=''):
        self.__id=id
        self.nombre=nombre
        self.cedula=cedula
        self.FechaIngreso=ingreso
        self.sueldo=sueldo
        self.departamento=depa

    @property
    def id(self):
        return self.__id

    def valorHora(self):
        return self.sueldo/240

    def mostrarEmpleado(self):
        print('Id:[{}]   Nombre: {:10} Cedula: {:10} Fecha de Ingreso: {:10} Sueldo: ${}'.format(self.__id,self.nombre,self.cedula,self.FechaIngreso,self.sueldo))


class Administrativo(Empleado):
    def __init__(self,nom,ced,ingre,suel,departamento,comision=True):
        super().__init__(nom,ced,ingre,suel,departamento)
        self.comision=comision

    def mostrarAdministrativo(self):
        print('Id:[{}]   Administrativo: {:10} Cedula: {:10} Fecha de Ingreso: {:10} Sueldo: ${}'.format(self.__id,self.nombre,self.cedula,self.FechaIngreso,self.sueldo))
        print("Comision: {}".format(self.comision))

    def valorHora(self):
        return super().valorHora()

class Obrero(Empleado):
    def __init__(self,nom,ced,ingre,suel,sindicato=True,contrColect=True):
        super().__init__(nom,ced,ingre,suel)
        self.__sindicato=sindicato
        self.__contratoColectivo=contrColect



class Prestamo:
    def __init__(self,id=1,fecha='',valor='',numPag=0,cuota=0,empleado='',saldo=0,estado=True):
        self.__id=id
        self.empledo=empleado
        self.fecha=fecha
        self.valor=valor
        self.numeroPagos=numPag
        self.cuota=cuota
        self.saldo=saldo
        self.estado=estado

    @property
    def id(self):
        return self.__id

    def mostrarPrestamo(self):
        print('Id:[{}]  Fecha: {:19} Valor: {:12} Numero de Pagina: {:12} Cuota: {:12} Saldo: {:12} Estado: {}'.format(self.__id,self.fecha,self.valor,self.numeroPaginas,self.cuota,self.saldo,self.estado))
       
class Sobretiempo:
    def __init__(self,id=1,horasRecargo=0,horasExtraordinarias=0,empleado='',fecha='',estado=True):
        self.__id=id
        self.horasRecargo=horasRecargo
        self.horasExtraordinaias=horasExtraordinarias
        self.empleado=empleado
        self.fecha=fecha
        self.estado=estado

    @property
    def id(self):
        return self.__id

    def Sobretiempo(self):
        return round(self.empleado.valorHora()+(self.horasRecargo*1.5+self.horasExtraordinaias*2),2)

    def mostrarSobretiempo(self):
        print('Id: {:15} Fecha: {:19} Empleado: {:12} Horas de Recargo: {:12} Horas Extraordinarias: {:12} Estado: {}'.format(self.__id,self.fecha,self.empleado,self.horasRecargo,self.horasExtraordinaias,self.estado))
      
class Deducciones:
    def __init__(self,iess=0,comision=0,antiguedad=0):
        self.__iess=iess
        self.__comision=comision
        self.__antiguedad=antiguedad

    def Iess(self):
        return round(self.__iess/100/4)

    def Comision(self):
        return round(self.__comision/100,2)

    def Antiguedad(self):
        return round(self.__antiguedad/100,2)

    def mostrarDeducciones(self):
        print('Iess: {:15} Comision: {:19} Antiguedad: {}'.format(self.iess,self.comision,self.antiguedad))

class Nomina:

    def __init__(self,id=1,empleado='',fecha='',sueldo=0,sobretiempo='',comision=0,antiguedad=0,sothing=0,iess=0,prestamo='',totalDescuento=0,liquidoRecidido=0):
        self.__id=id
        self.empleado=empleado
        self.fecha=fecha
        self.sueldo=sueldo
        self.sobretiempo=sobretiempo
        self.comision=comision
        self.antiguedad=antiguedad
        self.shoting=sothing
        self.iess=iess
        self.prestamo=prestamo
        self.totalDescuento=totalDescuento
        self.liquidoRecidido=liquidoRecidido

    @property
    def id(self):
        return self.__id

    def mostrarNomina(self):
        print('Id: {:15} Fecha: {:19} Sueldo: {:12} Sobretiempo: {:12} Comision: {:12} Antiguedad: {:12} Sothing: {:12} IESS: {:12} Prestamo: {:12} Total de descuento: {:12} Liquido a Recibir: {}'.format(self.__id,self.fecha,self.sueldo,self.sobretiempo,self.comision,self.antiguedad,self.shoting,self.iess,self.prestamo,self.totalDescuento,self.liquidoRecidido))
      

empresa=Empresa()
empleado=Empleado(1,'ronny','0665666','2015',550)




empresa.mostrarEmpresa()
empleado.mostrarEmpleado()

#nom=Nomina('ronny','2019',200,'ccc',12,5,10,2,'tt',5,1000)
#nom.mostrarNomina()

#Emp=Empresa()
#Emp.mostrarEmpresa()
