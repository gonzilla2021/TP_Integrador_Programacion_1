# Importar módulos necesarios
import csv  # Para leer y escribir archivos CSV
import sys  # Para funcionalidades del sistema como salir del programa
import time  # Para medir tiempos de ejecución

def cargar_peliculas():
    """Carga las películas desde el archivo IMBD.csv"""
    peliculas = []  # Lista para almacenar todas las películas
    
    try:
        # Abrir el archivo CSV con codificación UTF-8 (para manejar caracteres especiales)
        with open('IMBD.csv', 'r', encoding='utf-8') as archivo:
            # Crear un lector de CSV que mapea cada fila a un diccionario
            lector = csv.DictReader(archivo)
            
            # Mostrar las columnas disponibles en el archivo
            print("📝 Columnas encontradas en el CSV:", lector.fieldnames)
            
            # Procesar cada fila del archivo CSV
            for fila in lector:
                # Mostrar datos de la primera fila para verificación
                if len(peliculas) == 0:
                    print("🔍 Primera fila (para verificar datos):")
                    for key, value in fila.items():
                        print(f"  {key}: '{value}'")
                
                try:
                    # Procesamiento del año - extraer solo los 4 dígitos numéricos
                    year_str = str(fila.get('year', '')).strip()
                    if year_str.isdigit() and len(year_str) == 4:
                        fila['year'] = int(year_str)
                    else:
                        # Extraer dígitos de cadenas como "(1994)" o "1994-01-01"
                        digits = ''.join([c for c in year_str if c.isdigit()])
                        fila['year'] = int(digits[:4]) if len(digits) >= 4 else 0
                    
                    # Procesamiento del rating - manejar diferentes formatos numéricos
                    rating_str = str(fila.get('rating', '')).strip()
                    if rating_str.replace('.', '').replace(',', '').isdigit():
                        fila['rating'] = float(rating_str.replace(',', '.'))  # Manejar decimales con coma
                    else:
                        fila['rating'] = 0.0
                    
                    # Procesamiento de votos - eliminar comas en números grandes
                    votes_str = str(fila.get('votes', '')).strip()
                    if votes_str.replace(',', '').isdigit():
                        fila['votes'] = int(votes_str.replace(',', ''))
                    else:
                        fila['votes'] = 0
                        
                except (ValueError, AttributeError) as e:
                    # Manejar errores en la conversión de datos
                    print(f"⚠️  Error convirtiendo datos en fila {len(peliculas)+1}: {e}")
                    fila['year'] = 0
                    fila['rating'] = 0.0
                    fila['votes'] = 0
                
                # Agregar la película procesada a la lista
                peliculas.append(fila)
        
        # Estadísticas de carga exitosa
        print(f"✅ Se cargaron {len(peliculas)} películas desde IMBD.csv")
        
        # Calcular y mostrar estadísticas de datos válidos
        años_validos = sum(1 for p in peliculas if p['year'] > 0)
        print(f"📊 Años válidos encontrados: {años_validos}/{len(peliculas)}")
        
        # Mostrar rango de años si hay datos válidos
        if años_validos > 0:
            años_unicos = sorted(set(p['year'] for p in peliculas if p['year'] > 0))
            print(f"📅 Rango de años encontrados: {min(años_unicos)} - {max(años_unicos)}")
            print("Ejemplos de años:", años_unicos[:10], "...")
        
        # Mostrar ejemplos de datos para diagnóstico
        print("\n🔍 Ejemplos de películas con años válidos:")
        for p in [p for p in peliculas[:20] if p['year'] > 0][:3]:
            print(f"  {p['title']} - Año: {p['year']}")
        
        print("\n⚠️  Ejemplos de películas SIN año válido:")
        for p in [p for p in peliculas[:20] if p['year'] == 0][:3]:
            print(f"  {p['title']} - Valor original: '{p.get('year', '')}'")
        
        return peliculas
        
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'IMBD.csv'")
        print("   Asegúrate de que el archivo esté en el mismo directorio que este programa")
        return None
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {str(e)}")
        return None

