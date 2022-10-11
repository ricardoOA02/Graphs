import subway 
import sys
class Nodo():

    def __init__(self, nombre): #Constructor de la clase Nodo
        self.nombre = nombre
        self.vecinos = []
        self.color = 'blanco'
        self.distancia = -1
        self.padre = None
        self.d = 0
        self.f = 0
        self.pred = None

    def agregarVecino(self, nodo):
        for vec in self.vecinos: #Recorre la lista de los vecinos
            if vec == nodo: # Si ya existe el vecino envia un mensaje de error
                print("Ya existe el nodo como vecino")
                return
        self.vecinos.append(nodo)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre 

    
class Grafo():
    
    def __init__(self): #Constructor de la clase Grafo
        self.vertices = {}
        print()

    def agregarVertice(self, nombreNodo):
        for i in self.vertices.values(): #Recorre el diccionario de vertices
            if i.nombre == nombreNodo: #Si encuentra un nodo con el mismo nombre no lo agrega
                print("El nodo",nombreNodo,"ya existe")
                return
            
        nuevoNodo = Nodo(nombreNodo) #Crea el nodo con el nombre que recibe la funcion
        self.vertices[nombreNodo] = nuevoNodo #Agrega el nodo al diccionario de vertices
        print("Nodo:",nombreNodo,",agregado") 

    def agregarArista(self, nombreNodo1, nombreNodo2):
        if nombreNodo1 in self.vertices: #Comprueba que el nodo exista en el diccionario vertices
            nodo1 = self.vertices[nombreNodo1] #Asigna el nodo a una variable
            for i in nodo1.vecinos: #Recorre los vecinos del nodo1
                if i.nombre == nombreNodo2: #Si entre los vecinos del nodo 1 esta el nodo 2 envia mensaje de error
                    print("Ya existe el arista entre los nodos {} y {}".format(nombreNodo1, nombreNodo2))
                    return
        else:
            print("Error no existe el nodo con nombre "+nombreNodo1) #Si no existe el nodo en el diccionario envia mensaje de error
            return
        
        if nombreNodo2 in self.vertices: #Comprueba que el nodo exista en el diccionario vertices
            nodo2 = self.vertices[nombreNodo2] #Asigna el nodo a una variable
            for i in nodo2.vecinos: #Recorre los vecinos del nodo2
                if i.nombre == nombreNodo1: #Si entre los vecinos del nodo 2 esta el nodo 1 envia mensaje de error
                    print("Ya existe el arista entre los nodos {} y {}".format(nombreNodo2, nombreNodo1))
                    return
        else:
            print("Error no existe el nodo con nombre "+nombreNodo2) #Si no existe el nodo en el diccionario envia mensaje de error
            return

        print("Arista {} - {} agregado".format(nombreNodo1, nombreNodo2))
        nodo1.agregarVecino(nodo2) #Llama a la funcion agregar vecino con ambos nodos para que ambos se agreguen como vecinos
        nodo2.agregarVecino(nodo1)

    def BreadthFirstSearch(self, nombreNodoInicial):
        for u in self.vertices.values(): #Establece los valores iniciales del nodo
            u.color = 'blanco' 
            u.distancia = -1
            u.padre = None

        self.vertices[nombreNodoInicial].color = 'gris' #Se selecciona el nodo inicial asignandole color gros
        self.vertices[nombreNodoInicial].distancia = 0 #distancia 0
        self.vertices[nombreNodoInicial].padre = None # y padre vacio

        Q = []
        Q.append(self.vertices[nombreNodoInicial]) #Se crea la cola y se agrega el nodo inicial

        while len(Q) > 0: #Mientras la cola tenga datos se realizara el while
            u = Q.pop(0) #Se saca el primer elemento que se agrego a la cola 
            for v in u.vecinos: #Se itera sobre los vecinos de el elemento que se saco de la cola
                if v.color == 'blanco': #Si el vecino no ha sido explorado:
                    v.color = 'gris' #Se cambia su color a gris
                    v.distancia = u.distancia + 1 #Su distancua sera la de su padre mas uno
                    v.padre = u #Se establece como su padre al elemento que se saco de la cola
                    Q.append(v) #Se agrega el nodo ya que se han establecido sus datos 
            u.color = 'negro' #El nodo que se saco de la cola se marca como explorado

    def DepthFirstSearch_EC(self, nombreV):
        vert = self.vertices[nombreV] #Obtenemos el vertice final
        global tiempo 
        tiempo = 0
        for u in self.vertices.values(): #Establecemos los datos de todos los nodos
            u.color = 'blanco' #Color blanco
            u.pred = None #Sin predecesores
            u.d = 0 #Tiempo inicial
            u.f = 0 #Tiempo final
        
        for u in vert.vecinos: #Se exploraon los vecinos del vertice obtenido
            if u.color == 'blanco': #Si los vecinos tienen color blanco se llama a la funcion DFS_visitar
                self.DFS_Visitar_EC(u)

    def DFS_Visitar_EC(self, u):
        
        global tiempo
        tiempo += 1 
        u.d = tiempo
        u.color = 'gris' #Se establece el color en gris

        for v in u.vecinos: #Se exploran los vecinos del vertice que se le paso a la funcion 
            if v.color == 'blanco': #Si los vecinos no han sido explorados:
                v.pred = u #Se establece su predecesor 
                self.DFS_Visitar_EC(v) #Se llama recursicvamente a la funcion DFS_visitar
        u.color = 'negro' #Ya explorados sus vecinos se establece el color del vertice en negro
        tiempo += 1 
        u.f = tiempo #Se establece el tiempo final

    def EncontrarCaminoDFS(self, nombreVerticeInicial, nombreVerticeFinal):
        self.DepthFirstSearch_EC(nombreVerticeFinal) #Se lla a la funcion DepthFirstSearch con el vertice final

        camino = [nombreVerticeInicial] #Se crea el arreglo para guardar las estaciones 
        for u in range(self.vertices[nombreVerticeInicial].d): #Itera sobre los predecesores del vertice inicial
            aux = self.vertices[nombreVerticeInicial].pred #Guarda al predecesor en una variable auxiliar
            if(aux == nombreVerticeFinal or aux == None): #Si se llega al la estacion final
                camino.append(nombreVerticeFinal) 
                cont = 0
                for i in range(len(camino)): #Se imprime la ruta 
                    print(camino[i], sep=' ', end=' ', file=sys.stdout, flush=False) # Modificar la funcion print para que no haga
                    cont += 1                                                                  # salto de linea automatico
                    if cont < len(camino):
                        print("->", sep=' ', end=' ', file=sys.stdout, flush=False)
                return #Termina la funcion
            camino.append(str(aux)) #Si no se entra al if se agrega la estacion
            nombreVerticeInicial = str(aux) #Se cambia el vertice para explorar el siguiente predecesor 
            
        

    def EncontrarCaminoBFS(self, nombreVerticeInicial, nombreVerticeFinal):
        self.BreadthFirstSearch(nombreVerticeInicial) #Se llama a la funcion Breadth First Search

        camino_invertido = [nombreVerticeFinal] #Se crea el arreglo para guardar el camino
        for u in range(self.vertices[nombreVerticeFinal].distancia): #Se itera sobre los padres del vertice final
            aux = self.vertices[nombreVerticeFinal].padre.nombre #Se guarda el nombre del padre en una variable auxiliar
            camino_invertido.append(aux) #Se agrega el nombre al arreglo
            nombreVerticeFinal = aux #Se cambia el vertice final al padre para explorar el siguiente padre
                       
        cont = 0
        for i in range(len(camino_invertido)-1, -1, -1): #Se imprime el camino
            print(camino_invertido[i], sep=' ', end=' ', file=sys.stdout, flush=False) # Modificar la funcion print para que no haga
            cont += 1                                                                  # salto de linea automatico
            if cont < len(camino_invertido):
                print("->", sep=' ', end=' ', file=sys.stdout, flush=False)
            
    def __str__(self): 
        s = ''
        for v in self.vertices:
            aux = 0
            s += self.vertices[v].nombre + ' - ['
            for i in self.vertices[v].vecinos:
                s += i.nombre #+ ','
                aux += 1
                if aux < len(self.vertices[v].vecinos):
                    s += ', '
            s += ']\n'
        return s

    def __repr__(self):
        s = ''
        for v in self.vertices:
            s += self.vertices[v].nombre + '-'
        return s
        


