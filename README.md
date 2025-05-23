# 🍤 Sistema de Registro Digital de Pedidos – Restaurante Tuya Pez

## 📌 Resumen

**Tuya Pez**, restaurante peruano especializado en comida marina, actualmente registra los pedidos de forma manual, lo que genera errores, pérdida de tiempo y dificulta el análisis de datos. Para solucionar este problema, se ha desarrollado una aplicación en **Python 3.12** que permite registrar digitalmente los pedidos, calcular el total automáticamente y almacenar la información en archivos CSV. Este sistema mejora la eficiencia, reduce los errores y facilita la toma de decisiones.

---

## 🏢 Datos del Restaurante

- **Razón social:** Tuya Pez S.A.C.
- **Giro:** Gastronomía – Comida marina
- **Misión:** Brindar una experiencia gastronómica marina memorable a través de calidad, atención y tradición.
- **Visión:** Ser el restaurante marino líder en innovación y servicio personalizado en Perú.

---

## 📉 Situación Actual

El proceso manual de registro de pedidos genera problemas como:

- Errores en los cálculos.
- Pérdida de información.
- Demora en la atención y facturación.
- Dificultad para generar reportes.
- Imposibilidad de obtener estadísticas útiles en tiempo real.

---

## 💡 Propuesta de Innovación

Se propone la digitalización del proceso mediante una aplicación desarrollada en Python que permite:

- Registrar los platos solicitados con nombre, cantidad y precio.
- Calcular automáticamente el total a pagar.
- Registrar el tipo de pago (efectivo o POS).
- Guardar toda la información en un archivo CSV.

---

## 🔄 Detalle del Nuevo Proceso

### Entradas:
- Nombre del plato
- Cantidad
- Precio unitario
- Método de pago

### Proceso:
- Registro de pedido (múltiples ítems).
- Validación de datos.
- Cálculo automático del total.
- Almacenamiento del resumen en CSV.

### Salidas:
- Archivo `pedido_tuya_pez.csv` con los datos del pedido y el total.
- Datos disponibles para análisis posteriores y control de ventas.

---

## 🛠️ Herramientas Utilizadas

- **Lenguaje:** Python 3.12
- **Base de datos:** CSV (formato plano para análisis y visualización)
- **Gestión de proyecto:** Trello (product backlog y tareas por sprint)

---

## 📌 Algoritmo Propuesto (Pseudocódigo)

```text
FUNCIÓN main()
  Mostrar encabezado
  Solicitar nombre del plato
  Validar cantidad y precio
  Calcular subtotal y total
  Solicitar método de pago
  Escribir los datos en archivo CSV
FIN FUNCIÓN
```

---

## ⚙️ Instalación y Ejecución

### ✅ Requisitos

- Python 3.12 instalado
- Editor de código (VS Code, Thonny, etc.)

### 📥 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/nombre_del_repo.git
cd nombre_del_repo
```

### ▶️ Cómo ejecutar el proyecto

```bash
python pedido_tuya_pez.py
```
