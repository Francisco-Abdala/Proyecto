from persona import Persona
import json
import random

#Carga los datos del archivo json
with open("texto.json") as archivo:
    datos = json.load(archivo)

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

        #Número de recuperados
        self.__recuperados = 0

        #Número de susceptibles
        self.__susceptibles = parametro1

        #Número de muertos
        self.__muertos = 0
        #Función que crea gente
        self.__vacunas = []
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
    def get_enfermos(self):
        return self.__enfermos
    def get_probabilidad_conexion_fisica(self):
        return self.__probabilidad_conexion_fisica
    def get_num_infectado(self):
        return self.__num_infectados
    def get_habitantes(self):
        return self.__habitantes
    def get_fallecidos(self):
        return self.__muertos
    def get_recuperados(self):
        return self.__recuperados
    def get_susceptible(self):
        return self.__susceptibles
    def get_muertos(self):
        return self.__muertos
    def get_vacunas(self):
        return self.__vacunas
#Métodos set para crear los datos necesarios
    def set_habitantes(self, parametro):
        if isinstance(parametro, Persona):
            self.__habitantes.append(parametro)   
        else:
           print("que")    
    def set_promedio_conexion_fisica(self,parametro):
        if isinstance(parametro, int):
            self.__promedio_conexion_fisica = parametro
        else:
            raise TypeError("El promedio de conexion fisica debe ser un numero entero")
    def set_fallecidos(self,parametro): 
        self.__fallecidos += parametro
    def set_num_infectados(self,parametro):
        if isinstance(parametro,int):
            self.__num_infectados = self.__num_infectados + parametro
        else:
            raise ValueError("No es un numero")
    def set_num_recuperados(self,parametro):
        if isinstance(parametro, int):
            self.__recuperados = self.__recuperados + parametro
        else:
            raise ValueError("No es un número")
    def set_num_susceptibles(self,parametro):
        if isinstance(parametro, int):
            self.__susceptibles = self.__susceptibles + parametro
        else:
            raise ValueError("No es un número")
    def set_num_muertos(self,parametro):
        if isinstance(parametro, int):
            self.__muertos = self.__muertos + parametro
        else:
            raise ValueError("No es un número")
    def set_vacuna(self,parametro):
        self.__vacunas.append(parametro)
#Crea la gente que estará en la comunidad
    def crear_gente(self):
            #Clase persona
            individuo = Persona()
            #Crea la lista de nombres 
            nombres = datos["nombres"]

            #Crea la lista de apellidos
            apellidos = datos["apellidos"]
            
            #Será utilizado para obtener el id de las personas
            contador = 0
            for _ in range(self.__num_ciudadanos):
                contador += 1
                individuo.set_id(contador)
                individuo.set_nombre(nombres[random.randint(0, 153)])
                individuo.set_familia(apellidos[random.randint(0,153)])
                individuo.set_estado("S")
                self.set_habitantes(individuo)
