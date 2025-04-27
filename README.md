# Gestor de Tareas

Un sistema de línea de comandos para gestionar tareas pendientes con prioridades, fechas de vencimiento y filtros inteligentes.

---

## 📋 Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Requisitos](#requisitos)
5. [Instalación](#instalación)
6. [Uso](#uso)
7. [Ejemplos](#ejemplos)

---

## 📝 Descripción

Este proyecto implementa un gestor de tareas en Python con las siguientes funcionalidades:

- **Agregar tareas**: Título, descripción, fecha de vencimiento y prioridad.
- **Listar tareas**: Ordenadas por fecha de vencimiento.
- **Buscar tareas**: Por palabra clave en título o descripción.
- **Filtrar tareas**: Por prioridad (alta, media, baja).
- **Mostrar vencidas**: Tareas cuyo vencimiento es anterior a la fecha actual y no están completadas.
- **Marcar completadas**: Cambia el estado de una tarea a completada.
- **Eliminar tareas**: Por ID.
- **Persistencia**: Guardar y cargar tareas desde un archivo CSV entre ejecuciones.

---

## 🚀 Características

- **Interfaz CLI**: Menú interactivo en bucle.
- **Validaciones**: Fecha en formato `YYYY-MM-DD`, prioridad válida.
- **CSV Persistente**: Uso de `csv.DictReader` y `csv.DictWriter`.
- **Código modular**: Separación de responsabilidades en varios archivos.

---

## 🗂️ Estructura del Proyecto

```plaintext
gestor_tareas/
├── data/
│   └── tareas.csv           # Archivo CSV con las tareas (se crea automáticamente)
├── main.py                  # Punto de entrada: menú CLI
├── logica_tareas.py         # Funciones puras: CRUD, filtros y validaciones
├── persistencia.py          # Carga y guardado en CSV
├── utils.py                 # Utilidades: validación de fecha, prioridad, generación de ID y limpieza de pantalla
├── .gitignore
└── README.md
```

---

## ⚙️ Requisitos

- **Python** 3.11 o superior
- Módulos estándar: `csv`, `datetime`, `os`, `typing`

---

## 📥 Instalación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:carloswm/gestor_tareas.git
   cd gestor_tareas
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

---

## 💻 Uso

Ejecuta el programa principal:

```bash
python main.py
```

Sigue las opciones del menú:

1. Agregar tarea
2. Ver todas las tareas
3. Buscar tarea
4. Filtrar por prioridad
5. Mostrar vencidas
6. Marcar como completada
7. Eliminar tarea
8. Guardar y salir

El archivo `data/tareas.csv` se creará automáticamente la primera vez.

---

## 📊 Ejemplos

```plaintext
> 1  # Agregar tarea
Título: Estudiar matemáticas
Descripción: Repasar ecuaciones diferenciales
Fecha venc. (YYYY-MM-DD): 2025-05-10
Prioridad (alta/media/baja): alta
Tarea creada con ID 1

> 2  # Ver tareas
ID: 1 | [✘] Estudiar matemáticas | 🕒 2025-05-10 | Prioridad: alta

> 5  # Mostrar vencidas (suponiendo fecha > 2025-05-10)
ID: 1 | [✘] Estudiar matemáticas | 🕒 2025-05-10 | Prioridad: alta

> 6  # Marcar como completada
ID de tarea a marcar completada: 1
Marcada como completada.

> 8  # Guardar y salir
Guardado. ¡Hasta luego!
```

---

