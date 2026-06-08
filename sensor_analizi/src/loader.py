import numpy as np
import pandas as pd

def load_sensor_data() -> pd.DataFrame:
    """Simüle edilmiş sensör verisini döndürür."""
    sensor_verisi = {
        'Zaman_Milisaniye': [100, 200, 300, 400, 500, 600, 700],
        'Hiz_kmh': [45, 50, np.nan, 55, 60, np.nan, 65],
        'Motor_Sicakligi_C': [88.5, 89.0, 89.2, 95.0, np.nan, 90.5, 91.0]
    }
    return pd.DataFrame(sensor_verisi)