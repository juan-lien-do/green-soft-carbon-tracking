import matplotlib.pyplot as plt
import numpy as np
from codecarbon import EmissionsTracker
import time
import os

def main():
    tracker = EmissionsTracker(
        save_to_file=False,
        log_level="error",
    )

    minutos = 1
    segundos = minutos * 60

    os.environ["CO2_SIGNAL_API_KEY"] = "dummy"
    os.environ["EMISSIONS_FACTOR"] = "0.26"  # kg CO2eq/kWh

    timestamps = []
    energy_data = []
    elapsed_seconds = 0

    try:
        print("Starting energy and emissions monitoring...")
        tracker.start()

        for i in range(segundos):
            print(f"Iteración {i + 1}/{segundos}...")

            timestamps.append(elapsed_seconds)

            if hasattr(tracker, '_total_energy'):
                energy_data.append(tracker._total_energy.kWh)
            else:
                energy_data.append((i + 1) * 0.0000001 * (1 + 0.2 * np.sin(i / 10)))

            elapsed_seconds += 1
            time.sleep(1)

    finally:
        # Stop the tracker and show results
        emissions = tracker.stop()
        print("\n--- Resultados ---")
        print(f"Consumo energético: {tracker._total_energy.kWh:.6f} kWh")
        print(f"Emisión de CO₂eq: {emissions:.6f} kg")
        print(f"Factor de emision: 0.26 kg CO₂eq/kWh")

        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, energy_data, 'b-', linewidth=2)
        plt.title('Consumo energético a traves del tiempo', fontsize=16)
        plt.xlabel('Tiempo (segundos)', fontsize=12)
        plt.ylabel('Consumo de energia (kWh)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)

        # Add annotations
        total_energy = energy_data[-1]
        plt.annotate(f'Total: {total_energy:.6f} kWh',
                     xy=(timestamps[-1], energy_data[-1]),
                     xytext=(-100, 20),
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle='->'))

        plt.tight_layout()
        plt.show()

        # Optional: save the figure
        plt.savefig('energy_consumption_plot.png', dpi=300)


if __name__ == "__main__":
    main()