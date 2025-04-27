Gestor de Tareas

Un sistema de línea de comandos para gestionar tareas pendientes con prioridades, fechas de vencimiento y filtros inteligentes.

📋 Tabla de Contenidos

Descripción

Características

Estructura del Proyecto

Requisitos

Instalación

Uso

Ejemplos


📝 Descripción

Este proyecto implementa un gestor de tareas en Python que permite:

Agregar tareas con título, descripción, fecha de vencimiento y prioridad.

Listar tareas ordenadas por fecha.

Buscar y filtrar tareas por palabra clave o prioridad.

Identificar tareas vencidas.

Marcar tareas como completadas.

Eliminar tareas por ID.

Guardar y cargar tareas desde un archivo CSV para persistencia entre ejecuciones.

🚀 Características

Interfaz CLI: Menú interactivo en bucle hasta que el usuario decida salir.

Validaciones: Formato de fecha (YYYY-MM-DD) y prioridad (alta, media, baja).

Persistencia CSV: Uso de csv.DictReader/DictWriter.

Código modular: Separación de lógica, persistencia y utilidades.

Tests unitarios: Con pytest para funciones de lógica y persistencia.

🗂️ Estructura del Proyecto

gestor_tareas/
├── data/
│   └── tareas.csv           # Archivo CSV con las tareas (se crea automáticamente)
├── main.py                  # Punto de entrada y menú CLI
├── logica_tareas.py         # Funciones puras: CRUD y filtros
├── persistencia.py          # Carga y guardado en CSV
├── utils.py                 # Helpers: validaciones y utilidades
├── .gitignore
└── README.md

⚙️ Requisitos

Python 3.8 o superior

Módulos estándar: csv, datetime, os, typing

Para pruebas opcionales: pytest

📥 Instalación

Clona el repositorio:

git clone git@github.com:carloswm/gestor_tareas.git
cd gestor_tareas

Crea un entorno virtual y actívalo:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

Instala dependencias (solo pytest si vas a ejecutar tests):

pip install pytest

💻 Uso

Ejecuta el programa principal:

python main.py

Sigue las opciones del menú para agregar, listar, buscar, filtrar, marcar y eliminar tareas. El archivo data/tareas.csv se crea automáticamente la primera vez.

📊 Ejemplos

1. Agregar tarea
2. Ver todas las tareas
3. Buscar tarea
4. Filtrar por prioridad
5. Mostrar vencidas
6. Marcar como completada
7. Eliminar tarea
8. Guardar y salir
> 1
Título: Estudiar matemáticas
Descripción: Repasar ecuaciones diferenciales
Fecha venc. (YYYY-MM-DD): 2025-05-10
Prioridad (alta/media/baja): alta
Tarea creada con ID 1

📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.