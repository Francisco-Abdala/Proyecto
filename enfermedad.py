import random

class Enfermedad():
    def __init__(self,parametro,parametro2,parametro3):
        #Referencia a la probabilidad de infección de una persona
        self.__infeccion_probable = parametro
        
        #Referencia a la cantidad de días en la que deja de ser infecciosa
        self.__promedio_pasos = parametro2

        #Referencia a qué tan mortal es la enfermedad
        self.__muerte = parametro3
#Métodos get para obtener el parametro que se necesite
    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def get_promedio_pasos(self):
        return self.__promedio_pasos

    def get_muerte(self):
        return self.__muerte



#Entrega la cantidad de días que debería tener una persona cuando se enferma,devuelve la cantidad de días que tiene la persona  
    def set_contador(self):
        while True:
            referencia = int(random.gauss(self.__promedio_pasos,self.__promedio_pasos/4))
            if referencia > 0:
                return referencia




#Determina la muerte de la persona, True si muere, False si no muere
    def muerte(self):
        while True:
            referencia = random.randint(0,100)
            if referencia <= self.__muerte:
                return True
            else:
                return False



#Determina si alguien se contagió
    def contagio(self):
        while True:
            referencia = random.randint(0,100)
            if referencia <= self.__infeccion_probable:
                return True
            else:
                return False