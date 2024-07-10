#Por hacer:
#Imprimir en pantalla los elementos de la lista
#Agregar un elemento (Solo se agregaran por el inicio de la lista)
#Buscar un elemento en la lista
#Un método que sea propio del problema que se está tratando (Pueden seleccionar y definir cualquiera)
from operator import truediv
from xmlrpc.client import boolean


class Proyecto:
    def __init__(self,SD,DL,user,desc):
        self.StartDate = SD
        self.Deadline = DL
        self.name= user
        self.description = desc
        self.siguiente = None
        
class User:
    def __init__(self,nam,passw,mail,proAso):
        self.name=nam
        self.password=passw
        self.email=mail
        self.proyectosAsociados= proAso
        self.siguiente = None
        
    def PrintInfo(self):
        return 'Nombre:'+ self.name + 'Contraseña:' + self.password + 'Correo:' + self.email
        
        
class ListaSE:
    def __init__(self):
        self.cabeza = None
        
    def IndicarVacia(self):
        if self.cabeza is None:
            return True
        else:
            return False
        
    def ContarElementos(self):
        actualNodo = self.cabeza
        contador = 0
        while actualNodo != None:
            contador +=1
            actualNodo = actualNodo.siguiente
        return contador
    
    def ImprimirElementos(self):
        pass
        
    def BuscarNombre(self,nomb):
        nActual = self.cabeza #valor observado
        buscando = True
        while buscando:
            if nActual.name == nomb: #si el nodo observado tiene valor igual al vab
                buscando = False
                return True
            else:
                if nActual.siguiente is None: #si el valor no es igual, se revisa si el nodo apunt a un nodo distinto
                    buscando = False
                    return False
                else:
                    nActual = nActual.siguiente # si sí tiene nodo siguiente, se observa el próximo nodo
        
    def AgregarInicio(self):
            pass
            
class ListaUsuarios(ListaSE):
    def AgregarInicio(self,usuario):
        nUser = usuario
        
        if self.cabeza is None:
            self.cabeza = nUser
            return
        else:
            nUser.siguiente = self.cabeza
            self.cabeza = nUser
            
    def ImprimirElementos(self):
        actualUsuario = self.cabeza
        while(actualUsuario):
            print(actualUsuario.name)
            print(actualUsuario.password)
            print(actualUsuario.email)
            actualUsuario.proyectosAsociados.ImprimirElementos()
            actualUsuario = actualUsuario.siguiente
            
    def CambiarContraseña(self,user,oPass,nPass):
        nActual = self.cabeza #valor observado
        buscando = True
        while buscando:
            if nActual.name == user: #si el nodo observado tiene el nombre deseado
                buscando = False
                
                if oPass == nActual.password:
                    nActual.password = nPass
            else:
                if nActual.siguiente is None: #si el valor no es igual, se revisa si el nodo apunta a un nodo distinto
                    buscando = False
                    print('No hay usuario con ese nombre')
                else:
                    nActual = nActual.siguiente # si sí tiene nodo siguiente, se observa el próximo nodo
    
            
class ListaProyectos(ListaSE):
    def AgregarInicio(self, proyect):
        nProyecto = proyect
        
        if self.cabeza is None:
            self.cabeza = nProyecto
            return
        else:
            nProyecto.siguiente = self.cabeza
            self.cabeza = nProyecto
            
    def ImprimirElementos(self):
        actualProyecto = self.cabeza
        while(actualProyecto):
            print(actualProyecto.StartDate)
            print(actualProyecto.Deadline)
            print(actualProyecto.name)
            print(actualProyecto.description)
            actualProyecto = actualProyecto.siguiente


# Zone de pruebas

Lista1 = ListaUsuarios() # Se crea Lista de usuarios
Lista2 = ListaProyectos() # Se crea Lista de proyectos personal para el primer usuario
Lista3 = ListaProyectos() # Se crea Lista de proyectos personal para el segundo usuario

pepega = Proyecto('01/02/2005','02/03/2006','pepo','Proyecto chévere') # Se crea un proyecto por añadir a la primera lista
Lista2.AgregarInicio(pepega) # Se añade el proyecto a la lista personal del primer usuario

hababa = Proyecto('02/03/2006','03/04/2007','pepa','Proyecto mamón') # Se crea un proyecto por añadir a la segunda lista
Lista3.AgregarInicio(hababa) # Se añade el proyecto a la lista personal del segundo usuario

pepo = User('Juan','abc123','Juan123abc@hotmail.com',Lista2) # Se crea el primer usuario

jorge= User('José','abc124','Jamón123abc@hotmail.com',Lista3) # Se crea el segundo usuario

Lista1.AgregarInicio(pepo) # Se añade el primer usuario a la lista
Lista1.AgregarInicio(jorge) # Se añade el segundo usuario a la lista

Lista1.ImprimirElementos() # Se imprimen los elementos de la lista de ususarios

Lista1.CambiarContraseña('Juan','abc123', 'cba321') # Se desea cambiar la contraseña del usuario de nombre 'Juan' a 'cba321'

Lista1.ImprimirElementos() # Se vuelven a imprimir los elementos para comprobar que el cambio se hizo efectivamente

#      
