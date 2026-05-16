import os
import json

#проверяю существует ли файл используя безопасный способ через os.path.join
path = os.path.join("C:/Users/user", "memory.json")
if os.path.exists(path):
    print("file exist")
    with open(path, "r", encoding = "utf-8") as f:
        memory = json.load(f)

else:
    memory = []        
    
print(memory)



#вношу измененияё
data = input("Enter new fact about yourself: ")

memory.append(data)

with open(path, "w", encoding = "utf-8") as f:
    json.dump(memory, f)

#проверка изменений
with open(path, "r", encoding = "utf-8") as f:
    memory = json.load(f)
print(memory)


