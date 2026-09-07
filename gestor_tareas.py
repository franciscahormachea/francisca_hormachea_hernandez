class Tarea:
    def __init__(self, identificador, descripcion, prioridad):
        self.identificador = identificador
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{self.identificador}] {self.descripcion} - {self.prioridad} - {estado}"


class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.correlativo = 1

    def agregar(self, descripcion, prioridad="Media"):
        tarea = Tarea(self.correlativo, descripcion, prioridad)
        self.tareas.append(tarea)
        self.correlativo += 1
        return tarea

    def completar(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                tarea.completar()
                return True
        return False

    def listar(self, solo_pendientes=False):
        for tarea in self.tareas:
            if solo_pendientes and tarea.completada:
                continue
            print(tarea)


if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.agregar("Configurar repositorio del proyecto", "Alta")
    gestor.agregar("Documentar el flujo de ramas", "Media")
    gestor.completar(1)
    gestor.listar()