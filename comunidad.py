from persona import Persona
import json
import random

class Comunidad():
    def __init__(self,parametro1,parametro2,parametro3,parametro4,parametro5):
        #Cantidad de ciudadanos
        self.__num_ciudadanos = parametro1

        #Lista de objetos persona
        self.__habitantes = []

        #Media de conexiones fisicas
        self.__promedio_conexion_fisica = parametro4

        #La clase enfermedad
        self.__enfermedad = parametro2

        #Número de infectados
        self.__num_infectados = parametro3

        #Probabilidad de interacción de una persona con otra
        self.__probabilidad_conexion_fisica = parametro5

        self.__fallecidos = 0
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
    
    def get_num_infectado(self):
        return self.__num_infectados
    
    def get_habitantes(self):
        return self.__habitantes
    
    def get_fallecidos(self):
        return self.__fallecidos

#Crea la gente que estará en la comunidad
    def crear_gente(self):
        with open("texto.json") as archivo:
            #Clase persona
            individuo = Persona()

            #Información del archivo json
            datos = json.load(archivo)

            #Crea la lista de nombres 
            nombres = datos["nombres"]

            #Crea la lista de apellidos
            apellidos = datos["apellidos"]
            
            contador = 0

            for i in range(self.__num_ciudadanos):
                ayuda = list(set([apellidos[random.randint(0, 153)]]))
                for k in range(10):
                    contador +=10
                    for j in range(10):
                        contador += 1
                        individuo.set_id(contador)
                        individuo.set_nombre(nombres[random.randint(0, 153)])
                        individuo.set_estado("S")
                        self.set_habitantes(individuo)

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
        if isinstance(parametro, Persona):
            self.__habitantes.append(parametro)   
        else:
           print("olololo")
        
    def set_promedio_conexion_fisica(self,parametro):
        if isinstance(parametro, int):
            self.__promedio_conexion_fisica = parametro
        else:
            raise TypeError("El promedio de conexion fisica debe ser un numero entero")
        
    def set_fallecidos(self,parametro):
        self.__fallecidos = parametro
    def set_num_infectados(self,parametro):
        self.__num_infectados = parametro
