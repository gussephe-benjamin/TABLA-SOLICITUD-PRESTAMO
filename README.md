# TABLA-SOLICITUD-PRESTAMO

¡Entendido! Aquí tienes los **JSON de entrada y salida** para cada función Lambda de la tabla **TABLA-SOLICITUD-PRESTAMO**, teniendo en cuenta las entradas correctas y coherentes con el esquema.

---

### **1. Crear Solicitud de Préstamo (POST)**
**Endpoint:** `/solicitud-prestamo/crear`

#### **Entrada**:
```json
{
  "usuario_id": "user123",
  "monto": 10000,
  "descripcion": "Necesito un préstamo para iniciar un negocio"
}
```

#### **Salida (Éxito)**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-generado",
  "monto": 10000,
  "estado": "pendiente",
  "descripcion": "Necesito un préstamo para iniciar un negocio",
  "fecha_creacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles**:
1. **Faltan campos obligatorios**:
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id o monto"
   }
   ```

2. **Monto inválido (por ejemplo, negativo)**:
   ```json
   {
     "error": "Solicitud inválida",
     "details": "El monto debe ser mayor a 0"
   }
   ```

---

### **2. Aceptar Solicitud de Préstamo (PUT)**
**Endpoint:** `/solicitud-prestamo/aceptar`

#### **Entrada**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001"
}
```

#### **Salida (Éxito)**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "estado": "aceptada",
  "fecha_actualizacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles**:
1. **Solicitud no encontrada**:
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

2. **Estado no válido (ya aceptada o rechazada)**:
   ```json
   {
     "error": "Estado inválido",
     "details": "Solo las solicitudes en estado 'pendiente' pueden ser aceptadas"
   }
   ```

---

### **3. Rechazar Solicitud de Préstamo (PUT)**
**Endpoint:** `/solicitud-prestamo/rechazar`

#### **Entrada**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001"
}
```

#### **Salida (Éxito)**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "estado": "rechazada",
  "fecha_actualizacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles**:
1. **Solicitud no encontrada**:
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

2. **Estado no válido (ya aceptada o rechazada)**:
   ```json
   {
     "error": "Estado inválido",
     "details": "Solo las solicitudes en estado 'pendiente' pueden ser rechazadas"
   }
   ```

---

### **4. Listar Solicitudes de Préstamo por Usuario (GET)**
**Endpoint:** `/solicitud-prestamo/listar`

#### **Entrada**:
```json
{
  "usuario_id": "user123"
}
```

#### **Salida (Éxito)**:
```json
[
  {
    "usuario_id": "user123",
    "solicitud_id": "uuid-solicitud001",
    "monto": 10000,
    "estado": "pendiente",
    "descripcion": "Necesito un préstamo para iniciar un negocio",
    "fecha_creacion": "2024-11-12T12:00:00Z"
  },
  {
    "usuario_id": "user123",
    "solicitud_id": "uuid-solicitud002",
    "monto": 5000,
    "estado": "rechazada",
    "descripcion": "Préstamo para remodelar la casa",
    "fecha_creacion": "2024-11-10T08:00:00Z"
  }
]
```

#### **Errores Posibles**:
1. **Faltan campos obligatorios**:
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Falta el campo usuario_id"
   }
   ```

---

### **5. Obtener Solicitud de Préstamo (GET)**
**Endpoint:** `/solicitud-prestamo/obtener`

#### **Entrada**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001"
}
```

#### **Salida (Éxito)**:
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "monto": 10000,
  "estado": "pendiente",
  "descripcion": "Necesito un préstamo para iniciar un negocio",
  "fecha_creacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles**:
1. **Faltan campos obligatorios**:
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id o solicitud_id"
   }
   ```

2. **Solicitud no encontrada**:
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

---

Ahora tienes las entradas y salidas detalladas para todas las funciones de la tabla **Solicitud de Préstamo**. 😊 ¿Algo más que ajustar o complementar?
