import csv
import os
from datetime import datetime
from typing import Any, Dict, List

from logica_tareas import Tarea

CSV_FIELDS = ["id", "titulo", "descripcion", "fecha_vencimiento", "prioridad", "completada"]


def cargar_tareas(path: str = "data/tareas.csv") -> List[Tarea]:
    tareas: List[Tarea] = []
    # Si el archivo no existe, crearlo con cabecera
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
        return tareas

    # Si existe, leer las tareas
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["fecha_vencimiento"] = datetime.strptime(row["fecha_vencimiento"], "%Y-%m-%d").date()
            row["completada"] = row["completada"] == "True"
            tareas.append(row)
    return tareas


def guardar_tareas(tareas: List[Tarea], path: str = "data/tareas.csv") -> None:
    """Guarda las tareas en un CSV (sobrescribe archivo existente)."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for t in tareas:
            row = {
                **t,
                "fecha_vencimiento": t["fecha_vencimiento"].strftime("%Y-%m-%d"),
                "completada": str(t["completada"])
            }
            writer.writerow(row)
