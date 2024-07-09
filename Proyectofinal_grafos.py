#Importación de Dependencias
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

#Clase Usuario

def obtener_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            print("Formato incorrecto. Por favor, use el formato YYYY-MM-DD.")

class User:
        def __init__(self,nam,passw,mail,proAso,cod):
            self.name=nam
            self.password=passw
            self.email=mail
            self.proyectosAsociados= proAso
            self.codigo = cod


#Clase Proyecto

class Proyecto:
    def __init__(self,titulo, SD,DL,autores,desc):
        self.titulo = titulo
        self.StartDate = SD
        self.Deadline = DL
        self.autores=  autores
        self.description = desc
        self.siguiente = None


#Clase de Listas Simplemente Enlazadas

class ListaSE:

    #Constructor
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
                    

#Clase ListaProyectos, que hereda de la simplemente enlazada   
#                  
class ListaProyectos(ListaSE):

    #Agrega los elementos al inicio de la lista
    def AgregarInicio(self, proyect):
        nProyecto = proyect
        
        if self.cabeza is None:
            self.cabeza = nProyecto
            return
        else:
            nProyecto.siguiente = self.cabeza
            self.cabeza = nProyecto

    #Método de impresión propio        
    def ImprimirElementos(self):
        actualProyecto = self.cabeza
        while(actualProyecto):
            print("Título del proyecto: ", actualProyecto.titulo)
            print("Fecha de Inicio: ",actualProyecto.StartDate)
            print("Fecha Límite: ", actualProyecto.Deadline)
            print("Autores del proyecto:", ",".join(actualProyecto.autores))            
            print("Descripción: ", actualProyecto.description)
            print("------------------")
            actualProyecto = actualProyecto.siguiente

    #Devuelve los elementos de la forma []
    def getList(self):
        actualProyecto = self.cabeza
        projectList = []
        while(actualProyecto):
            projectList.append(actualProyecto)
            actualProyecto = actualProyecto.siguiente
        return projectList


#Clase generadora del grafo.

class GrafoUsuarios:

    #Constructor. la contraseña y el usuario de administración son de ejemplo para acceder a las funciones de admin

    def __init__ (self):
       
        self.adminUser = "1234"
        self.adminPassword = "xd"
        self.grafo = nx.Graph()

   

    #Funcion que se debe llamar cada vez que se haga una operación con los nodos, para actualizar los vértices en caso de que hayan nuevos proyectos
    def actualizarConecciones(self):

        for node, data in self.grafo.nodes(data=True):
            for proyecto in data["data"].proyectosAsociados.getList():
                if len(proyecto.autores) > 1:       #Si algún proyecto de la lista tiene más de un autor, entonces hay que crear la arista
                    for i in range(1, len(proyecto.autores)):
                        self.grafo.add_edge(data["data"].name, proyecto.autores[i])


