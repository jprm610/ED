from mensajeria.sistema import Sistema

def main() :
    root = Sistema()
    root.importarEmpleados()
    root.empleados.print()

main()