# Глобальная переменная для фрактального списка
fractal = [0, 2]
for i in range(3):
    # Добавление ссылки на сам список
    fractal.insert(i+1, fractal)

# Очистка чата
print(fractal[:])
