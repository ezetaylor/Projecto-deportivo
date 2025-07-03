import os
import pandas as pd

def importar_jugadores_csv(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"⚠ No se encontró el archivo '{nombre_archivo}' en: {os.getcwd()}")
        return []

    try:
        df = pd.read_csv(nombre_archivo, delimiter=';')  

        jugadores = []

        for _, fila in df.iterrows():
            jugador = {
                "nombre": fila["nombre"],
                "peso": float(fila["peso"]),
                "altura": float(fila["altura"]),
                "edad": int(fila["edad"]),
                "distancia": int(fila["distancia"]),
                "tiempo": int(fila["tiempo"]),
            }
            jugadores.append(jugador)

        return jugadores

    except Exception as e:
        print(f"⚠ Error al leer el archivo: {e}")
        return []

def lista_alumnos():
    alumnos=[]
    cant=int(input("Cantidad de alumnos a agregar: "))
    for i in range(cant):
        print(f"Alumno numero: {i+1}")
        nombre=str(input("Nombre: "))
        peso=float(input("Peso: "))
        altura=float(input("Altura: "))
        edad=int(input("Edad: "))
        distancia=int(input("Ultima distancia recorrida en metros: "))
        tiempo=int(input("Tiempo de distancia recorrida en segundos: "))

        alumno={
            "nombre": nombre,
            "peso":peso,
            "altura": altura,
            "edad": edad,
            "distancia":distancia,
            "tiempo": tiempo,
        }

        alumnos.append(alumno)
        os.system('cls')
    return alumnos

def prom_vel(lista):
    acum=0
    for vel in lista:
        acum=acum+vel
    prom=round(acum/(len(lista)),2)
    return prom

def top_3(lista):
    ordenados = sorted(lista, key=lambda x: x['velocidad'], reverse=True)
    print("\n")
    print("TOP 3 MAS VELOCES:\n")
    for list in ordenados[:3]:
        print(f"{list['nombre']} - Velocidad: {list['velocidad']}m/s")

def mostrar_alumnos(lista):
    print("Lista de alumnos: \n")
    for list in lista:
        print(f"Nombre: {list['nombre']} - Peso: {list['peso']} - Altura: {list['altura']} - Edad: {list['edad']}\n")

def filtrar_por_edad(lista):
    edad_min = int(input("\nMostrar alumnos con edad mayor o igual a: "))
    print(f"Alumnos mayores o iguales a {edad_min} años:\n")
    for alumno in lista:
        if alumno['edad'] >= edad_min:
            print(f"{alumno['nombre']} - Edad: {alumno['edad']}")

#-------------------------------------------Programa principal -------------------------------------

print("Cómo querés cargar los datos?")
print("1. Ingresar alumnos manualmente")
print("2. Importar desde archivo CSV")

opcion = input("Opción (1 o 2): ")

if opcion == "1":
    alumnos = lista_alumnos()
else:
    archivo = input("Nombre del archivo CSV (ej: jugadores.csv): ").strip()
    alumnos = importar_jugadores_csv(archivo)

print("\n")
mostrar_alumnos(alumnos)

imcs=[]
velocidades=[]
#Recorremos cada alumno para conseguir su velocidad y su IMC
for alumno in alumnos:
    peso=alumno['peso']
    altura=alumno['altura']
    distancia=alumno['distancia']
    tiempo=alumno['tiempo']

    vel=round(distancia/tiempo,2)
    velocidades.append(vel)
    alumno['velocidad']=vel

    IMC=round(peso / (altura * altura),2)
    imcs.append(IMC)
    alumno['IMC'] = IMC

    #Segun OMS, sobrepeso es mayor a 25
    if IMC >= 25:
        print(f"{alumno['nombre']} tiene un IMC de {IMC} - Riesgo de sobrepeso u obesidad.\n")

#Alumno mas rapido
maximo = max(velocidades)
indice=velocidades.index(maximo)
print("El alumno mas rapido es: ", alumnos[indice]['nombre'])

#Promedio de velocidad
promedio=prom_vel(velocidades)
print(f"El promedio de velocidad es de: {promedio}m/s")

#Top 3 mejores velocidades
top_3(alumnos)

#Mostrar resumen de IMC y velocidad
print("\n📊 Resumen final de alumnos con IMC y velocidad:")
for alumno in alumnos:
    print(f"{alumno['nombre']} - IMC: {alumno['IMC']} - Velocidad: {alumno['velocidad']} m/s")

#Filtro de alumnos por edad
filtrar_por_edad(alumnos)

