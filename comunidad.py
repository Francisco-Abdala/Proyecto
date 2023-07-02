from persona import Persona
import json
import random

class Comunidad():
    def __init__(self,parametro1,parametro2):
        #Cantidad de ciudadanos
        self.__num_ciudadanos = None

        #Lista de objetos persona
        self.__habitantes = []

        #Media de conexiones fisicas
        self.__promedio_conexion_fisica = parametro1

        #La clase enfermedad
        self.__enfermedad = None

        #Número de infectados
        self.__num_infectados = None

        #Probabilidad de interacción de una persona con otra
        self.__probabilidad_conexion_fisica = parametro2

        self.crear_gente()

#Métodos get para ingresar a los datos    
    def get_num_ciudadanos(self):
        return self.__num_ciudadanos
    
    def get_promedio_conexion_fisica(self):
        return self.__promedio_conexion_fisica
    

    def get_enfermedad(self):
        return self.__enfermedad
    

    def get_num_infectados(self):
        return self.__num_infectados
    

    def get_probabilidad_conexion_fisica(self):
        return self.__probabilidad_conexion_fisica
    

#Crea la gente que estará en la comunidad
    def crear_gente(self):
        with open("texto.json") as archivo:
            individuo = Persona()
            lista_de_familia = []
            datos = json.load(archivo)
            #Crea la lista de nombres 
            nombres = datos["nombres"]
            #Crea la lista de apellidos
            apellidos = datos["apellidos"]
            for i in range(10):
                ayuda = list(set([apellidos[random.randint(0, 153)]]))
                lista_de_familia.append(ayuda)
                contador = 0
                for k in range(10):
                    contador += 10
                    lista_de_familias = []
                    for j in range(10):
                        contador += 1
                        individuo.set_id(contador)
                        individuo.set_nombre(nombres[random.randint(0, 153)])
                        individuo.set_familia((lista_de_familia[i][0]))
                        individuo.set_estado("S")
                        lista_de_familias.append(individuo)
                        self.set_habitantes(lista_de_familias)
                        print(lista_de_familias.get_nombre(),lista_de_familias.get_familia())

    def conexiones(self):
        while True:
            conexion = random.gauss(self.__prom_coneccion_fisica, self.__prom_coneccion_fisica/4)
            if conexion >= 0 and conexion < self.__prom_coneccion_fisica*3:
                break
        return int(conexion)

    def contagiar_random(self):
        while True:
            ayuda = random.randint(0, self.__num_ciudadanos - 1)
            ciudadano = self.__ciudadanos[ayuda]
            if ciudadano.get_estado() == "S":
                ciudadano.set_contador(self.__enfermedad.set_contador())
                return ciudadano
            elif ciudadano.get_estado() in ["E", "I"]:
                return None





#Métodos set para crear los datos necesarios
    def set_habitantes(self, parametro):
        if isinstance(parametro, list):
            self.__habitantes.append(parametro)   
        else:
            raise TypeError("El parametro debe ser de tipo lista")
        
    def set_promedio_conexion_fisica(self,parametro):
        if isinstance(parametro, int):
            self.__promedio_conexion_fisica = parametro
        else:
            raise TypeError("El promedio de conexion fisica debe ser un numero entero")