# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:57:29 2021

@author: dios0
"""

class Vertice:
	def __init__(self, i):
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		if v not in self.vecinos:
			self.vecinos.append([v, p])
class Grafica:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, id):
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" llegando desde el vértice "+str(self.vertices[v].padre)+" es "+ str(self.vertices[v].costo))
			
	def camino(self, a, b):
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo]

	def minimo(self, l):
		if len(l) > 0:
			m = self.vertices[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None

	def dijkstra(self, a):
		if a in self.vertices:
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)
			while len(noVisitados) > 0:
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual
				self.vertices[actual].visitado = True
				noVisitados.remove(actual)
				actual = self.minimo(noVisitados)
		else:
			return False
class main:
    
    "instrucciones"
    "se crea una Grafica "
    "se usa la funcion agregarVertice para añadir los vertices"
    "seguidamente la funcion agregarArista donde colocaremos nombre del vertice, nombre de vertice vecino , valor de arista"
    
    g = Grafica()
    
    g.agregarVertice('1')
    g.agregarVertice('2')
    g.agregarVertice('3')
    g.agregarVertice('4')
    g.agregarVertice('5')
    g.agregarVertice('6')
    g.agregarVertice('7')
    g.agregarVertice('8')
    g.agregarVertice('9')
    g.agregarVertice('10')
    g.agregarArista('1', '2', 2)
    g.agregarArista('1', '3', 2)
    g.agregarArista('2', '5', 1)
    g.agregarArista('3', '5', 3)
    g.agregarArista('3', '4', 1)
    g.agregarArista('5', '7', 2)
    g.agregarArista('4', '6', 2)
    g.agregarArista('4', '8', 1)
    g.agregarArista('6', '7', 2)
    g.agregarArista('7', '10', 2)
    g.agregarArista('8', '10', 3)
    g.agregarArista('8', '9', 1)
    g.agregarArista('9', '10', 1)
    
    
    "ejecutamos la funcion de dijkstra"
    
    print("")
    print("--------------------------- Grande --------------------")
    print("-----Prueba desde el vértice '1' hasta vértice '10'----")
    print("\n[[La ruta más rápida por Dijkstra]su costo es]")
    g.dijkstra('1')
    
    "le indicamos al programa de que vértice a que vértice debera recorrer"
    print(g.camino('1', '10'))
    
    "print resultados"
    print("------------------------------------------------------")
    print("\nLos valores finales son:")
    g.imprimirGrafica()