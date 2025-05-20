import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Зчитування даних з файлу
with open(r"C:\Users\ACER\Desktop\update repository .txt", 'r', encoding='utf-8') as file:
    texts = file.readlines()

# Мітки для текстів (припустимо, що міток недостатньо)
labels = np.array([1, 0, 1, 0])  # 1 - позитивний, 0 - негативний

# Перевірка кількості текстів та міток
if len(texts) != len(labels):
    # Повторення міток для всіх текстів
    labels = np.tile(labels, int(np.ceil(len(texts) / len(labels))))[:len(texts)]

# Векторизація текстів
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()

# Створення моделі
model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dense(1, activation='sigmoid')
])

# Компіляція моделі
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Тренування моделі
history = model.fit(X, labels, epochs=10, verbose=1)

# Візуалізація функції втрат
plt.plot(history.history['loss'])
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.savefig(r'C:\Users\ACER\Desktop\training_loss_plot.png', dpi=300, bbox_inches='tight')
plt.show()