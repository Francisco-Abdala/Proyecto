import random


class Vacuna_C():
    def __init__(self, parametro):
        #Cantidad de vacunas disponibles
        self.__vacunas_disponibles = int(parametro * 0.25)
    def get_vacunas_disponibles(self):
        return self.__vacunas_disponibles
#Vacuna a la gente
    def vacunado(self,parametro):
        ayuda = random.randint(1,10)
        if parametro.get_estado() == "I" and ayuda < 3:
            parametro.get_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1
        else:
            pass    




        
