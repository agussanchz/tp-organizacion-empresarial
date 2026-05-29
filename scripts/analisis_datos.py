equipos = {}

with open("../datos/partidos.csv", "r") as archivo:
    next(archivo)

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

resultado = "Tabla de posiciones\n\n"

for equipo, puntos in equipos.items():
    resultado += f"{equipo}: {puntos} puntos\n"

print(resultado)

with open("../resultados/tabla_posiciones.txt", "w") as salida:
    salida.write(resultado)
