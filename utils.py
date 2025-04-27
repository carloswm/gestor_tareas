from datetime import datetime, date
from typing import Any, Dict, List

PRIORIDADES = {"alta", "media", "baja"}

def generar_id(tareas: List[Dict[str, Any]]) -> int:
    return 1 if not tareas else max(t["id"] for t in tareas) + 1

def validar_fecha(fecha_str: str) -> date:

    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha inválido. Usa YYYY-MM-DD.")

def validar_prioridad(prio: str) -> str:
    p = prio.lower()
    if p not in PRIORIDADES:
        raise ValueError(f"Prioridad inválida. Elige entre {PRIORIDADES}.")
    return p

def clear_screen() -> None:
    """Limpia la consola (Windows y Unix)."""
    import os
    os.system("cls" if os.name == "nt" else "clear")