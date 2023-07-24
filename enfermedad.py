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
