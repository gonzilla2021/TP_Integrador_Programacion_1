TECNICATURA UNIVERSITARIA EN PROGRAMACION

TP Integrador de Programacion 1 TUP "Algoritmos de Busqueda y Ordenamiento"

Alumnos: Buchek Lautaro y Castellini Gonzalo


Sistema de Películas IMDB 🎬
Un proyecto Python que implementa algoritmos de búsqueda y ordenamiento para analizar datos de películas de IMDB, mostrando su rendimiento y eficiencia.


Descripción del Proyecto 📌
Este sistema permite:
✅ Cargar datos de películas desde un archivo CSV (título, año, género, rating, votos).
✅ Ordenar películas por año, rating o género usando distintos algoritmos.
✅ Buscar películas por título, género o año.
✅ Analizar estadísticas del dataset (ratings promedio, años, géneros más comunes).

Características ✨
  Interfaz de consola interactiva con menú de opciones.

  Medición de tiempo para comparar la eficiencia de algoritmos.

  Manejo robusto de datos (años en diferentes formatos, ratings con decimales).

  Visualización clara en formato de tabla.


Instalación y Uso ⚙️
  Requisitos
    Python 3.8+
  Modulos
    Sys
    Time
    Csv


Algoritmos Implementados 🧠
  Algoritmo	Tipo	Uso en el Proyecto	Complejidad
  Bubble Sort	Ordenamiento	Ordenar películas por año (descendente)	O(n²)
  Selection Sort	Ordenamiento	Ordenar películas por rating (descendente)	O(n²)
  Insertion Sort	Ordenamiento	Ordenar películas por género (A-Z)	O(n²)
  Quick Sort	Ordenamiento	Ordenar películas por rating (descendente)	O(n log n)
  Búsqueda Lineal	Búsqueda	Buscar por título o género	O(n)
  Búsqueda Binaria	Búsqueda	Buscar películas por año	O(log n)


Reflexiones del Equipo 💭
  Desafíos Técnicos
  Procesamiento de datos: Limpiar y normalizar años en diferentes formatos (ej. "1994", "(2001)", "2010-05-12").

  Rendimiento: El Bubble Sort fue significativamente más lento en datasets grandes (>10,000 películas).

  Experiencia de usuario: Mejoramos la presentación de resultados con tablas formateadas.

  Aprendizajes
  Los algoritmos de ordenamiento eficiente (como Quick Sort) marcan la diferencia en datasets grandes.

  La búsqueda binaria es rápida, pero requiere datos ordenados previamente.
    
  Git puede generar warnings por formatos de línea (LF/CRLF), pero no afecta la funcionalidad.



🎉 ¡Disfruta explorando el mundo del cine con datos reales!

PONER EL ENLACE AL VIDEO DE YOUTUBE


