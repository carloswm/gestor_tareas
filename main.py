from utils import clear_screen
from persistencia import cargar_tareas, guardar_tareas
from logica_tareas import (
    agregar_tarea, eliminar_tarea, marcar_completada,
    listar_tareas, buscar_tareas, filtrar_por_prioridad,
    tareas_vencidas
)

def menu():
    tareas = cargar_tareas()
    while True:
        clear_screen()
        print("""Gestor de Tareas
                1. Agregar tarea
                2. Ver todas las tareas
                3. Buscar tarea
                4. Filtrar por prioridad
                5. Mostrar vencidas
                6. Marcar como completada
                7. Eliminar tarea
                8. Guardar y salir""")
        opc = input("> ").strip()
        if opc == "1":
            titulo = input("Título: ")
            desc   = input("Descripción: ")
            fecha  = input("Fecha venc. (YYYY-MM-DD): ")
            prio   = input("Prioridad (alta/media/baja): ")
            try:
                t = agregar_tarea(tareas, titulo, desc, fecha, prio)
                print(f"Tarea creada con ID {t['id']}")
            except ValueError as e:
                print("Error:", e)
            input("Enter para continuar…")
        elif opc == "2":
            listar_tareas(tareas)
            input("Enter para continuar…")
        elif opc == "3":
            palabra = input("Buscar palabra: ")
            res = buscar_tareas(tareas, palabra)
            if res:
                listar_tareas(res)
            else:
                print("No se encontraron tareas.")
            input("Enter para continuar…")
        elif opc == "4":
            prio = input("Prioridad a filtrar (alta/media/baja): ")
            try:
                res = filtrar_por_prioridad(tareas, prio)
                listar_tareas(res)
            except ValueError as e:
                print("Error:", e)
            input("Enter para continuar…")
        elif opc == "5":
            venc = tareas_vencidas(tareas)
            if venc:
                listar_tareas(venc)
            else:
                print("No hay tareas vencidas.")
            input("Enter para continuar…")
        elif opc == "6":
            idm = int(input("ID de tarea a marcar completada: "))
            if marcar_completada(tareas, idm):
                print("Marcada como completada.")
            else:
                print("ID no encontrado.")
            input("Enter para continuar…")
        elif opc == "7":
            idd = int(input("ID de tarea a eliminar: "))
            if eliminar_tarea(tareas, idd):
                print("Tarea eliminada.")
            else:
                print("ID no encontrado.")
            input("Enter para continuar…")
        elif opc == "8":
            guardar_tareas(tareas)
            print("Guardado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            input("Enter para continuar…")

if __name__ == "__main__":
    menu()