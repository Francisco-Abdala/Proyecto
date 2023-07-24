import random

class Vacuna_B():
    def __init__(self, parametro):
        #Cantidad de vacunas disponibles
        self.__vacunas_disponibles = int(parametro * 0.5)
    def get_vacunas_disponibles(self):
        return self.__vacunas_disponibles
#Vacuna a la gente
    def vacunado(self,parametro):
        ayuda = random.randint(0,1)
        if parametro.get_estado() == "I" and ayuda == 0:
            parametro.set_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1
        else:
            pass
