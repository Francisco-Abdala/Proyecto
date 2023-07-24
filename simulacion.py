import random
from time import sleep
class Simulacion():
    def __init__(self, parametro1,parametro2,parametro3):
        #La comunidad que tendrá la enfermedad
        self.__comunidad = parametro1

        #La enfermedad como tal
        self.__enfermedad = parametro2

        #Días
        self.__pasos = parametro3

        #contador
        self.__cuenta = 0
        #Infectados por día
        self.__infectados = 0
        #Fallecidos por día
        self.__fallecidos = 0

        #Susceptibles por día
        self.__susceptible = 0
#Métodos get para la obtención de los datos cuando se requiera
    def get_pasos(self):
        return self.__pasos
    def get_cuenta(self):
        return self.__cuenta
    def get_enfernedad(self):
        return self.__enfermedad
    def get_fallecidos(self):
        return self.__fallecidos
    def get_susceptible(self):
        return self.__susceptible
    def get_infectados(self):
        return self.__infectados
    
#Métodos set para la creación de datos cuando se requiera
    def set_infectados(self,parametro):
        if isinstance(parametro,int):
            self.__infectados = parametro
        else:
            raise ValueError("No es un número")
    def set_fallecidos(self,parametro):
        if isinstance(parametro,int):
            self.__fallecidos = parametro
        else:
            raise ValueError("No es un número")
    def set_susceptible(self,parametro):
        if isinstance(parametro,int):
            self.__susceptible = parametro
        else:
            raise ValueError("No es un número")

#Inicia simulación
    def comienzo(self):
       contador = 0
       for i in range(2):
            contador += 1
            #Cantidad de personas susceptibles
            susceptibles = self.__comunidad.get_susceptible()

            #Cantidad de personas infectadas
            infectados = self.__comunidad.get_num_infectados()

            #Cantidad de personas recuperadas
            recuperados = self.__comunidad.get_recuperados()

            #Capacidad de transmisión de la enfermedad
            transmision = self.__enfermedad.get_infeccion_probable()

            #Tasa de recuperación
            recuperacion = 1

            #Tasa de mortalidad
            muerte = self.__enfermedad.get_muerte()

            #Cantidad de muertos
            muertos = self.__comunidad.get_muertos()

            #Formulas del modelo SIR
            susceptible = (transmision*susceptibles) - infectados
            infectado = infectados + (transmision * susceptibles * infectados) - (recuperacion * infectados) -  (muerte * infectados)
            print(infectado,transmision,susceptibles,infectados,recuperacion,muerte)
            recuperado = recuperados + (recuperacion * infectados)
            muerto = muertos + (muerte * infectados)

            #Personas susceptibles
            for i in range(self.__comunidad.get_num_ciudadanos()):
                for _ in self.__comunidad.get_habitantes():
                    if self.__comunidad.get_habitantes()[i-1].get_estado() == "S":
                        self.__comunidad.set_num_susceptibles(1)

            #Personas infectadas
            for i in range(self.__comunidad.get_num_ciudadanos()):
                for _ in self.__comunidad.get_habitantes():
                    if self.__comunidad.get_habitantes()[i-1].get_estado() == "S":
                        self.__comunidad.get_habitantes()[i-1].set_estado("I")
                        self.__comunidad.set_num_infectados(1)
                        self.__comunidad.set_num_susceptibles(-1)

                
            #Personas recuperadas
            for i in range(self.__comunidad.get_num_ciudadanos()):
                for _ in self.__comunidad.get_habitantes():
                    if self.__comunidad.get_habitantes()[i-1].get_estado() == "I" and contador >=3:
                        self.__comunidad.set_num_recuperados(1)
                        self.__comunidad.set_num_susceptibles(-1)
                        self.__comunidad.set_num_infectados(-1)
                        self.__comunidad.get_habitantes()(i-1).set_estado("R")

            #Personas muertas
            for i in range(self.__comunidad.get_num_ciudadanos()):
                for _ in self.__comunidad.get_habitantes():
                    if self.__comunidad.get_habitantes()[i-1].get_estado() == "I" and self.__comunidad.get_habitantes()[i].get_vivencia() == True:
                        self.__comunidad.get_habitantes()[i-1].set_estado("F")
                        self.__comunidad.get_habitantes()[i-1].set_vivencia(False)
                        self.__comunidad.set_num_infectados(-1)
                        self.__comunidad.set_num_muertos(1)
                
            

            print(f"Día: {contador}, poblacion: {self.__comunidad.get_num_ciudadanos()}, infectados: {infectado}, recuperados: {recuperado}, fallecidos: {muerto}")
            susceptibles = 0
            infectados = 0
            recuperados = 0
            muertos = 0
            susceptible = 0
            infectado = 0
            recuperado = 0
            muerto = 0
        
