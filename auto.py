from vehiculo import Vehiculo
    
class Auto(Vehiculo):
    def __init__(self, patente: str, marca: str, modelo: str, año: int, precio: float, numPuertas: int, combustible: str):
        
        super().__init__(patente, marca, modelo, año, precio)
        self.numPuertas = numPuertas
        self.combustible = combustible

    def mostrarInfo(self):
        """Sobrescribe mostrarInfo para incluir datos propios del Auto."""
        super().mostrarInfo()
        print(f" -> Tipo: Auto | Puertas: {self.numPuertas} | Combustible: {self.combustible}")

    def abrirMaletero(self):
        print(f"El maletero del auto con patente {self.patente} ha sido abierto.")

    def tieneAireAcondicionado(self) -> bool:
        return True