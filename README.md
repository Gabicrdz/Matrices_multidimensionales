# Carga de datos de Personas 👥📱

## Descripción del Proyecto
Esta es una aplicación web simple para gestionar información de personas, permitiendo agregar múltiples números de teléfono por persona y visualizar los datos ingresados.

## Características ✨
- Formulario interactivo para ingresar datos personales
- Agregar múltiples números de teléfono de forma dinámica
- Visualización instantánea de personas registradas
- Diseño responsivo y moderno

## Tecnologías Utilizadas 🚀
- HTML5
- JavaScript
- Tailwind CSS (via CDN)

## Estructura del Código 📂
```
index.html           # Archivo principal de la aplicación
```

## Funcionalidades Principales 🔍
- **Agregar Persona**: Permite ingresar nombre, apellido y DNI
- **Gestión de Teléfonos**: 
  - Botón "+" para añadir números de teléfono
  - Botón "-" para eliminar números de teléfono
- **Listado de Personas**: Muestra todas las personas registradas

## Cómo Usar 🖥️

### Paso 1: Ingresar Datos
1. Introduce el nombre en el campo "Nombre"
2. Introduce el apellido en el campo "Apellido"
3. Introduce el DNI en el campo "DNI"

### Paso 2: Agregar Teléfonos
- Haz clic en el botón "+" para añadir más números de teléfono
- Usa el botón "-" para eliminar números de teléfono no deseados

### Paso 3: Guardar
- Haz clic en "Agregar Persona"
- Los datos se mostrarán instantáneamente en la lista de personas

## Ejemplo de Estructura de Datos 📊
```javascript
[
  [
    'Juan',     // Nombre
    'Pérez',    // Apellido
    '26123456', // DNI
    [           // Teléfonos
      '37041223', 
      '37043215'
    ]
  ]
]
```

## Requisitos 🔧
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexión a Internet (para cargar Tailwind CSS)