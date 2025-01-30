import pathlib

path = pathlib.Path(r"C:/Users/W/Documents/vcode/hw-04/goit-algo-hw-04/salary_file.txt")

def total_salary(path):
    try:
        total = 0.0
        count = 0
        
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                salary = float(parts[1].strip())
                total += salary
                count += 1
        
        if count > 0:
            average = total / count
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        return total, average
    
    except FileNotFoundError:
        print(f"Error: File not found")
total_salary(path)
