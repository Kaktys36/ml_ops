import numpy as np
import pandas as pd
import os

# Создание папок для хранения данных
os.makedirs('C:/Users/Kaktys/Desktop/1/data/train', exist_ok=True)
os.makedirs('C:/Users/Kaktys/Desktop/1/data/test', exist_ok=True)


# Функция для генерации данных
def generate_data(anomaly_prob=0.05, noise_std=0.5):
    np.random.seed(42)
    days = np.arange(1, 366)
    temperatures = np.sin(days / 365 * 2 * np.pi) * 20 + 15
    anomalies = np.random.choice([0, 1], size=len(days), p=[1 - anomaly_prob, anomaly_prob])
    temperatures[anomalies == 1] += np.random.normal(scale=noise_std, size=np.sum(anomalies))
    return days, temperatures


# Генерация данных для обучения и тестирования
train_days, train_temps = generate_data()
test_days, test_temps = generate_data()

# Сохранение данных в файлы
pd.DataFrame({'day': train_days, 'temperature': train_temps}).to_csv('C:/Users/Kaktys/Desktop/1/data/train/train_df.csv', index=False)
pd.DataFrame({'day': test_days, 'temperature': test_temps}).to_csv('C:/Users/Kaktys/Desktop/1/data/test/test_df.csv', index=False)
