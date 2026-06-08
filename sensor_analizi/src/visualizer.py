import matplotlib.pyplot as plt
import pandas as pd

def plot_telemetry(df: pd.DataFrame, title: str):
    """Telemetri verilerini grafiğe döker."""
    plt.figure(figsize=(10, 5))
    
    plt.plot(df['Zaman_Milisaniye'], df['Hiz_kmh'], label='Hız (km/h)', color='blue', marker='o')
    plt.plot(df['Zaman_Milisaniye'], df['Motor_Sicakligi_C'], label='Motor Sıcaklığı (°C)', color='red', linestyle='--', marker='x')
    
    plt.title(title)
    plt.xlabel("Zaman (ms)")
    plt.ylabel("Değerler")
    plt.legend()
    plt.grid(True)
    
    plt.show()