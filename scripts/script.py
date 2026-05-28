equipos = {}

with open("../datos/datos.txt", "r") as archivo:
    for linea in archivo:
        local, goles_local, visitante, goles_visitante = linea.strip().split(",")

        goles_local = int(goles_local)
        goles_visitante = int(goles_visitante)

        if local not in equipos:
            equipos[local] = 0

        if visitante not in equipos:
            equipos[visitante] = 0

        if goles_local > goles_visitante:
            equipos[local] += 3

        elif goles_visitante > goles_local:
            equipos[visitante] += 3

        else:
            equipos[local] += 1
            equipos[visitante] += 1

print("Tabla de posiciones:")

for equipo, puntos in equipos.items():
    print(equipo, puntos)
