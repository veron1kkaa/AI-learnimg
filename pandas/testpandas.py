import pandas as pd


file_path = '/content/[ПР №3] zfpo_rivne_region (3).xlsx'
data_admissions = pd.read_excel(file_path, sheet_name='Вступ групи')
data_education = pd.read_excel(file_path, sheet_name='Здобувачі')


applicants_by_college = data_admissions.groupby('Заклад освіти')['Вступники'].sum()

students_by_college = data_education.groupby('Заклад освіти')['Здобувачів'].sum()

results = pd.DataFrame({'Вступники': applicants_by_college, 'Здобувачів': students_by_college})

print(results)


# Зчитуємо таблиці
data_education = pd.read_excel('/content/[ПР №3] zfpo_rivne_region (3).xlsx', sheet_name='Здобувачі')
data_admissions = pd.read_excel('/content/[ПР №3] zfpo_rivne_region (3).xlsx', sheet_name='Вступ групи')

# Зливаємо таблиці за колонкою 'Заклад освіти'
merged_data = pd.merge(data_admissions, data_education, on='Заклад освіти')

# Обчислюємо відсоток вступників від загальної кількості здобувачів
merged_data['Відсоток вступників'] = (merged_data['Вступники'] / (merged_data['Вступники'] + merged_data['Здобувачів'])) * 100

# Форматуємо відсоток з двома десятковими знаками
merged_data['Відсоток вступників'] = merged_data['Відсоток вступників'].map('{:.0f}%'.format)

# Виводимо результат
print(merged_data[['Заклад освіти', 'Відсоток вступників']])
