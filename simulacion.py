import io
import random
import matplotlib.pyplot as plt
import statsmodels.api as sm
from time import sleep
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

        self.__enfermos = [self.__comunidad.get_num_infectados()]
        #Fallecidos por día
        self.__fallecidos = [0]

        #Susceptibles por día
        self.__susceptible = [self.__comunidad.get_num_ciudadanos() - self.__comunidad.get_num_infectados()]
        
#Métodos get para la obtención de los datos cuando se requiera
    def get_pasos(self):
        return self.__pasos
    
    def get_cuenta(self):
        return self.__cuenta
    
    def otro_dia(self):
        self.__cuenta += self.__cuenta
#Comienza las infecciones
    def comienzo(self):
        for _ in range(self.__pasos):
            #Considera el día cero
            if self.__cuenta == 0:
                self.caso_cero()
                sleep(2)
            #Si es otro día,cambia de día
            else:
                self.pasar_el_dia()

            self.__cuenta += 1
            self.datos()

#Creación del primer caso
    def caso_cero(self):
        caso_0 = self.__comunidad.get_num_infectados()
        poblacion = self.__comunidad.get_num_ciudadanos()
        personas = self.__comunidad.get_habitantes()
        for _ in range(caso_0):
            while True:
                ayuda = random.randint(0, poblacion - 1)
                if personas[ayuda].get_estado() == "S":
                    personas[ayuda].set_estado("I")
                    personas[ayuda].set_contador(self.__enfermedad.set_contador())
                    break
                else:
                    ayuda = None

        for persona in range(len(personas)-1):
            ayuda = personas[persona]
            print(type(ayuda))
            self.__comunidad.set_habitantes(ayuda)

#Muestra el avance y cambio de la enfermedad en la poblacion
    def datos(self):
        dia = self.__cuenta
        contagio = self.__comunidad.get_num_infectados()
        infectados = self.__comunidad.get_num_infectados()
        fallecidos = self.__comunidad.get_fallecidos()
        print(f"Día: {dia}, contagiados totales: {contagio}, enfermos: {infectados}, muertos {fallecidos}\n")

#Guarda los datos en las variables necesarias
    def leer_datos(self):
        fallecidos = 0
        infectados = 0
        recuperados = 0
        susceptibles = 0
        #Compara sus estados para obtener cuantos hay de cada uno
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "F":
                fallecidos +=1
            elif ciudadano.get_estado() == "I":
                infectados +=1
            elif ciudadano.get_estado() == "R":
                recuperados += 1
            elif ciudadano.get_estado() == "S":
                susceptibles +=1

        #Agrega los datos donde deben estar
        self.__comunidad.set_fallecidos(fallecidos)
        self.__fallecidos.append(fallecidos)

        self.__comunidad.set_enfermos(infectados)
        self.__enfermos.append(infectados)

        self.__comunidad.set_num_infectados(fallecidos+infectados+recuperados)
        self.__infectados.append(fallecidos+infectados+recuperados)


        self.__susceptible.append(susceptibles)

#Crea la red de contagios
    def contagiar(self):
        enfermos = []
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "I":
                conexiones = self.__comunidad.conexiones()
                for _ in range(conexiones):
                    if self.__comunidad.contacto_estrecho():
                            enfermo = self.__comunidad.contagiar_contacto_estrecho(ciudadano)
                            if isinstance(enfermo,Persona):
                                enfermos.append(enfermo)
                    else:
                        if self.__enfermedad.contagio():
                            nuevo_enfermo = self.__comunidad.contagiar_random()
                            if isinstance(nuevo_enfermo, Persona):
                                enfermos.append(nuevo_enfermo)
        for i in range(len(enfermos)):
            enfermos[i].set_estado("I")




#Verifica si siguen enfermos,luego comparan cuantos días llevan con la enfermedad, si pasaron todos los días, determina si esta muerto o recuperado
    def continua_enfermo(self):
        for ciudadano in self.__comunidad.get_habitantes():
            if ciudadano.get_estado() == "I":
                ciudadano.restar_contador()
                if ciudadano.get_contador() == 0:
                    if self.__enfermedad.muerte():
                        ciudadano.set_estado("F")
                    else:
                        ciudadano.set_estado("R")

#Muestra el gráfico de la enfermedad
    def mostrar_grafico(self):
        plt.show()
        plt.plot(self.__enfermos)
        plt.plot(self.__infectados)
        plt.plot(self.__fallecidos)
        plt.plot(self.__susceptible)
        plt.grid() 
        plt.xlabel('Días')
        plt.ylabel('Población')

        if self.__pasos== self.__cuenta:
            plt.title(f"Gráfico Modelo SIR Final de la sumlación ({self.__pasos} días)")
        else:
            plt.title(f"Gráfico Modelo SIR día {self.__cuenta}")
#Cambia de día
    def pasar_el_dia(self):
        self.continua_enfermo()
        self.contagiar()
        self.leer_datos()