def mostrar_peliculas(peliculas, limite=10):
    """Muestra las películas en formato de tabla con límite opcional"""
    if not peliculas:
        print("No hay películas para mostrar.")
        return
    
    # Encabezado de la tabla
    print(f"\n{'='*110}")
    print(f"Mostrando {min(len(peliculas), limite)} de {len(peliculas)} películas:")
    print(f"{'='*110}")
    print(f"{'#':<3} {'TÍTULO':<40} {'AÑO':<6} {'GÉNERO':<18} {'RATING':<8} {'VOTOS':<12}")
    print("-" * 110)
    
    # Mostrar cada película con formato alineado
    for i, p in enumerate(peliculas[:limite]):
        # Acortar campos largos para mejor visualización
        titulo = p['title'][:39] + '...' if len(p['title']) > 39 else p['title']
        año = str(p['year']) if p['year'] > 0 else 'N/A'
        genero = p['genre'][:17] + '...' if len(p['genre']) > 17 else p['genre']
        rating = f"{p['rating']:.1f}" if p['rating'] > 0 else 'N/A'
        votos = f"{p['votes']:,}" if p['votes'] > 0 else 'N/A'
        
        # Imprimir fila formateada
        print(f"{i+1:<3} {titulo:<40} {año:<6} {genero:<18} {rating:<8} {votos:<12}")
    
    # Indicador si hay más películas que el límite mostrado
    if len(peliculas) > limite:
        print(f"\n... y {len(peliculas) - limite} películas más.")

# ===================== ALGORITMOS DE ORDENAMIENTO =====================

def bubble_sort_year(peliculas):
    """Ordena películas por año usando Bubble Sort"""
    pelis_copia = peliculas.copy()  # Trabajar sobre una copia
    n = len(pelis_copia)
    
    print("🔄 Ejecutando Bubble Sort por año...")
    inicio = time.time()  # Iniciar cronómetro
    
    # Algoritmo Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if pelis_copia[j]['year'] < pelis_copia[j+1]['year']:  # Orden descendente
                pelis_copia[j], pelis_copia[j+1] = pelis_copia[j+1], pelis_copia[j]
    
    # Mostrar tiempo de ejecución
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    # Mostrar resultados
    print("\n🔄 Películas ordenadas por AÑO (Bubble Sort - Descendente):")
    mostrar_peliculas(pelis_copia)

def selection_sort_rating(peliculas):
    """Ordena películas por rating usando Selection Sort"""
    pelis_copia = peliculas.copy()
    n = len(pelis_copia)
    
    print("⭐ Ejecutando Selection Sort por rating...")
    inicio = time.time()
    
    # Algoritmo Selection Sort
    for i in range(n):
        max_idx = i  # Asumir que el actual es el máximo
        for j in range(i+1, n):
            if pelis_copia[j]['rating'] > pelis_copia[max_idx]['rating']:
                max_idx = j  # Encontrar el máximo real
        
        # Intercambiar el máximo encontrado con la posición actual
        pelis_copia[i], pelis_copia[max_idx] = pelis_copia[max_idx], pelis_copia[i]
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    print("\n⭐ Películas ordenadas por RATING (Selection Sort - Descendente):")
    mostrar_peliculas(pelis_copia)

def insertion_sort_genre(peliculas):
    """Ordena películas por género usando Insertion Sort"""
    pelis_copia = peliculas.copy()
    
    print("🎭 Ejecutando Insertion Sort por género...")
    inicio = time.time()
    
    # Algoritmo Insertion Sort
    for i in range(1, len(pelis_copia)):
        key = pelis_copia[i]  # Elemento a insertar
        j = i - 1
        
        # Mover elementos mayores hacia la derecha
        while j >= 0 and pelis_copia[j]['genre'].lower() > key['genre'].lower():
            pelis_copia[j + 1] = pelis_copia[j]
            j -= 1
        
        # Insertar el elemento en su posición correcta
        pelis_copia[j + 1] = key
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    print("\n🎭 Películas ordenadas por GÉNERO (Insertion Sort - Alfabético):")
    mostrar_peliculas(pelis_copia)

