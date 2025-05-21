import sqlite3
#comentario
def mostrar_menu():
    print("\033[34mTaller CRUD básico en Python y SQLite desde\033[0m\033[44m desktop Ubuntu \033[0m")
    print("\033[34m1. Agregar usuario\033[0m")
    print("\033[34m2. Consultar usuarios\033[0m")
    print("\033[34m3. Actualizar usuario\033[0m")
    print("\033[34m4. Eliminar usuario\033[0m")
    print("\033[34m5. Salir\033[0m")

def conectar():
    return sqlite3.connect("uninpahu.db")

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def agregar():
    id_usuario = input("Ingrese el ID del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")

    conn = conectar()
    cursor = conn.cursor()

    # Verificar si el ID ya existe
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
    if cursor.fetchone():
        print("\033[31mError: El ID ya existe. Intente con otro.\033[0m")
    else:
        cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (?, ?)", (id_usuario, nombre))
        conn.commit()
        print("\033[32mUsuario agregado correctamente.\033[0m")

    conn.close()

def consultar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    conn.close()
    
    if registros:
        print("\033[36mLista de usuarios:\033[0m")
        for row in registros:
            print(f"ID: {row[0]}, Nombre: {row[1]}")
    else:
        print("\033[33mNo hay usuarios registrados.\033[0m")

def actualizar():
    id_usuario = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nuevo_nombre, id_usuario))
    
    if cursor.rowcount > 0:
        print("\033[32mUsuario actualizado correctamente.\033[0m")
    else:
        print("\033[31mNo se encontró un usuario con ese ID.\033[0m")
    
    conn.commit()
    conn.close()

def eliminar():
    id_usuario = input("Ingrese el ID del usuario a eliminar: ")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    
    if cursor.rowcount > 0:
        print("\033[31mUsuario eliminado correctamente.\033[0m")
    else:
        print("\033[31mNo se encontró un usuario con ese ID.\033[0m")
    
    conn.commit()
    conn.close()

def main():
    crear_tabla()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar()
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print("\033[31mSaliendo del programa...\033[0m")
            break
        else:
            print("\033[31mOpción no válida. Intente de nuevo.\033[0m")

if __name__ == "__main__":
    main()
