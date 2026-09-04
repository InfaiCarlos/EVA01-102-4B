class Vendedor:
    def __init__(self, nombre: str, rut: str, telefono: str):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrarDatos(self):
        """Muestra la información del vendedor."""
        print(f"\n=== DATOS DEL VENDEDOR ===")
        print(f"Nombre: {self.nombre}")
        print(f"RUT: {self.rut}")
        print(f"Teléfono: {self.telefono}")

    def calcularComision(self, montoVenta: float) -> float:
        """RN03: Si el monto de la venta es >= $5.000.000 la comisión es del 10%.
        Si es menor, la comisión es del 5%."""
        if montoVenta >= 5000000:
            return montoVenta * 0.10
        else:
            return montoVenta * 0.05

        