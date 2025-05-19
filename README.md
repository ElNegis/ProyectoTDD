# 🎮 Juego de 3 en Raya (Tic Tac Toe)

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://github.com/usuario/tic-tac-toe/workflows/CI%2FCD%20Pipeline/badge.svg)
![Coverage](https://codecov.io/gh/usuario/tic-tac-toe/branch/main/graph/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un juego clásico de 3 en raya implementado en Python con una arquitectura limpia, pruebas unitarias completas y CI/CD automatizado.

## 🚀 Características

- ✅ Juego completo de 3 en raya para 2 jugadores
- ✅ Interfaz de consola intuitiva
- ✅ Validación de movimientos en tiempo real
- ✅ Detección automática de victoria y empate
- ✅ Arquitectura modular y extensible
- ✅ Cobertura de pruebas > 90%
- ✅ CI/CD con GitHub Actions
- ✅ Análisis de seguridad automatizado

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación rápida

```bash
# Clonar el repositorio
git clone https://github.com/usuario/tic-tac-toe.git
cd tic-tac-toe

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Para desarrollo

```bash
# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

## 🎯 Uso

### Ejecutar el juego

```bash
python main.py
```

### Ejemplo de juego

```
=== JUEGO DE 3 EN RAYA ===

Ingresa el nombre del Jugador 1 (X): Alice
Ingresa el nombre del Jugador 2 (O): Bob

¡Bienvenido al juego de 3 en raya!
Alice juega con 'X'
Bob juega con 'O'

   0   1   2
  -----------
0 |   |   |   |
  -----------
1 |   |   |   |
  -----------
2 |   |   |   |

Turno de Alice (X)
Ingresa la fila (0-2): 1
Ingresa la columna (0-2): 1
```

## 🧪 Pruebas

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar con cobertura

```bash
pytest --cov=src --cov-report=html
```

### Ejecutar pruebas específicas

```bash
# Pruebas del tablero
pytest tests/test_board.py

# Pruebas del jugador
pytest tests/test_player.py

# Pruebas del juego
pytest tests/test_game.py
```

## 🔧 Desarrollo

### Estructura del proyecto

```
tic-tac-toe/
├── src/                    # Código fuente
│   ├── board.py           # Lógica del tablero
│   ├── player.py          # Lógica del jugador
│   └── game.py            # Lógica principal del juego
├── tests/                 # Pruebas unitarias
├── .github/workflows/     # Configuración CI/CD
├── main.py               # Punto de entrada
└── requirements*.txt     # Dependencias
```

### Comandos útiles

```bash
# Formatear código
black src tests

# Linting
flake8 src tests

# Análisis de tipos
mypy src

# Verificar seguridad
bandit -r src/
safety check
```

## 🏗️ Arquitectura

### Principios de diseño

- **Separación de responsabilidades**: Cada clase tiene una responsabilidad específica
- **Principio abierto/cerrado**: Fácil extensión sin modificar código existente
- **Inversión de dependencias**: Bajo acoplamiento entre componentes

### Componentes principales

1. **Board**: Maneja el estado del tablero y las reglas del juego
2. **Player**: Representa a un jugador y maneja la entrada de usuario
3. **Game**: Orquesta el flujo del juego y la interacción entre componentes

## 🔄 CI/CD Pipeline

Nuestro pipeline automatizado incluye:

1. **Pruebas**: Ejecuta en Python 3.8-3.12
2. **Calidad de código**: Linting con flake8, tipo checking con mypy
3. **Seguridad**: Análisis con bandit y safety
4. **Cobertura**: Reportes automáticos a Codecov
5. **Build**: Construcción de paquetes en rama main

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

### Guías de contribución

- Asegúrate de que las pruebas pasen: `pytest`
- Mantén la cobertura > 90%
- Sigue las convenciones de código (flake8, black)
- Agrega documentación para nuevas funcionalidades

## 📝 Changelog

### v1.0.0 (2024-01-01)
- Implementación inicial del juego
- Pruebas unitarias completas
- CI/CD con GitHub Actions
- Documentación completa

## 🔒 Seguridad

Si encuentras vulnerabilidades de seguridad, por favor envía un email a security@ejemplo.com en lugar de crear un issue público.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## ✨ Agradecimientos

- Inspirado en el clásico juego de 3 en raya
- Construido con amor ❤️ y Python 🐍

---

<div align="center">
  <strong>¡Diviértete jugando! 🎮</strong>
</div>