class Persona():
    def __init__(self):
        #Tipo None que al crearse el objeto será tipo int, identificador único de la persona
        self.__id = None

        #Tipo None que al crearse el objeto será tipo string, identifica su nombre
        self.__nombre = None

        #Tipo None que al crearse el objeto será tipo string, identifica su apellido
        self.__familia = None

        #Tipo None que al crearse el objeto será tipo Enfermedad, enfermedad que tiene la persona
        self.__enfermedad = None

        #Cambiará entre "S" de susceptible,"I" de infectado, "R" de recuperado y "F" de fallecido, identidica el estado de la persona
        self.__estado = None

        #Tipo None que al crearse el objeto será tipo int,identidica cuanto dura la enfermedad
        self.__contador = None

#Métodos get para obtener el parametro que se necesite.
    def get_comunidad(self):
        return self.__comunidad
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_familia(self):
        return self.__familia
    
    def get_enfermedad(self):
        return self.__enfermedad
    
    def get_estado(self):
        return self.__estado
    
    def get_contador(self):
        return  self.__contador

#Métodos set para crear el parametro que se necesite.
    def set_nombre(self,parametro):
        if isinstance (parametro,str):
            self.__nombre = parametro
        else:
            print("walalalaala")

    def set_familia(self,parametro):
        if isinstance (parametro,str):
            self.__familia = parametro
        else:
            print("olololo")

    def set_id(self,paramtetro):
        if isinstance(paramtetro,int):
            self.__id = paramtetro
        else:
            print("olololo")
            
    def set_comunidad(self,parametro):
        self.__comunidad = parametro

    def set_estado(self, estado):
        if estado in ["S", "R", "I", "F"]:
            self.__estado = estado
        
    def set_enfermedad(self,parametro):
        self.__enfermedad = parametro


    def set_contador(self,parametro):
        if isinstance(parametro,int):
            self.__contador = parametro
        else:
            print("olololo")

    #Método que indica cuantos días enfermo le queda a la persona, o en su caso, cuantos días de inmunidad tiene
    def restar_contador(self):
        self.__contador = self.__contador -1