import pathlib

path = pathlib.Path(r"C:/Users/W/Documents/vcode/hw-04/goit-algo-hw-04/cats_file.txt")

def get_cats_info(path):
    try:
        cat_list = []
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                data = {
                    "id": parts[0],
                    "age": parts[1],
                    "name": parts[2]
                }
                cat_list.append(data)
        return cat_list
    except FileNotFoundError:
        print(f"Error: File not found")

cats_info = get_cats_info(path)
print(cats_info)
