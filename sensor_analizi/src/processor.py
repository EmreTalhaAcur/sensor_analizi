import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Eksik verileri uygun matematiksel yöntemlerle doldurur."""
    # Orijinal veriyi bozmamak için kopyası üzerinde çalışmak iyi bir pratiktir
    df_cleaned = df.copy()
    
    # Hız için interpolasyon, sıcaklık için ortalama
    df_cleaned['Hiz_kmh'] = df_cleaned['Hiz_kmh'].interpolate()
    
    sicaklik_ortalamasi = df_cleaned['Motor_Sicakligi_C'].mean()
    df_cleaned['Motor_Sicakligi_C'] = df_cleaned['Motor_Sicakligi_C'].fillna(sicaklik_ortalamasi)
    
    return df_cleaned