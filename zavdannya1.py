import pathlib

path = pathlib.Path(r"C:/Users/W/Documents/vcode/hw-04/goit-algo-hw-04/salary_file.txt")

def total_salary(path):
    try:
        total = 0 
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                salary = int(parts[1].strip())
                total += int(salary)
                average = int(total / 2)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    
    except FileNotFoundError:
        print(f"Error: File not found")

total_salary(path)
