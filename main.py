from os import system
system("cls")
from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():
    
    mi_automotora = Automotora("Automotora Central Puente Alto")

    
    auto1 = Auto("ABCD-12", "Toyota", "Yaris", 2020, 8500000, 4, "Gasolina")
    auto2 = Auto("XYZW-34", "Suzuki", "Swift", 2024, 11000000, 5, "Híbrido")

    
    moto1 = Motocicleta("AA-0123", "Yamaha", "MT-07", 2023, 7990000, 689, "Deportiva")
    moto2 = Motocicleta("BB-0987", "Honda", "CB125F", 2022, 1800000, 125, "Urbana")

    print("\n--- REGISTRANDO VEHÍCULOS ---")
    
    mi_automotora.agregarVehiculo(auto1)
    mi_automotora.agregarVehiculo(auto2)
    mi_automotora.agregarVehiculo(moto1)
    mi_automotora.agregarVehiculo(moto2)

    
    mi_automotora.mostrarVehiculos()

    
    print("\n--- PRUEBAS DE AUTOMÓVIL ---")
    auto1.mostrarInfo()
    auto1.abrirMaletero()
    anos_auto = auto1.calcularAñosUso(2026)
    print(f"Años de uso del automóvil: {anos_auto} años.")

    
    print("\n--- PRUEBAS DE MOTOCICLETA ---")
    moto1.mostrarInfo()
    moto1.encenderMotor()
    print(f"¿Es de alta cilindrada?: {'Sí' if moto1.esDeAltaCilindrada() else 'No'}")
    
    print("\nSegunda motocicleta para contraste de cilindrada:")
    moto2.mostrarInfo()
    print(f"¿Es de alta cilindrada?: {'Sí' if moto2.esDeAltaCilindrada() else 'No'}")
    
    anos_moto = moto1.calcularAñosUso(2026)
    print(f"Años de uso de la motocicleta {moto1.marca}: {anos_moto} años.")

    
    vendedor1 = Vendedor("Juan Pérez", "12.345.678-9", "+56912345678")

    
    vendedor1.mostrarDatos()

    
    print("\n=== CÁLCULO DE COMISIONES ===")
    venta_alta = 6500000
    comision1 = vendedor1.calcularComision(venta_alta)
    print(f"Venta: ${venta_alta:,.0f} | Comisión (10%): ${comision1:,.0f}")

    venta_baja = 3200000
    comision2 = vendedor1.calcularComision(venta_baja)
    print(f"Venta: ${venta_baja:,.0f} | Comisión (5%): ${comision2:,.0f}")



if __name__ == "__main__":
    main()
