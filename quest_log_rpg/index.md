---
title: "QuestLog RPG — Privacy Policy / Política de privacidad"
---

# Política de Privacidad — QuestLog RPG

**Desarrollador:** neurozerox  
**Fecha de entrada en vigor:** 2026-11-07  
**Contacto:** david.cheuquen@gmail.com  
**Paquete:** `com.neurozerox.quest_log_rpg`

---

## Español

### 1. Resumen
QuestLog RPG es una aplicación de seguimiento de hábitos y tareas gamificada para uso personal. No requiere la creación de cuentas de usuario, no contiene anuncios publicitarios, no integra herramientas de análisis ni telemetría y funciona de manera 100% offline. El desarrollador no recopila, almacena ni transmite ningún tipo de información personal o de uso.

### 2. Datos almacenados en el dispositivo
Toda la información ingresada en la aplicación se almacena únicamente en la memoria local de tu dispositivo a través del almacenamiento seguro del sistema (`SharedPreferences`):
- Misiones, títulos de hábitos, categorías, nivel de dificultad y atributos asignados.
- Progreso del personaje: nivel, puntos de experiencia (EXP), puntos de vida (HP), monedas de oro acumuladas y puntos de atributos (Fuerza, Intelecto, Espíritu y Carisma).
- Rachas de días cumplidos y contadores de hábitos.
- Daño infligido y estado del Jefe Semanal.
- Preferencias de la aplicación: idioma seleccionado, paleta de colores activa y estado de compleción de la guía inicial.

### 3. Notificaciones y Recordatorios Locales
Si activas voluntariamente la función de recordatorio diario de misiones, la aplicación programará una notificación local en el dispositivo a la hora seleccionada. Esta función se ejecuta localmente mediante el sistema de alarmas inexactas de Android y no utiliza servidores remotos, conexiones de red ni servicios push en la nube.

### 4. Permisos solicitados
- `POST_NOTIFICATIONS`: Requerido en Android 13 y superior solo para emitir el recordatorio diario si decides activarlo. Puedes revocar este permiso en cualquier momento desde los ajustes del sistema operativo.
- `RECEIVE_BOOT_COMPLETED`: Permite al sistema operativo reprogramar el recordatorio local tras reiniciar el teléfono.
- `VIBRATE`: Permite la vibración sutil estándar al notificarte.
- **Sin permisos de alarmas exactas**: La aplicación no solicita `SCHEDULE_EXACT_ALARM` ni `USE_EXACT_ALARM`.

### 5. Copias de Seguridad y Compartir
- **Respaldo JSON**: Puedes exportar e importar archivos de respaldo en formato JSON utilizando el selector de archivos del sistema. Estos archivos se guardan únicamente donde tú decidas y nunca se envían a servidores externos.
- **Compartir Ficha de Héroe**: La tarjeta de estadísticas se procesa como imagen directamente en la memoria gráfica del dispositivo y se transfiere al menú nativo de compartir del sistema operativo únicamente cuando tocas el botón correspondiente.

### 6. Enlaces y Servicios de Terceros
QuestLog RPG no incluye SDKs de publicidad, herramientas de analítica (como Firebase o Google Analytics) ni pasarelas de pago. La aplicación no se comunica con ningún servidor externo durante su funcionamiento ordinario.

### 7. Menores de edad
La aplicación no recopila información personal de ningún usuario, incluidos niños y adolescentes menores de 13 años.

### 8. Eliminación de datos
Para borrar permanentemente todos los datos almacenados, puedes:
- Eliminar las misiones individualmente dentro de la aplicación.
- Borrar el almacenamiento o caché de la aplicación desde los ajustes de aplicaciones de tu dispositivo.
- Desinstalar la aplicación.

### 9. Contacto
Si tienes preguntas sobre esta política de privacidad o sobre el funcionamiento de la aplicación, puedes escribir a:  
**david.cheuquen@gmail.com**

---

## English

### 1. Overview
QuestLog RPG is a gamified habit tracker and daily quest planner designed for personal use. It requires no user account registration, displays no ads, contains no analytics or tracking SDKs, and runs 100% offline. The developer never collects, transmits, or accesses any user data.

### 2. Data Stored on Your Device
All content and progress created within the app are stored strictly in your device's local storage (`SharedPreferences`):
- Quest titles, categories, difficulty ratings, and linked character attributes.
- Hero progression stats: level, experience points (EXP), hit points (HP), gold coins, and attribute points (Strength, Intellect, Spirit, Charisma).
- Streak counters and habit counters.
- Weekly raid boss damage and health status.
- App settings: chosen language, color palette, and tutorial completion state.

### 3. Local Notifications & Daily Reminders
If you opt in to daily quest reminders, the app schedules a local notification at your chosen hour. This operates entirely within Android's local alarm subsystem without connecting to external cloud servers, push services, or internet networks.

### 4. Permissions Used
- `POST_NOTIFICATIONS`: Required on Android 13+ solely to deliver the optional daily reminder. You can disable this permission at any time in system settings.
- `RECEIVE_BOOT_COMPLETED`: Allows Android to restore your scheduled local reminder after restarting your device.
- `VIBRATE`: Allows standard vibration feedback on reminder delivery.
- **No exact alarm permissions**: The app avoids `SCHEDULE_EXACT_ALARM` or `USE_EXACT_ALARM` to respect battery efficiency.

### 5. Backup & Sharing
- **JSON Backup**: You can export and import JSON backup files using the OS file picker. These files exist only where you choose to save them and are never uploaded to any remote server.
- **Share Hero Card**: Hero cards are rendered into images entirely on your device and passed to the operating system's native share sheet only when initiated by you.

### 6. Third-Party Services
QuestLog RPG integrates no ad networks, tracking libraries, or telemetry platforms. No network requests are made during standard operation.

### 7. Children's Privacy
The application does not collect personal data from anyone, including children under 13.

### 8. Data Retention & Deletion
To permanently delete all stored data, you can:
- Delete quests manually within the app.
- Clear app data/cache in your Android system settings.
- Uninstall the app from your device.

### 9. Contact
If you have any questions or feedback regarding this privacy policy, please contact:  
**david.cheuquen@gmail.com**
