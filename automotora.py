class Automotora:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.vehiculos = []  

    def agregarVehiculo(self, vehiculo: Vehiculo):
        """Agrega un vehículo (Auto o Motocicleta) a la lista."""
        self.vehiculos.append(vehiculo)
        print(f"Vehículo [{vehiculo.patente}] agregado exitosamente a {self.nombre}.")

    def mostrarVehiculos(self):
        """Muestra todos los vehículos registrados en la automotora."""
        print(f"\n=== VEHÍCULOS REGISTRADOS EN: {self.nombre.upper()} ===")
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        for v in self.vehiculos:
            v.mostrarInfo()
            print("-" * 50)