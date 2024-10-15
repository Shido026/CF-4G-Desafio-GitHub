from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        self._salario = nuevo_salario