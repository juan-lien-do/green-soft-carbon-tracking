from codecarbon import EmissionsTracker
import psutil
import time
import os

# Configura el factor de emisión (0.26 kg CO₂eq/kWh para tu país)
os.environ["EMISSIONS_FACTOR"] = "0.26"
os.environ["CO2_SIGNAL_API_KEY"] = "dummy"  # Evita errores de API

def main():
    # Configuración
    minutos_monitoreo = 1  # Cambia este valor para más tiempo
    segundos = minutos_monitoreo * 60

    # Inicializa el tracker de CodeCarbon
    tracker = EmissionsTracker(
        save_to_file=False,
        log_level="error",
    )

    try:
        print(f"🔍 Monitoreando CPU por {minutos_monitoreo} minuto(s)...")
        tracker.start()

        total_cpu_usage = 0.0
        muestras = 0

        for i in range(segundos):
            cpu_usage = psutil.cpu_percent(interval=1)  # Uso de CPU en %
            total_cpu_usage += cpu_usage
            muestras += 1

            print(f"⏳ [{i + 1}/{segundos}] CPU: {cpu_usage:.1f}%")
            time.sleep(1)  # Intervalo de 1 segundo

        avg_cpu = total_cpu_usage / muestras  # Uso promedio de CPU

    finally:
        # Detiene el tracker y obtiene resultados
        emissions = tracker.stop()
        energia_total = tracker._total_energy.kWh

        # Cálculos extrapolados (2 horas al día, 365 días)
        horas_anio = 2 * 365
        energia_anio = energia_total * (120 / minutos_monitoreo) * 365
        emisiones_anio = emissions * (120 / minutos_monitoreo) * 365

        # Resultados
        print("\n📊 --- Resultados ---")
        print(f"⚡ Consumo de energía (sesión): {energia_total:.6f} kWh")
        print(f"🌍 Emisiones CO₂eq (sesión): {emissions:.6f} kg")
        print(f"🖥️ CPU promedio: {avg_cpu:.1f}%\n")

        print("📅 **Extrapolación Anual (2 horas/día)**")
        print(f"⚡ Energía/año: {energia_anio:.3f} kWh")
        print(f"🌍 Emisiones/año: {emisiones_anio:.3f} kg CO₂eq")
        print(f"🌳 Equivale a ~{emisiones_anio / 21:.2f} árboles/año*")

if __name__ == "__main__":
    main()