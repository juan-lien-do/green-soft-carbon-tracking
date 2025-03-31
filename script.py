from codecarbon import EmissionsTracker
import time
import os

def main():
    # Configura el tracker (sin carbon_intensity en el constructor)
    tracker = EmissionsTracker(
        save_to_file=False,  # No guardar en archivo
        log_level="error",   # Solo mostrar errores
    )

    # MODIFICA ESTA LINEA PARA CAMBIAR LA CANTIDAD DE TIEMPO DURANTE EL MUESTREO
    minutos = 10

    # Fuerza el factor de emisión (para versiones que no lo soportan en el constructor)
    os.environ["CO2_SIGNAL_API_KEY"] = "dummy"  # Evita errores de API
    os.environ["EMISSIONS_FACTOR"] = "0.26"     # Fija el factor a 0.26 kg CO2eq/kWh

    segundos = minutos * 60
    try:
        print("Iniciando el monitoreo de energía y emisiones...")
        tracker.start()

        # Simula una carga de trabajo (reemplázalo con tu código real)
        for i in range(segundos):
            print(f"Ejecutando iteración {i + 1}/{segundos}...")
            time.sleep(1)  # Simula procesamiento

    finally:
        # arbol = 0,34 ton co2

        # Detiene el tracker y muestra resultados
        emissions = tracker.stop()

        # cantidad co2 en tanto tiempo (minutos)
        cantidad = emissions
        #1440 minutos en un dia
        equivalencia_dia_anio = 365
        equivalencia_doshoras = 120 / minutos

        energia_sesion = tracker._total_energy.kWh
        emision_sesion = emissions

        energia_doshoras = energia_sesion * equivalencia_doshoras
        emision_doshoras = emision_sesion * equivalencia_doshoras

        energia_anio = energia_doshoras * equivalencia_dia_anio
        emision_anio = emision_doshoras * equivalencia_dia_anio

        print("\n--- Resultados ---")
        print(f"Consumo de energía de la sesión: {energia_sesion:.6f} kWh")
        print(f"Emisiones de CO₂eq de la sesión: {emision_sesion:.6f} kg \n")

        print(f"Consumo de energía de dos horas: {energia_doshoras:.6f} kWh")
        print(f"Emisiones de CO₂eq de dos horas: {emision_doshoras:.6f} kg \n")

        print("ESTIMADO")
        print(f"Consumo de energía de dos horas por día al año: {energia_anio:.6f} kWh")
        print(f"Emisiones de CO₂eq de dos horas por día al año: {emision_anio:.6f} kg \n")

        print(f"Factor de emisión usado: 0.26 kg CO₂eq/kWh")

if __name__ == "__main__":
    main()