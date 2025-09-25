"""
Sistema de gestión de biblioteca con inyección de dependencias.

Este módulo contiene la lógica principal del sistema de biblioteca
que maneja préstamos de libros utilizando stubs para pruebas.
"""


class BibliotecaSistema:
    """
    Sistema principal de gestión de biblioteca.
    
    Maneja las operaciones de préstamo de libros utilizando
    inyección de dependencias para autenticación y base de datos.
    """
    
    def __init__(self, db, auth):
        """
        Inicializa el sistema de biblioteca.
        
        Args:
            db: Interfaz de base de datos (puede ser stub o implementación real)
            auth: Interfaz de autenticación (puede ser stub o implementación real)
        """
        self.db = db
        self.auth = auth
    
    def prestar_libro(self, usuario_id: int, libro_id: int) -> str:
        """
        Procesa el préstamo de un libro a un usuario.
        
        Args:
            usuario_id (int): ID del usuario que solicita el préstamo
            libro_id (int): ID del libro a prestar
            
        Returns:
            str: Resultado del préstamo ('Préstamo exitoso', 'Usuario no autorizado', 
                 o 'Libro no disponible')
        """
        # 1. Verificar autorización del usuario
        if not self.auth.verificar_usuario(usuario_id):
            return "Usuario no autorizado"
        
        # 2. Verificar disponibilidad del libro
        if not self.db.libro_disponible(libro_id):
            return "Libro no disponible"
        
        # 3. Registrar el préstamo exitoso
        self.db.registrar_prestamo(usuario_id, libro_id)
        return "Préstamo exitoso"