# TABLA-SOLICITUD-PRESTAMO

### JSON de Entrada y Salida para las funciones Lambda de la **Tabla Solicitud de Préstamo**

---

### **1. Crear Solicitud de Préstamo (POST)**  
**Endpoint:** `/solicitud-prestamo/crear`

#### **Entrada:**
```json
{
  "usuario_id": "user123",
  "cuenta_id": "account12345",
  "monto": 10000,
  "plazo": 12,
  "descripcion": "Necesito un préstamo para mi negocio"
}
```

#### **Salida (Éxito):**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-generado",
  "cuenta_id": "account12345",
  "monto": 10000,
  "plazo": 12,
  "estado": "pendiente",
  "descripcion": "Necesito un préstamo para mi negocio",
  "fecha_creacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles:**
1. **Faltan campos obligatorios:**
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id, cuenta_id, monto o plazo"
   }
   ```

2. **Usuario o Cuenta no encontrados:**
   ```json
   {
     "error": "Usuario o Cuenta no encontrados",
     "details": "El usuario o la cuenta asociada no existen"
   }
   ```

---

### **2. Aceptar Solicitud de Préstamo (PUT)**  
**Endpoint:** `/solicitud-prestamo/aceptar`

#### **Entrada:**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "tasa_interes": 0.05
}
```

#### **Salida (Éxito):**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "estado": "aceptada",
  "fecha_aceptacion": "2024-11-12T12:00:00Z",
  "tasa_interes": 0.05
}
```

#### **Errores Posibles:**
1. **Faltan campos obligatorios:**
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id, solicitud_id o tasa_interes"
   }
   ```

2. **Solicitud no encontrada:**
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

3. **Estado no válido:**
   ```json
   {
     "error": "Estado inválido",
     "details": "Solo las solicitudes en estado 'pendiente' pueden ser aceptadas"
   }
   ```

---

### **3. Rechazar Solicitud de Préstamo (PUT)**  
**Endpoint:** `/solicitud-prestamo/rechazar`

#### **Entrada:**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001"
}
```

#### **Salida (Éxito):**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "estado": "rechazada",
  "fecha_rechazo": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles:**
1. **Faltan campos obligatorios:**
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id o solicitud_id"
   }
   ```

2. **Solicitud no encontrada:**
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

3. **Estado no válido:**
   ```json
   {
     "error": "Estado inválido",
     "details": "Solo las solicitudes en estado 'pendiente' pueden ser rechazadas"
   }
   ```

---

### **4. Listar Solicitudes de Préstamo por Usuario (GET)**  
**Endpoint:** `/solicitud-prestamo/listar`

#### **Entrada:**
```json
{
  "usuario_id": "user123"
}
```

#### **Salida (Éxito):**
```json
[
  {
    "usuario_id": "user123",
    "solicitud_id": "uuid-solicitud001",
    "monto": 10000,
    "plazo": 12,
    "estado": "pendiente",
    "descripcion": "Necesito un préstamo para mi negocio",
    "fecha_creacion": "2024-11-12T12:00:00Z"
  },
  {
    "usuario_id": "user123",
    "solicitud_id": "uuid-solicitud002",
    "monto": 5000,
    "plazo": 6,
    "estado": "rechazada",
    "descripcion": "Préstamo para remodelar la casa",
    "fecha_creacion": "2024-11-10T08:00:00Z"
  }
]
```

#### **Errores Posibles:**
1. **Faltan campos obligatorios:**
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Falta el campo usuario_id"
   }
   ```

---

### **5. Obtener Solicitud de Préstamo (GET)**  
**Endpoint:** `/solicitud-prestamo/obtener`

#### **Entrada:**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001"
}
```

#### **Salida (Éxito):**
```json
{
  "usuario_id": "user123",
  "solicitud_id": "uuid-solicitud001",
  "monto": 10000,
  "plazo": 12,
  "estado": "pendiente",
  "descripcion": "Necesito un préstamo para mi negocio",
  "fecha_creacion": "2024-11-12T12:00:00Z"
}
```

#### **Errores Posibles:**
1. **Faltan campos obligatorios:**
   ```json
   {
     "error": "Solicitud inválida",
     "details": "Faltan campos obligatorios: usuario_id o solicitud_id"
   }
   ```

2. **Solicitud no encontrada:**
   ```json
   {
     "error": "Solicitud no encontrada",
     "details": "No existe una solicitud asociada al usuario_id y solicitud_id proporcionados"
   }
   ```

---

Espero que esta estructura sea clara y cubra todos los escenarios posibles. ¿Algo más que ajustar o agregar? 😊
