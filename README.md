# Vehicle Telemetry Data Cleansing & Analysis

This project is a fundamental data analytics pipeline designed to clean, structure, and visualize raw and corrupted vehicle sensor data (speed, temperature, etc.) using core data science methodologies.

## 🚀 Key Features
* **Vectorized Data Manipulation:** Leveraged `NumPy` array architecture instead of standard Python loops to ensure memory efficiency and high-speed processing.
* **Advanced Missing Data Management (Imputation):** Handled sensor dropouts (`NaN` values) by applying **Linear Interpolation** for speed data to preserve physical acceleration trends, and **Mean Imputation** for temperature to maintain the overall statistical distribution.
* **Data Visualization:** Generated comprehensive trend analysis graphs using `Matplotlib` to inspect data distribution before and after the cleansing process.

## 🛠️ Tech Stack
* Python 3
* NumPy
* Pandas
* Matplotlib

## 📦 Installation & Usage
```bash
pip install numpy pandas matplotlib
python main.py
