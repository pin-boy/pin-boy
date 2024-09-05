import mpmath
import matplotlib.pyplot as plt

# Установка точности
mpmath.mp.dps = 1000000  # Устанавливаем 1 миллион знаков после запятой

# Вычисление числа Пи
pi_value = str(mpmath.mp.pi)

# Извлечение первых 1,000,000 знаков после запятой
pi_digits = pi_value[2:1000002]  # Пропускаем '3.'

# Сбор статистики
digit_count = {str(i): 0 for i in range(10)}
even_count = 0
odd_count = 0

for digit in pi_digits:
    digit_count[digit] += 1
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Подсчет процентов
total_digits = len(pi_digits)
percentages = {digit: (count / total_digits) * 100 for digit, count in digit_count.items()}

# Вывод результатов
print("Количество цифр:")
for digit, count in digit_count.items():
    print(f"{digit}: {count} ({percentages[digit]:.2f}%)")

print(f"\nЧетные цифры: {even_count}")
print(f"Нечетные цифры: {odd_count}")

# Визуализация данных
labels = list(digit_count.keys())
sizes = list(digit_count.values())

# Построение круговой диаграммы
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Равные оси для круга
plt.title('Распределение цифр в числе Пи (первые 1,000,000 знаков)')
plt.show()

# Построение столбчатой диаграммы
plt.figure(figsize=(10, 6))
plt.bar(labels, sizes, color='skyblue')
plt.xlabel('Цифры')
plt.ylabel('Количество')
plt.title('Количество каждой цифры в числе Пи (первые 1,000,000 знаков)')
plt.xticks(rotation=45)
plt.show()