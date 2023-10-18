from mensajeria.sistema import Sistema

def main() :
    root = Sistema()
    root.importarEmpleados()

    user = root.login()
    print(f"Bienvenido/a {user.nombre}!")

main()