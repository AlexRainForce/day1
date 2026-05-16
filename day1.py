import os
import json
import sys

# Переводим путь на относительный (будет работать везде)
path = "memory.json"

if os.path.exists(path):
    print("Файл существует, читаем данные...")
    with open(path, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    print("Файл не найден, создаём новый список.")
    memory = []        
    
print("Текущая память:", memory)

# Безопасный ввод для пайплайна: берем из аргументов запуска или пишем дефолт
if len(sys.argv) > 1:
    data = sys.argv[1]
else:
    data = "Автоматический факт из пайплайна"

print(f"Добавляем новый факт: {data}")
memory.append(data)

# Сохраняем
with open(path, "w", encoding="utf-8") as f:
    json.dump(memory, f, ensure_ascii=False, indent=4)

# Проверка изменений
with open(path, "r", encoding="utf-8") as f:
    memory = json.load(f)
print("Обновленная память:", memory)
