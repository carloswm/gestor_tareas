from datetime import date
from typing import Any, Dict, List

from utils import generar_id, validar_fecha, validar_prioridad

Tarea = Dict[str, Any]

def agregar_tarea(tareas: List[Tarea], titulo: str, descripcion: str, fecha_str: str, prioridad: str) -> Tarea:

    fecha_vto = validar_fecha(fecha_str)
    prio = validar_prioridad(prioridad)
    nueva = {
        "id": generar_id(tareas),
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_vencimiento": fecha_vto,
        "prioridad": prio,
        "completada": False
    }
    tareas.append(nueva)
    return nueva

def eliminar_tarea(tareas: List[Tarea], tarea_id: int) -> bool:
    for i, t in enumerate(tareas):
        if t["id"] == tarea_id:
            del tareas[i]
            return True
    return False

def marcar_completada(tareas: List[Tarea], tarea_id: int) -> bool:
    for t in tareas:
        if t["id"] == tarea_id:
            t["completada"] = True
            return True
    return False

def listar_tareas(tareas: List[Tarea]) -> None:
    """Muestra por pantalla todas las tareas ordenadas por fecha ascendente."""
    for t in sorted(tareas, key=lambda x: x["fecha_vencimiento"]):
        estado = "✔" if t["completada"] else "✘"
        print(f'ID: {t["id"]} | [{estado}] {t["titulo"]} | 🕒 {t["fecha_vencimiento"]} | Prioridad: {t["prioridad"]}')

def buscar_tareas(tareas: List[Tarea], palabra: str) -> List[Tarea]:
    p = palabra.lower()
    return [t for t in tareas if p in t["titulo"].lower() or p in t["descripcion"].lower()]

def filtrar_por_prioridad(tareas: List[Tarea], prioridad: str) -> List[Tarea]:
    p = prioridad.lower()
    return [t for t in tareas if t["prioridad"] == p]

def tareas_vencidas(tareas: List[Tarea], hoy: date = date.today()) -> List[Tarea]:
    return [t for t in tareas if (t["fecha_vencimiento"] < hoy and not t["completada"])]