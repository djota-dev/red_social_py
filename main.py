from red_social import RedSocial

def main():
    red_social = RedSocial()

    # estoy cargando datos guardados
    try:
        red_social.cargar_datos("datos_red_social.json")
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se creará uno nuevo.")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Usuario")
        print("2. Crear Publicación")
        print("3. Ver Publicaciones de un Usuario")
        print("4. Ver Todas las Publicaciones")
        print("5. Guardar y Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            red_social.registrar_usuario(nombre, email)
            print("Usuario registrado con éxito.")
        
        elif opcion == '2':
            email = input("Ingrese el email del usuario: ")
            usuario = red_social.encontrar_usuario(email)
            
            if usuario:
                contenido = input("Ingrese el contenido de la publicación: ")
                usuario.crear_publicacion(contenido)
                print("Publicación creada con éxito.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == '3':
            email = input("Ingrese el email del usuario: ")
            usuario = red_social.encontrar_usuario(email)
            
            if usuario:
                usuario.mostrar_publicaciones()
            else:
                print("Usuario no encontrado.")
        
        elif opcion == '4':
            red_social.mostrar_todas_publicaciones()
        
        elif opcion == '5':
            red_social.guardar_datos('datos_red_social.json')
            print("Datos guardados exitosamente. Saliendo...")
            print("by qub1t:. :)")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
