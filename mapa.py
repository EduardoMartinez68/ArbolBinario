#crear arbol 
class ArbolBinario:
	def __init__(self,objetoRaiz):
		self.clave=objetoRaiz
		self.hijoIzquierdo=None
		self.hijoDerecho=None
		self.padre=None

    #añadir hijos (añadir decisiones)
	def insertarIzquierda(self,nuevoNodo):
		if self.hijoIzquierdo==None:
			self.hijoIzquierdo=ArbolBinario(nuevoNodo)

			self.hijoIzquierdo.padre=self   #insertar a tu padre 
		else:
			t=ArbolBinario(nuevoNodo)
			t.hijoIzquierdo=self.hijoIzquierdo
			self.hijoIzquierdo=t 

	def insertarDerecha(self,nuevoNodo):
		if self.hijoDerecho==None:
			self.hijoDerecho=ArbolBinario(nuevoNodo)

			self.hijoDerecho.padre=self   #insertar a tu padre 
		else:
			t=ArbolBinario(nuevoNodo)
			t.hijoDerecho=self.hijoDerecho  
			self.hijoDerecho=t 

	#averiguar quienes son mis hijos(saber cuales son mis decisiones)
	def obtenerHijoDerecha(self):
		if self.hijoDerecho==None:
		    return 'null'
		else:
			return self.hijoDerecho

	def obtenerHijoIzquierdo(self):
		if self.hijoIzquierdo==None:
		    return 'null'
		else:
			return self.hijoIzquierdo

	#averiguar lo que dice mi hijo 
	def asignarValorRaiz(self,obj):
		self.clave=obj

	def obtenerValorRaiz(self):
		return self.clave



#bucle para crear cosas en el arbol
def imprimirArbol(arbol):
	print(''' ''')
	#imprimir arbol padre
	print('padre')
	print(arbol.obtenerValorRaiz())
	#imprimir el valor del hijo derecha
	print('hijo derecho') 
	if(arbol.hijoDerecho==None):
		print('Null')
	else:
		print(arbol.obtenerHijoDerecha().obtenerValorRaiz())

    #imprimir el valor del hijo izquierdo
	print('hijo izquierda') 
	if(arbol.hijoIzquierdo==None):
		print('Null')
	else:
		print(arbol.obtenerHijoIzquierdo().obtenerValorRaiz())

def escribirArbol(arbol):
    #imprimir o llenar al hijo derecho
    menu=0
    while(menu!=3):
    	imprimirArbol(arbol)

        #menu 
    	print('''
    	1--escribir en el hijo derecho 
    	2--escribir en el hijo izquierdo
    	3--nada 
    	''')
    	menu=int(input('tu respuesta: '))

    	if(menu==1): 
	    	texto=input('ingresa dato hijo derecho: ')
	    	arbol.insertarDerecha(texto)
    	elif(menu==2):
	    	texto=input('ingresa dato hijo izquierda: ')
	    	arbol.insertarIzquierda(texto)
    	else:
	    	elegirCamino(arbol)

def elegirCamino(arbol):
	imprimirArbol(arbol)
	#avanzar por el nodo 
	print('''
		1---ir a la derecha 
		2---ir a la izquierda 
		3---regresar 
		''')
	lado=int(input(' ¿Porque lado quieres ir? '))
	print('')

	if (lado==1):
		#preguntar si existe algo
		if(arbol.hijoDerecho!=None): 
			avanzarArbol(arbol.hijoDerecho)
		else:
			escribirArbol(arbol)
	elif (lado==2):
		if(arbol.hijoIzquierdo!=None): 
			avanzarArbol(arbol.hijoIzquierdo)
		else:
			escribirArbol(arbol)
	else:
		if(arbol.padre!=None): 
			avanzarArbol(arbol.padre)
		else:
			escribirArbol(arbol)

def avanzarArbol(arbol):
	escribirArbol(arbol)


#crear arbol 
a=ArbolBinario('a')
avanzarArbol(a) #pasear por el 
