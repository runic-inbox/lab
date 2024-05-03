import csv

max_male, max_female, min_male, min_female = 0, 0, 200, 200  # Гарантированно заниженные/завышенные значения

with open('data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Age'] == '':
            continue  # Если возраст не указан, считать нечего.

        age = float(row['Age'])

        if row['Sex'] == 'male':
            max_male = max(max_male, age)
            min_male = min(min_male, age)

        elif row['Sex'] == 'female':
            max_female = max(max_female, age)
            min_female = min(min_female, age)

        else:
            print('Движение ЛГБТ признано экстремистским, и запрещено в РФ!')

print(f'Диапазон возрастов мужчин от {min_male} до {max_male}')
print(f'Диапазон возрастов женщин от {min_female} до {max_female}')
