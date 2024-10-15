from empleado import Empleado

class Mecanico(Empleado):
    def __init__(self, nombre, salario, especialidad, experiencia):
        super().__init__(nombre, salario)
        self._especialidad = especialidad
        self._experiencia = experiencia
    
    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, nuevo_especialidad):
        self._especialidad = nuevo_especialidad
    
    @property
    def experiencia(self):
        return self._experiencia
    
    @experiencia.setter
    def experiencia(self, nuevo_experiencia):
        self._experiencia= nuevo_experiencia