def quick_sort_rating(peliculas):
    """Ordena películas por rating usando Quick Sort"""
    def quicksort(arr):
        """Función recursiva de Quick Sort"""
        if len(arr) <= 1:  # Caso base
            return arr
        
        pivot = arr[len(arr) // 2]['rating']  # Pivote del medio
        left = [x for x in arr if x['rating'] > pivot]    # Mayores que pivote
        middle = [x for x in arr if x['rating'] == pivot] # Iguales al pivote
        right = [x for x in arr if x['rating'] < pivot]   # Menores que pivote
        
        return quicksort(left) + middle + quicksort(right)  # Combinar resultados
    
    print("⚡ Ejecutando Quick Sort por rating...")
    inicio = time.time()
    
    pelis_ordenadas = quicksort(peliculas.copy())
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    print("\n⚡ Películas ordenadas por RATING (Quick Sort - Descendente):")
    mostrar_peliculas(pelis_ordenadas)

# ===================== ALGORITMOS DE BÚSQUEDA =====================

def busqueda_lineal_titulo(peliculas):
    """Busca películas por título usando búsqueda lineal"""
    titulo = input("Ingrese el título a buscar: ").strip().lower()
    encontradas = []
    
    print(f"🔍 Buscando películas con '{titulo}' en el título...")
    inicio = time.time()
    
    # Búsqueda lineal - revisar cada elemento
    for pelicula in peliculas:
        if titulo in pelicula['title'].lower():
            encontradas.append(pelicula)
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    if encontradas:
        print(f"\n🔍 Se encontraron {len(encontradas)} películas con '{titulo}' en el título:")
        mostrar_peliculas(encontradas)
    else:
        print(f"❌ No se encontraron películas con '{titulo}' en el título")

def busqueda_lineal_genero(peliculas):
    """Busca películas por género usando búsqueda lineal"""
    genero = input("Ingrese el género a buscar: ").strip().lower()
    encontradas = []
    
    print(f"🎭 Buscando películas del género '{genero}'...")
    inicio = time.time()
    
    for pelicula in peliculas:
        if genero in pelicula['genre'].lower():
            encontradas.append(pelicula)
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    if encontradas:
        print(f"\n🎭 Se encontraron {len(encontradas)} películas del género '{genero}':")
        mostrar_peliculas(encontradas)
    else:
        print(f"❌ No se encontraron películas del género '{genero}'")

def busqueda_binaria_year(peliculas):
    """Busca películas por año usando búsqueda binaria"""
    try:
        año = int(input("Ingrese el año a buscar: "))
    except ValueError:
        print("❌ Por favor ingrese un año válido (número entero).")
        return
    
    print(f"📅 Buscando películas del año {año} usando búsqueda binaria...")
    inicio = time.time()
    
    # Primero ordenar por año (requisito para búsqueda binaria)
    pelis_ordenadas = sorted(peliculas, key=lambda x: x['year'])
    encontradas = []
    low, high = 0, len(pelis_ordenadas) - 1
    
    # Algoritmo de búsqueda binaria
    while low <= high:
        mid = (low + high) // 2  # Punto medio
        
        if pelis_ordenadas[mid]['year'] == año:
            # Encontramos una coincidencia
            encontradas.append(pelis_ordenadas[mid])
            
            # Buscar coincidencias adyacentes (mismo año)
            i = mid - 1
            while i >= 0 and pelis_ordenadas[i]['year'] == año:
                encontradas.append(pelis_ordenadas[i])
                i -= 1
            
            i = mid + 1
            while i < len(pelis_ordenadas) and pelis_ordenadas[i]['year'] == año:
                encontradas.append(pelis_ordenadas[i])
                i += 1
            break
            
        elif pelis_ordenadas[mid]['year'] < año:
            low = mid + 1  # Buscar en mitad superior
        else:
            high = mid - 1  # Buscar en mitad inferior
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos (incluye ordenamiento)")
    
    if encontradas:
        print(f"\n📅 Se encontraron {len(encontradas)} películas del año {año}:")
        mostrar_peliculas(encontradas)
    else:
        print(f"❌ No se encontraron películas del año {año}")

def mostrar_estadisticas(peliculas):
    """Muestra estadísticas generales del dataset de películas"""
    if not peliculas:
        print("❌ No hay películas cargadas para mostrar estadísticas.")
        return
    
    print(f"\n📊 ESTADÍSTICAS DEL DATASET:")
    print(f"{'='*60}")
    print(f"Total de películas: {len(peliculas)}")
    
    # Estadísticas de ratings
    ratings = [p['rating'] for p in peliculas if p['rating'] > 0]
    if ratings:
        print(f"Rating promedio: {sum(ratings)/len(ratings):.2f}")
        print(f"Rating más alto: {max(ratings)}")
        print(f"Rating más bajo: {min(ratings)}")
    else:
        print("No hay ratings válidos en el dataset")
    
    # Estadísticas de años
    años = [p['year'] for p in peliculas if p['year'] > 0]
    if años:
        print(f"Año más antiguo: {min(años)}")
        print(f"Año más reciente: {max(años)}")
    else:
        print("No hay años válidos en el dataset")
    
    # Análisis de géneros
    generos = {}
    for p in peliculas:
        genero = p['genre'].split(',')[0].strip()  # Tomar solo el primer género
        generos[genero] = generos.get(genero, 0) + 1
    
    # Top 5 géneros más comunes
    print(f"\nTop 5 géneros más comunes:")
    for genero, cantidad in sorted(generos.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {genero}: {cantidad} películas")

def mostrar_ayuda():
    """Muestra información sobre los algoritmos implementados"""
    print(f"\n📚 INFORMACIÓN SOBRE ALGORITMOS:")
    print(f"{'='*70}")
    
    print("\n🔄 ALGORITMOS DE ORDENAMIENTO:")
    print("• Bubble Sort: O(n²)")
    print("  - Compara elementos adyacentes e intercambia si están desordenados")
    print("  - Simple pero lento para datasets grandes")
    
    print("\n• Selection Sort: O(n²)")
    print("  - Encuentra el mínimo/máximo y lo coloca en su posición")
    print("  - Hace menos intercambios que Bubble Sort")
    
    print("\n• Insertion Sort: O(n²)")
    print("  - Construye la lista ordenada elemento por elemento")
    print("  - Eficiente para datasets pequeños o parcialmente ordenados")
    
    print("\n• Quick Sort: O(n log n) promedio, O(n²) peor caso")
    print("  - Divide y vencerás usando un elemento pivote")
    print("  - Muy eficiente para datasets grandes")
    
    print("\n🔍 ALGORITMOS DE BÚSQUEDA:")
    print("• Búsqueda Lineal: O(n)")
    print("  - Examina cada elemento secuencialmente")
    print("  - Funciona con datos ordenados y desordenados")
    
    print("\n• Búsqueda Binaria: O(log n)")
    print("  - Divide el espacio de búsqueda por la mitad en cada paso")
    print("  - Requiere que los datos estén ordenados")

def main():
    """Función principal que maneja el menú interactivo"""
    print("🎬 SISTEMA DE PELÍCULAS IMDB")
    print("="*60)
    
    # Cargar datos al iniciar
    peliculas = cargar_peliculas()
    
    if peliculas is None:
        print("❌ No se pudieron cargar los datos. Cerrando programa.")
        sys.exit(1)
    
    # Menú interactivo
    while True:
        print(f"\n{'='*60}")
        print("MENÚ PRINCIPAL")
        print("="*60)
        
        # Opciones de visualización
        print("\n📋 VISUALIZACIÓN:")
        print("1. Mostrar todas las películas")
        print("2. Estadísticas del dataset")
        
        # Opciones de ordenamiento
        print("\n🔄 ORDENAMIENTO:")
        print("3. Ordenar por año (Bubble Sort)")
        print("4. Ordenar por rating (Selection Sort)")
        print("5. Ordenar por género (Insertion Sort)")
        print("6. Ordenar por rating (Quick Sort)")
        
        # Opciones de búsqueda
        print("\n🔍 BÚSQUEDA:")
        print("7. Buscar por título")
        print("8. Buscar por género")
        print("9. Buscar por año (Búsqueda Binaria)")
        
        # Ayuda y salida
        print("\n❓ AYUDA:")
        print("10. Información sobre algoritmos")
        print("11. Salir")
        
        opcion = input("\nSeleccione una opción (1-11): ").strip()
        
        if opcion == "1":
            limite = input("¿Cuántas películas mostrar? (Enter para 10): ").strip()
            limite = int(limite) if limite.isdigit() else 10
            mostrar_peliculas(peliculas, limite)
        elif opcion == "2":
            mostrar_estadisticas(peliculas)
        elif opcion == "3":
            bubble_sort_year(peliculas)
        elif opcion == "4":
            selection_sort_rating(peliculas)
        elif opcion == "5":
            insertion_sort_genre(peliculas)
        elif opcion == "6":
            quick_sort_rating(peliculas)
        elif opcion == "7":
            busqueda_lineal_titulo(peliculas)
        elif opcion == "8":
            busqueda_lineal_genero(peliculas)
        elif opcion == "9":
            busqueda_binaria_year(peliculas)
        elif opcion == "10":
            mostrar_ayuda()
        elif opcion == "11":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida. Por favor seleccione un número del 1 al 11.")

if __name__ == "__main__":
    main()