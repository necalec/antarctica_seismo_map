import json

data = []

files = ['D:/diplom/antarctic_map/1904-1959.txt', 'D:/diplom/antarctic_map/1960-1969.txt', 'D:/diplom/antarctic_map/1970-1979.txt', 'D:/diplom/antarctic_map/1980-1989.txt', 'D:/diplom/antarctic_map/1990-1999.txt', 'D:/diplom/antarctic_map/2000-2009.txt', 'D:/diplom/antarctic_map/2010-2019.txt', 'D:/diplom/antarctic_map/2020-2023.txt']

num = 0
for j in range(0, 8):
    with open(files[j], 'r') as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split()
            if (float(elements[4]) <= -60) and (float(elements[7]) != 0.0):
                num = num + 1
                obj = {
                    "id": elements[0],
                    "code": elements[1],
                    "date": elements[2],
                    "time": elements[3],
                    "latitude": float(elements[4]),
                    "longitude": float(elements[5]),
                    "depth": elements[6],
                    "magnitude": float(elements[7]),
                    "N": elements[8]
                }
                data.append(obj)

print(num)

with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
