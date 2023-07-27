import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

class Simulacion():
    def __init__(self, parametro1,parametro2,parametro3):
        #La comunidad que tendrá la enfermedad
        self.__comunidad = parametro1

        #La enfermedad como tal
        self.__enfermedad = parametro2

        #Días
        self.__pasos = parametro3

#Métodos get para la obtención de los datos cuando se requiera
    def get_pasos(self):
        return self.__pasos
    def get_cuenta(self):
        return self.__cuenta
    def get_enfernedad(self):
        return self.__enfermedad
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
        np.random.seed() 
        caso_0 = self.__comunidad.get_habitantes()[0]
        caso_0.set_estado("I")

        susceptibles = [self.__comunidad.get_num_ciudadanos() - self.__comunidad.get_vacunados() - 1]
        infectados = [1]
        recuperados = [self.__comunidad.get_vacunados()]
        muertos = [0]
        for _ in range(self.__pasos):
            nuevo_i = 0
            nuevo_r = 0
            nuevo_f = 0

            for persona in self.__comunidad.get_habitantes():
                if persona.get_estado() == "I":
                    if np.random.random() < 0.1:
                        persona.set_estado("R")
                        nuevo_r += 1
                    else: 
                        if np.random.random() < self.__enfermedad.get_muerte():
                            self.__comunidad.get_habitantes().remove(persona)
                            nuevo_f +=1
                        else:
                            for vecino in self.__comunidad.get_habitantes():
                                if vecino.get_estado() == "S" and np.random.normal(self.__comunidad.get_enfermedad().get_infeccion_probable, self.__comunidad.get_enfermedad().get_infeccion_probable()/2) > 0:
                                    vecino.set_estado("I")
                                    nuevo_i += 1


            susceptibles.append(susceptibles[-1] - nuevo_i)
            infectados.append(infectados[-1] + nuevo_i - nuevo_r - nuevo_f)
            recuperados.append(recuperados[-1] + nuevo_r)
            muertos.append(muertos[-1] + nuevo_f)

            nuevo_i = 0
            nuevo_r = 0
            nuevo_f = 0

            if _ > 0:
                
                for persona in self.__comunidad.get_habitantes():
                    if persona.get_estado() == "I":
                        
                        # Obtener vecinos susceptibles
                        vecinos_susceptibles = [vecino for vecino in self.__comunidad.get_habitantes() if vecino.get_estado() == "S"]
                        
                        # Determinar cuántos vecinos se infectarán
                        num_vecinos_infectados = int(min(self.__comunidad.get_enfermedad().get_infeccion_probable(), len(vecinos_susceptibles)))
                       
                        # Elegir al azar los vecinos que serán infectados
                        infectados_vecinos = random.sample(vecinos_susceptibles, num_vecinos_infectados)
                        
                        # Infectar a los vecinos seleccionados
                        for vecino in infectados_vecinos:
                            vecino.set_estado("I")
                            nuevo_i += 1
            infectados[-1] += nuevo_i
            recuperados[-1] += nuevo_r
            muertos[-1] += nuevo_f



        data = {'Day': range(len(susceptibles)), 
                    'Susceptible': susceptibles,
                    'Infected': infectados,
                    'Recovered': recuperados,
                    'Deaths': muertos}
        df = pd.DataFrame(data)
        print(df)

