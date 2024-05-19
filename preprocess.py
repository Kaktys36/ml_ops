from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных
train_data = pd.read_csv('C:/Users/Kaktys/Desktop/1/data/train/train_df.csv')
test_data = pd.read_csv('C:/Users/Kaktys/Desktop/1/data/test/test_df.csv')

# Предобработка данных
scaler = StandardScaler()
train_data['temperature'] = scaler.fit_transform(train_data[['temperature']])
test_data['temperature'] = scaler.transform(test_data[['temperature']])

# Сохранение предобработанных данных
train_data.to_csv('C:/Users/Kaktys/Desktop/1/data/train/train_df_prep.csv', index=False)
test_data.to_csv('C:/Users/Kaktys/Desktop/1/data/test/test_df_prep.csv', index=False)