g = Grafo() #Creacion del objeto grafo

#Agregar todas las lineas del metro
for i in range(len(subway.lineas)):
    for j in range(len(subway.lineas[i])):
        g.agregarVertice(subway.lineas[i][j])

#Agregar las aristas entre las estaciones de cada linea
for k in range(len(subway.lineas)):
    for i in range(len(subway.lineas[k])-1):
        g.agregarArista(subway.lineas[k][i], subway.lineas[k][i+1])

#Ruta Aquiles Serdán -> Iztapalapa
inicio = 'Aquiles Serdán'
final = 'Iztapalapa'
#Usando Breadth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Breadth First Search\n")
g.EncontrarCaminoBFS(inicio, final)
#Usando Depth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Depth First Search\n")
g.EncontrarCaminoDFS(inicio, final)

#Ruta San Antonio -> Aragón
inicio = 'San Antonio'
final = 'Aragón'
#Usando Breadth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Breadth First Search\n")
g.EncontrarCaminoBFS(inicio, final)
#Usando Depth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Depth First Search\n")
g.EncontrarCaminoDFS(inicio, final)

#Ruta Vallejo -> Insurgentes
inicio = 'Vallejo'
final = 'Insurgentes'
#Usando Breadth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Breadth First Search\n")
g.EncontrarCaminoBFS(inicio, final)
#Usando Depth First Search
print("\n------------------------------------------------------------------------------------------------------------------------")
print("Ruta: [",inicio,"->",final,"] usando Depth First Search\n")
g.EncontrarCaminoDFS(inicio, final)
