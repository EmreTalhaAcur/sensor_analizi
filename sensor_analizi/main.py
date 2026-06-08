from src.loader import load_sensor_data
from src.processor import clean_data
from src.visualizer import plot_telemetry
from src.config import PLOT_TITLE

def main():
    # 1. Veriyi Oku
    print("Veri yükleniyor...")
    raw_df = load_sensor_data()
    
    # 2. Veriyi Temizle
    print("Veri temizleniyor...")
    cleaned_df = clean_data(raw_df)
    
    # 3. Sonucu Görselleştir
    print("Görselleştirme başlatılıyor...")
    plot_telemetry(cleaned_df, PLOT_TITLE)

if __name__ == "__main__":
    main()