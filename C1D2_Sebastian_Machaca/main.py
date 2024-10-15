from mecanico import Mecanico
from vehiculo import Vehiculo

def imorimir_vehiculo(vehi):
    print(f"Patente: {vehi.patente} - Marca: {vehi.marca} - Color: {vehi.color} - Problemas: {vehi.problemas}")

meca1 = Mecanico("Sebastian Machaca", 1000000, "Hidraulica", 10)
meca2 = Mecanico("Shidou Machaca", 1000000, "Motor", 6)

vehi1= Vehiculo("AA1122", "Hyundai", "Tucso", "Azul", "No enciende")
vehi2= Vehiculo("BB1122", "Hyundai", "Accent", "Blanco", "Luz delantera izquierda quebrada")
vehi3= Vehiculo("CC1122", "Suzuki", "Jimny", "Negro", "Chocado en puerta del conductor")
vehi4= Vehiculo("DD1122", "Suzuki", "Samurai", "Azul", "Problemas en el encendido")

vehiculo_meca1 = [vehi1, vehi2]
vehiculo_meca2 = [vehi3, vehi4]

print(f"{meca1.nombre}, con sus {meca1.experiencia} anos de experiencia, se especialista en {meca1.especialidad} y su sueldo es ${meca1.salario}")
print(f"{meca2.nombre}, con sus {meca2.experiencia} anos de experiencia, se especialista en {meca2.especialidad} y su sueldo es ${meca2.salario}")

print(f"Vehículos de {meca1.nombre}")
imorimir_vehiculo(vehiculo_meca1[0])
imorimir_vehiculo(vehiculo_meca1[1])

print(f"Vehículos de {meca2.nombre}")
imorimir_vehiculo(vehiculo_meca2[0])
imorimir_vehiculo(vehiculo_meca2[1])

vehi1.problemas= "Problmas eléctrico"
vehi3.problemas = "Chocado en la puerta de copiloto"

print(f"Vehículos de {meca1.nombre}")
imorimir_vehiculo(vehiculo_meca1[0])
imorimir_vehiculo(vehiculo_meca1[1])

print(f"Vehículos de {meca2.nombre}")
imorimir_vehiculo(vehiculo_meca2[0])
imorimir_vehiculo(vehiculo_meca2[1])