from mensajeria.sistema import Sistema
from mensajeria.empleado import Empleado
from mensajeria.administrador import Administrador

def main() :
    root = Sistema()
    root.importarEmpleados()

    while True :
        user = root.login()

        user.importarMensajes()

        print(f"Bienvenido/a {user.nombre}!")
        
        while True :
            # MENU
            print("MENÚ PRINCIPAL")
            if isinstance(user, Administrador) :
                print("0. Cerrar sesión")
                print("1. Bandeja de entrada")
                print("2. Mensajes leidos")
                print("3. Borradores")
                print("4. Redactar mensaje")
                print("5. Agregar usuario")
                print("6. Cambiar contraseña")
                print("7. Eliminar usuario")
                entrada = input("Seleccione lo que quiera hacer: ")
                if entrada == '0' : break
                elif entrada == '1' : user.bandejaEntrada()
                elif entrada == '2' : user.mensajesLeidos()
                elif entrada == '3' : user.borradores()
                elif entrada == '4' : user.redactarMensaje(root)
                elif entrada == '5' : user.agregarUsuario(root)
                elif entrada == '6' : user.cambiarContraseña()
                elif entrada == '7' : user.eliminarEmpleado(root)
                else : break
            elif isinstance(user, Empleado) :
                print("0. Cerrar sesión")
                print("1. Bandeja de entrada")
                print("2. Mensajes leidos")
                print("3. Borradores")
                print("4. Redactar mensaje")
                entrada = input("Seleccione lo que quiera hacer: ")
                if entrada == '0' : break
                elif entrada == '1' : user.bandejaEntrada()
                elif entrada == '2' : user.mensajesLeidos()
                elif entrada == '3' : user.borradores()
                elif entrada == '4' : user.redactarMensaje(root)
                else : break

        user.exportarMensajes()

main()