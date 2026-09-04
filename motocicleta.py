from vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, patente: str, marca: str, modelo: str, año: int, precio: float, cilindrada: int, tipo: str):
        
        super().__init__(patente, marca, modelo, año, precio)
        self.cilindrada = cilindrada
        self.tipo = tipo

    def mostrarInfo(self):
        """Sobrescribe mostrarInfo para incluir datos propios de la Motocicleta."""
        super().mostrarInfo()
        print(f" -> Tipo: Motocicleta | Cilindrada: {self.cilindrada}cc | Estilo: {self.tipo}")

    def encenderMotor(self):
        print(f"El motor de la motocicleta {self.marca} {self.modelo} ha sido encendido. ¡Brum brum!")

    def esDeAltaCilindrada(self) -> bool:
        """RN02: Una motocicleta es de alta cilindrada cuando su cilindrada es >= 600 cc."""
        if self.cilindrada >= 600:
            return True
        else:
            return False

    