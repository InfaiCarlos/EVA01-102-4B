class Vehiculo:
    def __init__(self, patente: str, marca: str, modelo: str, año: int, precio: float):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        """Muestra los datos básicos del vehículo."""
        print(f"Patente: {self.patente} | Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.año} | Precio: ${self.precio:,.0f}")

    def calcularAñosUso(self, añoActual: int) -> int:
        """RN01: Los años de uso se calculan como: añoActual - añoFabricacion."""
        return añoActual - self.año