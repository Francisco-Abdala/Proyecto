import random
import matplotlib.pyplot as plt
import numpy as np
from persona import Persona

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
        self.__infectados = [self.__comunidad.get_num_infectados()]

        #Fallecidos por día
        self.__fallecidos = [0]

        #Susceptibles por día
        self.__susceptible = [self.__comunidad.get_num_ciudadanos() - self.__comunidad.get_num_infectados()]
        

    def get_pasos(self):
        return self.__pasos
    

    def get_cuenta(self):
        return self.__cuenta
    
    def otro_dia(self):
        self.__cuenta += self.__cuenta
    

    def comienzo(self):
        for i in range(self.__pasos):
            if self.__cuenta == 0:
                self.caso_cero()
            else:
                self.pasar_el_dia()
            self.__cuenta += 1
            self.datos()


    def caso_cero(self):
        caso_0 = self.__comunidad.get_num_infectado()
        poblacion = self.__comunidad.get_num_ciudadanos()
        personas = self.__comunidad.get_habitantes()
        for _ in range(caso_0):
            while True:
                ayuda = random.randint(0, poblacion)
                if personas[ayuda].get_estado() == "S":
                    personas[ayuda].set_estado("E")
                    personas[ayuda].set_contador(self.__enfermedad.set_contador())
                    break
                else:
                    ayuda = None

        self.__comunidad.set_habitantes(personas)

    def datos(self):
        dia = self.__cuenta
        contagio = self.__comunidad.get_num_infectados()
        infectados = self.__comunidad.get_num_infectados()
        fallecidos = self.__comunidad.get_fallecidos()
        print(f"Día: {dia}, contagiados totales: {contagio}, enfermos: {infectados}, muertos {fallecidos}\n")

    def leer_datos(self):
        fallecidos = 0
        infectados = 0
        recuperados = 0
        susceptibles = 0
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "F":
                fallecidos +=1
            elif ciudadano.get_estado() == "I":
                infectados +=1
            elif ciudadano.get_estado() == "R":
                recuperados += 1
            elif ciudadano.get_estado() == "S":
                susceptibles +=1


        self.__comunidad.set_fallecidos(fallecidos)
        self.__fallecidos.append(fallecidos)
        self.__comunidad.set_num:infectados(infectados)
        self.__infectados.append(infectados)
        self.__comunidad.set_num_infectados(fallecidos+infectados+recuperados)
        self.__infectados.append(fallecidos+infectados+recuperados)
        self.__susceptible.append(susceptibles)


    def contagiar(self):
        enfermos = []
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "I":
                conexion = self.__comunidad.cantidad_conecciones()
                for _ in range(conexion): 
                    if self.__enfermedad.is_contagiado():
                        nuevo_enfermo = self.__comunidad.contagiar_random()
                        if isinstance(nuevo_enfermo, Persona):
                            enfermos.append(nuevo_enfermo)
        for i in range(len(enfermos)):
            enfermos[i].set_estado("I")




    def siguen_enfermos(self):
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "I":
                ciudadano.restar_contador()
                if ciudadano.get_contador() == 0:
                    if self.__enfermedad.is_muerto():
                        ciudadano.set_estado("F")
                    else:
                        ciudadano.set_estado("R")

    def mostrar_grafico(self):
        plt.clf()
        x = []
        for i in range(self.__contador):
            x.append(i+1)
        plt.plot(x,self.__enfermos_array)
        plt.plot(x,self.__infectados_array)
        plt.plot(x,self.__muertos_array)
        plt.plot(x,self.__susceptibles)
        plt.grid()    # rejilla
        plt.xlabel('Días')
        plt.ylabel('Población')

        if self.__dias == self.__contador:
            plt.title(f"Gráfico Modelo SIR Final de la sumlación ({self.__dias} días)")
        else:
            plt.title(f"Gráfico Modelo SIR día {self.__contador}")

    def pasar_el_dia(self):
        self.siguen_enfermos()
        self.contagiar()
        self.leer_datos()
