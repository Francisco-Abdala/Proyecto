class Vacuna_A():
    def __init__(self, parametro):
        #Cantidad de vacunas disponibles
        self.__vacunas_disponibles = int(parametro * 0.25)

    def get_vacunas_disponibles(self):
        return self.__vacunas_disponibles
#Vacuna a la gente
    def vacunado(self,parametro):
        if parametro.get_estado() == "I":
            parametro.set_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1
