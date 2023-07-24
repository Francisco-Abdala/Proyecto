import random

class Vacuna():
    def __init__(self,parametro):
        self.__vacunas_disponibles = parametro

#Métodos get para la obtención del valor para cuando se necesite
    def get_vacunas_disponibles(self):
        return self.__vacunas_disponibles
    
#Métodos set para la creación del valor para cuando se necesite
    def set_vacunas_disponibles(self,parametro):
        if isinstance(parametro,int):
            self.__vacunas_disponibles = parametro
        else:
            raise ValueError("No es un número")
        
    
#Primera Vacuna con un 100% de efectividad
class Vacuna_A(Vacuna):
    def __init__(self, parametro):
        super().__init__(parametro)

        self.__vacunas_disponibles = parametro * 0.25

    def vacunado(self,parametro):
        if parametro.get_estado() == "I":
            parametro.set_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1

#Segunda vacuna con un 50% de efectividad
class Vacuna_B(Vacuna):
    def __init__(self, parametro):
        super().__init__(parametro)
        self.__vacunas_disponibles = parametro * 0.5
    def vacunado(self,parametro):
        ayuda = random.randint(0,1)
        if parametro.get_estado() == "I" and ayuda == 0:
            parametro.set_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1
        else:
            pass

#Tercera vacuna con un 20% de efectividad
class Vacuna_C(Vacuna):
    def __init__(self, parametro):
        super().__init__(parametro)
        self.__vacunas_disponibles = parametro * 0.25
    def vacunado(self,parametro):
        ayuda = random.randint(1,10)
        if parametro.get_estado() == "I" and ayuda < 3:
            parametro.get_estado("R")
            self.__vacunas_disponibles = self.__vacunas_disponibles - 1
        else:
            pass    




        
