# =====================
# Proyecto final RBAC
# ====================
texto = """
En este proyecto desarrollamos en equipo un sistema de control de acceso basado en roles (RBAC) en el lenguaje de Python.
El sistema permite a los usuarios iniciar sesión con diferentes roles como:
(admin, usuario, invitado) y acceder a funcionalidades específicas según su rol.
"""
comentarios = []
usuarios = {
    "Juan": {
        "password": "1234",
        "rol": "admin"
    },
    "Donis": {
        "password": "5678",
        "rol": "usuario"
    },
    "Victor": {
        "password": "0000",
        "rol": "invitado"
    }
}
def iniciar_sesion():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in usuarios:
        if usuarios[usuario]["password"] == contraseña:
            print("\n✅ Inicio de sesión exitoso")
            return usuario
    print("\n❌ Usuario o contraseña incorrectos")
    return None
def mostrar_menu(rol):
    print("\n========= MENÚ =========")
    print("1. Leer texto")
    if rol in ["admin", "usuario"]:
        print("2. Comentar texto")
    if rol == "admin":
        print("3. Editar texto")
        print("4. Borrar texto")
    print("0. Cerrar sesión")
while True:
    print("\n=========================")
    print(" SISTEMA DE ACCESO RBAC ")
    print("=========================")
    usuario_actual = iniciar_sesion()
    if usuario_actual is None:
        continue
    rol = usuarios[usuario_actual]["rol"]
    while True:
        mostrar_menu(rol)
        opcion = input("\nSeleccione una opción: ")
        # opción para leer
        if opcion == "1":
            print("\n----- TEXTO -----")
            print(texto)
            if comentarios:
                print("\nComentarios:")
                for c in comentarios:
                    print("-", c)
        # opción para comentar
        elif opcion == "2" and rol in ["admin", "usuario"]:
            comentario = input("Escriba su comentario: ")
            comentarios.append(
                f"{usuario_actual}: {comentario}"
            )
            print("✅ Comentario agregado")
        # opción para editar
        elif opcion == "3" and rol == "admin":
            print("\nTexto actual:")
            print(texto)
            texto = input(
                "\nIngrese el nuevo texto:\n"
            )
            print("✅ Texto actualizado")
        # opción para borrar
        elif opcion == "4" and rol == "admin":
            texto = ""
            print("✅ Texto eliminado")
        # cerrar sesión
        elif opcion == "0":
            print("\nSesión cerrada.")
            break
        else:
            print("\n❌ No tiene permisos o la opción no existe.")

