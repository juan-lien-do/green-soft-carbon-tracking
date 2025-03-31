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
    minutos = 1

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
        # Detiene el tracker y muestra resultados
        emissions = tracker.stop()
        print("\n--- Resultados ---")
        print(f"Consumo de energía: {tracker._total_energy.kWh:.6f} kWh")
        print(f"Emisiones de CO₂eq: {emissions:.6f} kg")
        print(f"Factor de emisión usado: 0.26 kg CO₂eq/kWh (fijado manualmente)")

if __name__ == "__main__":
    main()