import os
import re
import time
import datetime
import math

def find_txt_files(root_dir):
    txt_files = []

    # Recorre todas las carpetas y subcarpetas en el directorio raíz
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                txt_files.append(file_path)
    return txt_files




def search_pattern_in_files(file_paths, pattern):
    matching_files = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(pattern, content)
            if matches:
                matching_files.append((file_path, matches))

    return matching_files




# Directorio raíz para comenzar la búsqueda
start = time.time()
root_directory = 'C:\\Users\\lgonz\\Desktop\\python_udemy\\Dia_9\projrct_day_9\\Mi_Gran_Directorio'

txt_files = find_txt_files(root_directory)

# Patrón para buscar cadenas de caracteres que cumplan con el formato deseado
pattern = r'N[a-z]{3}-\d{5}'

matching_files = search_pattern_in_files(txt_files, pattern)

today_date = datetime.date.today()
date_formated = today_date.strftime("%d/%m/%Y")


# Imprime los resultados
print("---------------------------------------------------------------------")
print(f"Search Date: {date_formated}")
print("File\t\t\t\t\t\tSerial Nbr.")
for file_path, matches in matching_files:
    name_of_file = os.path.basename(file_path)
    print(f"{name_of_file}\t\t\t {matches[0]}")
print(f"Serial numbers found: {len(matching_files)}")
end = time.time()
rounded_duration = math.ceil(end - start)
print(f"Search duration: {rounded_duration} sec.")