#Clase principal
class Sistema:

    #Solamente trabaja con un atributo de grafo
    def __init__(self):

        self.centroDeDatos = GrafoUsuarios()


    #El menú de inicio
    def menu(self):    
        
        enElMenu = True

        
        while enElMenu:
            print("Bienvenido al Sistema de Manejo de Proyectos de Software. ¿Qué desea hacer?")
            print("1. Acceso como Administrador.")
            print("2. Acceso como Usuario")
            print("3. Salir")
            print("-----------------------")
            
            opcion = input("Ingrese su opción: ")
            if opcion == "1":
                codigo = input("Ingrese su código de administrador: ")
                password = input("Ingrese su contraseña de administrador: ")    

                if codigo == self.centroDeDatos.adminUser and password == self.centroDeDatos.adminPassword: #Compara con la contraseña y el usuario de prueba
                    print("Acceso Concedido")
                    self.menuAdmin()

                
                else: 
                    print("Usuario o Contraseña incorrectos. Intente de nuevo")



            
            elif opcion == "2":

                usuario = input("Ingrese su nombre de usuario: ")   #Compara con la contraseña y el usuario de prueba
                password = input("Ingrese su contraseña de usuario: ")    


                if self.centroDeDatos.grafo.has_node(usuario) and password == self.centroDeDatos.grafo.nodes[usuario]["data"].password: #Verifica que el usuario existe y luego mira la contraseña

                    print("Acceso Concedido")
                    self.menuUsuario(usuario)

                else:

                    print("Usuario o Contraseña incorrectos. Intente de nuevo")
                    print("-----------------------")
            
            elif opcion == "3":
                enElMenu = False

            else:
                print("Opción inválida. Intente nuevamente.")

    #Inicio de sesión y funciones de admin
    def menuAdmin(self):

        
        enElMenuAdmmin = True

        while enElMenuAdmmin:

            print("-----------------------") 
            print("Bienvenido al área de Administrador. ¿Qué desea hacer?")
            print("1. Consultar los usuarios actuales.")
            print("2. Agregar un usuario a la base de datos.")
            print("3. Buscar un usuario en la base de datos. ")
            print("4. Eliminar un usuario de la base de datos. ")
            print("5. Salir ")
            
            opcion = input("Ingrese su opción: ")


            if opcion == "1":

                if len(list(self.centroDeDatos.grafo.nodes)) > 0:       #Si hay al menos un nodo, dibuja el grafo 
                    """AQUÍ HAY QUE CAMBIAR LA FORMA DEL DIBUJO PARA TENER EN CUENTA SI ESTÁ ACTIVO O NO"""
                    nx.draw(self.centroDeDatos.grafo, with_labels=True) 
                    plt.show()
                    

                    print("Esta es la información requerida de los usuarios:")    #Imprime la información por consola también

                    for nodo, datos in self.centroDeDatos.grafo.nodes(data=True):
                        print("-----------------------") 
                        print("Usuario: ", datos["data"].name, "/", "Código: ", datos["data"].codigo, "/", "Email: ", datos["data"].email)
                        if datos["data"].proyectosAsociados != None:
                            print("Proyectos Asociados: ")
                            datos["data"].proyectosAsociados.ImprimirElementos()



                else:

                    print("El grafo está vacío, pruebe añadiendo nodos.")




            elif opcion == "2":

                print("Ingrese los datos a continuación: ")     #Pide los datos para añadir el nodo
                nombre= input("Nombre: ")
                password= input("Contraseña: ")
                email=input("Correo electrónico: ")
                codigo = input("Código/ID: ")

                self.centroDeDatos.grafo.add_node(nombre, data = User(nombre, password, email, ListaProyectos(), codigo))   #El label del nodo es el nombre, en data se guarda el objeto
                self.centroDeDatos.actualizarConecciones()  #Actualiza las aristas
                print("Agregado correctamente.")   

            elif opcion == "3":

                usuarioABuscar = input("Ingrese el nombre de usuario para buscar: ")

                if  self.centroDeDatos.grafo.has_node(usuarioABuscar):
                    print("Datos del usuario: ")
                    print("Usuario: ", self.centroDeDatos.grafo.nodes[usuarioABuscar]["data"].name, "/", "Código: ",    #Hay varios renglones pero solamente está imprimiendo el resultado de búsqueda
                          self.centroDeDatos.grafo.nodes[usuarioABuscar]["data"].codigo, "/", "Email: ", 
                          self.centroDeDatos.grafo.nodes[usuarioABuscar]["data"].email)
                    if self.centroDeDatos.grafo.nodes[usuarioABuscar]["data"].proyectosAsociados != None:       #Verifica si tiene proyectos.
                            print("Proyectos Asociados: ")
                            self.centroDeDatos.grafo.nodes[usuarioABuscar]["data"].proyectosAsociados.ImprimirElementos()
                
                else: print("No existe un nombre de usuario asociado a ese usuario.")

            elif opcion == "4":
                
                usuarioABuscar = input("Ingrese el nombre de usuario para eliminar.")       

                if  self.centroDeDatos.grafo.has_node(usuarioABuscar):      #Lo busca y lo elimina naturalmente
                
                    self.centroDeDatos.grafo.remove_node(usuarioABuscar)
                    print("El usuario se ha borrado correctamente ")
                    self.centroDeDatos.actualizarConecciones()      #Actualiza las aristas

                else: print("No existe un nombre de usuario asociado a ese usuario.")

            elif opcion == "5":
                enElMenuAdmmin = False

            else:
                print("Opción inválida, intente nuevamente")
                

            
    #Inicio de sesión y funciones de usuario
    def menuUsuario(self, usuario):

        enElMenuUsuario = True

        while enElMenuUsuario:

            print("-----------------------") 
            print("Bienvenido a su área personal. ¿Qué desea hacer?")
            print("1. Consultar sus Proyectos.")
            print("2. Añadir un proyecto.")
            print("3. Cambiar su contraseña. ")
            print("4. Salir. ")
            
            opcion = input("Ingrese su opción: ")


            if opcion == "1":
                                    
                if  self.centroDeDatos.grafo.nodes[usuario]["data"].proyectosAsociados.IndicarVacia():  #Si no tiene proyectos, no dibuja
                        print("[No tiene proyectos en este momento]")

                else:
                    colores = ["red","yellow","green"]
                    self.centroDeDatos.grafo.nodes[usuario]["data"].proyectosAsociados.ImprimirElementos()
                    grafoProyectosLocales = nx.DiGraph()    #Crea el grafo que va a dibujar
                    node_colors = {}
                    for proyecto in self.centroDeDatos.grafo.nodes[usuario]["data"].proyectosAsociados.getList():
                        dias = (proyecto.Deadline - proyecto.StartDate).days
                        print(dias)
                        if dias < 2:
                            color = colores[0]
                        elif 2 <= dias < 10:
                            color = colores[1]
                        else:
                            color = colores[2]
                        grafoProyectosLocales.add_edge(usuario, proyecto.titulo)
                        node_colors[proyecto.titulo] = color        #Añade los nodos a través de las aristas; si no existe el nodo, lo crea. Los nodos son nombres solamente
                    node_color_list = [node_colors[nodo] if nodo in node_colors else 'blue' for nodo in grafoProyectosLocales.nodes()]
                    self.centroDeDatos.actualizarConecciones()
                    nx.draw(grafoProyectosLocales, with_labels=True, node_color=node_color_list)
                    plt.show()

            elif opcion == "2":

                    print("Ingrese los datos a continuación: ")
                    titulo = input("Título: ")
                    fechaInicio=  obtener_fecha(f"Ingrese la fecha de inicio para {titulo} (YYYY-MM-DD): ")
                    fechaFin =obtener_fecha(f"Ingrese la fecha límite para {titulo} (YYYY-MM-DD): ")
                    autores = input("Autores (separados por coma): ").split(",")        #Recordar que los autores los va a guardar en una lista, por eso el split
                    descripcion = input("Descripción: ")
                    self.centroDeDatos.grafo.nodes[usuario]["data"].proyectosAsociados.AgregarInicio(Proyecto(titulo, fechaInicio, fechaFin, autores, descripcion)) #Añade el proyecto al inicio de la lista
                    print("Proyecto añadido satisfactoriamente. ")        

            elif opcion == "3":
                newPassword = input("Ingrese su nueva contraseña: ")
                self.centroDeDatos.grafo.nodes[usuario]["data"].password = newPassword      #Cambia la contraseña
                print("Contraseña cambiada correctamente")

            
            elif opcion == "4":
                enElMenuUsuario = False

            else: 
                print("Opción inválida, intente nuevamente")
                

##Función principal para iniciar el sistema

sistema = Sistema()

sistema.menu()