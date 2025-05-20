import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.preprocessing.sequence import TimeseriesGenerator

# Load the data
df = pd.read_csv(r"/datasets/river_flow.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Prepare data
data = df.values
_data = data.reshape((-1))
split = int(0.8 * len(data))  # 80% for training
train_data = data[:split]
test_data = data[split:]

# Set look-back period
look_back = 20

# Create the TimeseriesGenerator
train_generator = TimeseriesGenerator(train_data, train_data, length=look_back, batch_size=16)
test_generator = TimeseriesGenerator(test_data, test_data, length=look_back, batch_size=1)

# Define the model
model = keras.Sequential([
    keras.layers.LSTM(50, activation='relu', input_shape=(look_back, 1)),
    keras.layers.Dense(1)
])

# Compile and fit the model
model.compile(optimizer='adam', loss='mse')
history = model.fit(train_generator, epochs=30, verbose=1)

prediction = model.predict(test_generator)

plt.plot(df.index[split + look_back:], test_data[look_back:], label = "реальні дані")
plt.plot(df.index[split + look_back:], prediction, label = "Прогноз")

def predict_future(days,model):
    future_predirect = data[-look_back:]
    for _ in range(days):
        x = future_predirect[-look_back:].reshape((1, look_back, 1))
        next_value = model.predict(x)[0][0]
        future_predirect = np.append(future_predirect, next_value)
    return future_predirect[-days:]

future_forecost = predict_future(30, model)
future_dates = pd.date_range(df.index[-1], periods = 31)[1:]

plt.plot(future_dates, future_forecost, label="31 день")
plt.legend()
plt.show()