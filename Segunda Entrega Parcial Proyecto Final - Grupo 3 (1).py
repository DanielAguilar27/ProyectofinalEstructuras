class Proyecto:
    def __init__(self,SD,DL,nombre,desc):
        self.StartDate = SD
        self.Deadline = DL
        self.name= nombre
        self.description = desc
        self.siguiente = None


class User:
        def __init__(self,nam,passw,mail,proAso,cod):
            self.name=nam
            self.password=passw
            self.email=mail
            self.proyectosAsociados= proAso
            self.codigo = cod
            self.izquierda = None
            self.derecha = None


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
            print("Nombre del proyecto:", actualProyecto.name)
            print("Fecha de Inicio: ",actualProyecto.StartDate)
            print("Fecha Límite: ", actualProyecto.Deadline)            
            print("Descripción: ", actualProyecto.description)
            print("------------------")
            actualProyecto = actualProyecto.siguiente

class Arbol:
    # Funciones privadas
     
    def __init__(self, usuario):
        self.raiz = usuario

    def __agregar_recursivo(self, nodo, usuario):

        if nodo is None:
            self.raiz = usuario
        
        else: 

            if usuario.codigo < nodo.codigo:
                if nodo.izquierda is None:
                    nodo.izquierda = usuario
                else:
                    self.__agregar_recursivo(nodo.izquierda, usuario)
            else:
                if nodo.derecha is None:
                    nodo.derecha = usuario
                else:
                    self.__agregar_recursivo(nodo.derecha, usuario)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print("Usuario: ", nodo.name, "/" , "Codigo: ", nodo.codigo, "/","Email: ", nodo.email)
            if nodo.proyectosAsociados != None:
                print("Proyectos Asociados: ")
                nodo.proyectosAsociados.ImprimirElementos()
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:

            print(nodo.name)
            print(nodo.password)
            print(nodo.email)
            nodo.proyectosAsociados.ImprimirElementos()
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
        
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.name)
            print(nodo.password)
            print(nodo.email)
            nodo.proyectosAsociados.ImprimirElementos()

    def __buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if nodo.codigo == codigo:
            return nodo
        if codigo < nodo.codigo:
            return self.__buscar(nodo.izquierda, codigo)
        else:
            return self.__buscar(nodo.derecha, codigo)
    
    def codigoMinimo(self, nodo):
        actual = nodo

        
        while(actual.izquierda is not None):
            actual = actual.izquierda

        return actual

    

    def __eliminarUsuario(self, raiz, codigo):

        if raiz is None:
            return raiz
        
    
        if codigo < raiz.codigo:
            raiz.izquierda = self.__eliminarUsuario(raiz.izquierda, codigo)
        elif(codigo > raiz.codigo):
            raiz.derecha = self.__eliminarUsuario(raiz.derecha, codigo)
        else:
            
            if raiz.izquierda is None:
                if raiz is self.raiz:
                    self.raiz = raiz.derecha
                    return
                else:
                    temp = raiz.derecha
                    raiz = None
                    return temp

            elif raiz.derecha is None:
                if raiz is self.raiz:
                    self.raiz = raiz.izquierda
                    return
                else:
                    temp = raiz.izquierda
                    raiz = None
                    return temp

            
            temp = self.codigoMinimo(raiz.derecha)


            raiz.name = temp.name
            raiz.password = temp.password
            raiz.email = temp.email
            raiz.proyectosAsociados = temp.proyectosAsociados
            raiz.codigo = temp.codigo

            
            raiz.derecha = self.__eliminarUsuario(raiz.derecha, temp.codigo)

        return raiz

    # Funciones públicas

    def agregar(self, usuario):
        self.__agregar_recursivo(self.raiz, usuario)

    def inorden(self):
        print("Imprimiendo lista de usuarios en inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, codigo):
        return self.__buscar(self.raiz, codigo)
    
    def eliminarUsuario(self, codigo):
        return self.__eliminarUsuario(self.raiz, codigo)
    
    

"""
##Zona de Pruebas

usuario1 = User("Juan", "k123", "asomfo@gmail.com", None, 3 )
usuario2 = User("Paolo", "k123", "asomfo@gmail.com", None, 1 )
usuario3 = User("Manuel", "k123", "asomfo@gmail.com", None, 7 )
usuario4 = User("Juan Camilo", "k123", "asomfo@gmail.com", None, 9 )
usuario5 = User("Andres", "k123", "asomfo@gmail.com", None, 4 )

arbolPrueba = Arbol(usuario1)
arbolPrueba.agregar(usuario2)
arbolPrueba.agregar(usuario3)
arbolPrueba.agregar(usuario4)
arbolPrueba.agregar(usuario5)
arbolPrueba.inorden()

print(arbolPrueba.buscar(9).name)

arbolPrueba.eliminarUsuario(arbolPrueba.raiz, 7)
arbolPrueba.inorden()
arbolPrueba.eliminarUsuario(arbolPrueba.raiz, 3)
print("--------")
arbolPrueba.inorden()
arbolPrueba.eliminarUsuario(arbolPrueba.raiz, 1)
print("--------")
arbolPrueba.inorden()
arbolPrueba.eliminarUsuario(arbolPrueba.raiz, 4)
print("--------")
arbolPrueba.inorden()
"""

class Sistema():
    def menu():    
        print("Bienvenido al Sistema de Manejo de Proyectos de Software. ¿Qué desea hacer?")
        print("1. Consultar los usuarios actuales.")
        print("2. Agregar un usuario a la base de datos.")
        print("3. Buscar un usuario en la base de datos. ")
        print("4. Eliminar un usuario de la base de datos. ")
        print("5. Consultar/Añadir sus proyectos. (Acceso personal)")
        print("6. Cambiar su contraseña. (Acceso personal)")
        print("7. Salir ")
        enElMenu = True

        centroDeDatos = Arbol(None)

        while enElMenu:
            print("-----------------------")
            
            opcion = input("Ingrese su opción: ")
            if opcion == "1":
                if centroDeDatos.raiz is None:
                    print("El árbol de datos se encuentra vacío. Intente agregando usuarios nuevos.")

                else:
                    centroDeDatos.inorden()

                print("-----------------------")       
            
            
            elif opcion == "2":
                print("Ingrese los datos a continuación: ")
                nombre= input("Nombre: ")
                password= input("Contraseña: ")
                email=input("Correo electrónico: ")
                codigo = int(input("Código/ID (7 Cifras): "))
                if len(str(codigo)) == 7:
                    centroDeDatos.agregar(User(nombre, password, email, ListaProyectos(), codigo)) 
                    print("Agregado correctamente.")                   
                else:
                    print("Código incorrecto. Intente de nuevo.")

                print("-----------------------")   

            elif opcion == "3":
                codigoABuscar = int(input("Ingrese el código del usuario: "))
                
                busqueda = centroDeDatos.buscar(codigoABuscar)

                if busqueda is None:
                    print("No existe ningún usuario registrado con ese código. ")

                else:
                    print("Resultado de búsqueda: ")
                    print("Usuario: ", busqueda.name)
                    print("Email: ", busqueda.email)
                    if  busqueda.proyectosAsociados.IndicarVacia():
                        print("El usuario no tiene proyectos. ")

                    else:
                        print("Proyectos del usuario: ")
                        busqueda.proyectosAsociados.ImprimirElementos()

                print("-----------------------")               
                

            elif opcion == "4":
                codigo = int(input("Ingrese el código del usuario a eliminar: "))

                busqueda = centroDeDatos.buscar(codigo)

                if busqueda is None:
                    print("No existe ningún usuario registrado con ese código. ")


                else:
                    centroDeDatos.eliminarUsuario(codigo)
                    print("El usuario se ha borrado satisfactoriamente. ")
            
            elif opcion == "5":
                codigo = int(input("Ingrese su código de usuario: "))
                password = input("Ingrese su contraseña de usuario: ")

                busqueda = centroDeDatos.buscar(codigo)

                if busqueda is not None and busqueda.password == password:
                    print("Sus proyectos son: ")

                    if  busqueda.proyectosAsociados.IndicarVacia():
                        print("[No tiene proyectos en este momento]")

                    else:
                        busqueda.proyectosAsociados.ImprimirElementos()
                    
                    add = input("Desea añadir algún proyecto? (S/N)")

                    if add == "S":
                        print("Ingrese los datos a continuación: ")
                        nombre= input("Nombre: ")
                        fechaInicio= input("Fecha de Inicio: ")
                        fechaFin =input("Fecha de Fin: ")
                        descripcion = input("Descripción: ")
                        busqueda.proyectosAsociados.AgregarInicio(Proyecto(fechaInicio, fechaFin, nombre, descripcion))
                        print("Proyecto añadido satisfactoriamente. ")

                    else:
                        print("Sesión finalizada") 

                else:

                    print("Código o contraseña incorrectas. ")               
            
            elif opcion == "6":
                codigo = int(input("Ingrese su código de usuario: "))
                password = input("Ingrese su contraseña de usuario: ")

                busqueda = centroDeDatos.buscar(codigo)

                if busqueda is not None and busqueda.password == password:
                    newPassword = input("Ingrese su nueva contraseña: ")
                    busqueda.password = newPassword
                    print("Contraseña cambiada con éxito. ")
                    

                else:
                    print("Código o contraseña incorrectas. ")


            elif opcion == "7":
                enElMenu = False

            else:
                print("Opción inválida. Intente nuevamente.")

##Función principal 

Sistema.menu()
