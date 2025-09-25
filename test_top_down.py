"""
Pruebas Top Down para el sistema de biblioteca.

Este módulo contiene las pruebas de integración que verifican
el comportamiento del sistema usando stubs simulados.
"""

import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub


class TestBibliotecaSistema:
    """Suite de pruebas para el sistema de biblioteca usando metodología Top Down."""
    
    def setup_method(self):
        """Configuración común para todas las pruebas."""
        self.db_stub = DatabaseStub()
        self.auth_stub = AuthStub()
        self.sistema = BibliotecaSistema(self.db_stub, self.auth_stub)
    
    def test_prestamo_exitoso(self):
        """
        Prueba el flujo exitoso de préstamo.
        
        Escenario: Usuario autorizado (ID=1) solicita libro disponible (ID=2)
        Resultado esperado: Préstamo exitoso
        """
        # ARRANGE: Sistema ya configurado en setup_method
        
        # ACT: Ejecutar operación de préstamo
        resultado = self.sistema.prestar_libro(usuario_id=1, libro_id=2)
        
        # ASSERT: Verificar resultado exitoso
        assert resultado == "Préstamo exitoso"
    
    def test_usuario_no_autorizado(self):
        """
        Prueba rechazo por usuario no autorizado.
        
        Escenario: Usuario no autorizado (ID=0) solicita libro disponible (ID=2)
        Resultado esperado: Usuario no autorizado
        """
        # ACT: Ejecutar operación con usuario no autorizado
        resultado = self.sistema.prestar_libro(usuario_id=0, libro_id=2)
        
        # ASSERT: Verificar rechazo por autorización
        assert resultado == "Usuario no autorizado"
    
    def test_libro_no_disponible(self):
        """
        Prueba rechazo por libro no disponible.
        
        Escenario: Usuario autorizado (ID=1) solicita libro no disponible (ID=3)
        Resultado esperado: Libro no disponible
        """
        # ACT: Ejecutar operación con libro no disponible
        resultado = self.sistema.prestar_libro(usuario_id=1, libro_id=3)
        
        # ASSERT: Verificar rechazo por disponibilidad
        assert resultado == "Libro no disponible"
    
    def test_multiples_usuarios_autorizados(self):
        """
        Prueba que múltiples usuarios autorizados pueden acceder.
        
        Escenario: Varios usuarios con ID > 0 solicitan libros disponibles
        Resultado esperado: Todos los préstamos son exitosos
        """
        # Test con diferentes usuarios autorizados
        usuarios_test = [1, 2, 5, 10, 99]
        libro_disponible = 4  # ID par = disponible
        
        for usuario_id in usuarios_test:
            resultado = self.sistema.prestar_libro(usuario_id, libro_disponible)
            assert resultado == "Préstamo exitoso", f"Fallo para usuario {usuario_id}"
    
    def test_multiples_libros_no_disponibles(self):
        """
        Prueba que libros con ID impar no están disponibles.
        
        Escenario: Usuario autorizado solicita varios libros no disponibles
        Resultado esperado: Todos los libros son rechazados por no disponibilidad
        """
        # Test con diferentes libros no disponibles (ID impar)
        libros_no_disponibles = [1, 3, 5, 7, 9]
        usuario_autorizado = 1
        
        for libro_id in libros_no_disponibles:
            resultado = self.sistema.prestar_libro(usuario_autorizado, libro_id)
            assert resultado == "Libro no disponible", f"Fallo para libro {libro_id}"


# Pruebas individuales para mantener compatibilidad con el formato anterior
def test_prestamo_exitoso():
    """Prueba individual de flujo exitoso (compatibilidad)."""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)
    
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
    assert resultado == "Préstamo exitoso"


def test_usuario_no_autorizado():
    """Prueba individual de usuario no autorizado (compatibilidad)."""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)
    
    resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
    assert resultado == "Usuario no autorizado"