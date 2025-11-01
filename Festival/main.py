import time
from artistas import Cantante, DJ, Banda

def iniciar_festival(lista_artistas):
    print("\n" + "="*40)
    print("      ¡EL FESTIVAL VA A COMENZAR!")
    print("="*40)
    
    for artista in lista_artistas:
        # 1. Se presenta
        artista.presentarse()
        time.sleep(1)
        
        # 2. Actúa
        artista.actuar()
        time.sleep(1)

        # 3. Se despide
        artista.despedirse()
        
        print("\n Fin de la actuación ")
        print("-" * 30)
        time.sleep(2)

def main():
    print("------Preparativos del Festival de Música------")
    lista_artistas_festival = []

    while True:
        try:
            num_artistas = int(input("¿Cuántos artistas (o grupos) se presentarán?: "))
            if num_artistas > 0:
                break
            else:
                print("Error: Debes ingresar al menos 1 artista.")
        except ValueError:
            print("Error: Ingresa un número válido.")

    for i in range(num_artistas):
        print(f"\n--- Datos del Artista {i+1} ---")
        
        tipo_artista = ""
        while tipo_artista not in ["1", "2", "3"]:
            tipo_artista = input("Tipo (1: Cantante, 2: DJ, 3: Banda): ")
            if tipo_artista not in ["1", "2", "3"]:
                print("Opción no válida. Elige 1, 2 o 3.")

        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        
        popularidad = 0
        while not (1 <= popularidad <= 100):
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if not (1 <= popularidad <= 100):
                    print("Error: La popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Error: Ingresa un número válido.")

        if tipo_artista == "1":
            cancion = input("Canción más popular: ")
            artista_nuevo = Cantante(nombre, genero, popularidad, cancion)
            
        elif tipo_artista == "2":
            estilo = input("Estilo (ej. Techno, House, EDM): ")
            artista_nuevo = DJ(nombre, genero, popularidad, estilo)
            
        elif tipo_artista == "3":
            integrantes = 0
            while integrantes <= 0:
                try:
                    integrantes = int(input("Número de integrantes: "))
                    if integrantes <= 0:
                        print("Error: Una banda debe tener al menos 1 integrante.")
                except ValueError:
                    print("Error: Ingresa un número válido.")
            artista_nuevo = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas_festival.append(artista_nuevo)

    iniciar_festival(lista_artistas_festival)
    
    print("\n¡El festival ha sido éxitoso Gracias por venir!")

if __name__ == "__main__":
    main()