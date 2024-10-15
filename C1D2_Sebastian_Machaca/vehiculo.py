class Vehiculo():
    def __init__(self, patente, marca, modelo, color, problemas):
        self._patente = patente
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._problemas = problemas
    
    @property
    def patente(self):
        return self._patente
    
    @patente.setter
    def patente(self, nuevo_patente):
        self._patente = nuevo_patente
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, nuevo_marca):
        self._marca = nuevo_marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def nombre(self, nuevo_color):
        self._color = nuevo_color
    
    @property
    def problemas(self):
        return self._problemas
    
    @problemas.setter
    def problemas(self, nuevo_problemas):
        self._problemas = nuevo_problemas