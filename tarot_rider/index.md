---
title: "Tarot Rider-Waite — Privacy Policy / Política de privacidad"
---

# Política de privacidad — Tarot Rider-Waite

**Desarrollador:** neurozerox
**Fecha de entrada en vigor:** 2026-11-07
**Contacto:** david.cheuquen@gmail.com

## Español

### Resumen
La app no tiene cuentas, no muestra anuncios y no envía a ningún servidor tus
lecturas, tus notas ni tus fotos. Lo único que sale del dispositivo son datos
técnicos de diagnóstico que envía la biblioteca Google ML Kit cuando usas la
lectura por foto (ver más abajo).

### Datos que se guardan en tu dispositivo
- **Ajustes**: idioma, paleta de color, si usas cartas invertidas, si ya
  viste la presentación inicial y, si lo activas, la hora del recordatorio
  diario.
- **Diario de lecturas**: tirada, cartas, interpretación, la nota opcional que
  escribas y si la marcaste como favorita. Se guarda solo en el almacenamiento
  privado de la app.
- **Carta del día**: la fecha y la carta de cada día que la revelas (para
  mostrar tu racha). Se guarda solo en el dispositivo.
- «Copiar lectura» pone el texto en el portapapeles del sistema solo cuando tú
  lo pides.
- **Compartir como imagen**: la imagen se crea en el dispositivo y solo sale de
  él cuando tú la envías con la hoja de compartir del sistema a la app o
  persona que elijas. Tu nota personal solo aparece en la imagen si activas
  «Incluir mi nota».
- **Copia de seguridad**: «Exportar diario» crea un archivo con tus lecturas,
  notas, favoritas e historial de cartas del día y lo entrega a la hoja de
  compartir del sistema; tú decides dónde guardarlo o a quién enviarlo.
  «Importar diario» lee solo el archivo que eliges con el selector del
  sistema. La app no sube estos archivos a ningún servidor.

Estos datos no se transmiten a nadie salvo cuando tú los compartes. Puedes borrar cada lectura desde el
Diario, o todo borrando los datos de la app o desinstalándola.

### Fotos (lectura por foto)
- Cuando eliges «Tomar foto» se abre la cámara del sistema; con «Elegir de la
  galería» se abre el selector de fotos del sistema, que solo da a la app la
  foto que eliges (no se piden permisos de almacenamiento ni de fotos).
- La foto se procesa **en el dispositivo**: el reconocimiento de texto de Google
  ML Kit usa un modelo incluido en la app y no envía la imagen ni el texto
  reconocido a ningún servidor.
- La app trabaja con una copia temporal de la foto en su caché y la **borra en
  cuanto termina de leerla**. La foto no se guarda en el diario.

### Servicios de terceros
- **Google ML Kit – Text Recognition** (en el dispositivo). Según la
  [divulgación de datos de ML Kit](https://developers.google.com/ml-kit/android-data-disclosure),
  la biblioteca envía a Google, cifrado (HTTPS), datos técnicos para
  diagnóstico y analítica de uso del propio ML Kit: información del dispositivo
  (fabricante, modelo, versión del sistema), información de la app (nombre del
  paquete y versión), identificadores por instalación (no pensados para
  identificar a una persona ni al dispositivo), métricas de rendimiento,
  configuración de la API (p. ej. formato y resolución de imagen), tipo de
  evento y códigos de error. Google indica que no transfiere estos datos a
  terceros. No incluye la imagen ni el texto. Política de Google:
  <https://policies.google.com/privacy>.
- La cámara y el selector de fotos son componentes del propio sistema
  operativo.

### Recordatorio diario (opcional)
- Está desactivado por defecto. Si lo activas en Ajustes, la app pide permiso
  para mostrar notificaciones (Android 13 o superior) y programa en el propio
  teléfono un aviso al día a la hora que elijas, solo si aún no has revelado tu
  carta del día. Puedes desactivarlo cuando quieras.
- Los avisos se programan localmente; no se usa ningún servicio de
  notificaciones en línea.

### Permisos
- No se solicitan permisos de cámara, fotos ni almacenamiento: la cámara y el
  selector de fotos del sistema entregan la imagen a la app solo cuando tú la
  eliges.
- **Notificaciones** (`POST_NOTIFICATIONS`): solo se pide al activar el
  recordatorio diario. **Inicio del dispositivo** (`RECEIVE_BOOT_COMPLETED`):
  para volver a programar el recordatorio tras reiniciar. **Vibración**: la
  declara la biblioteca de notificaciones.
- El acceso a Internet que pueda figurar en la ficha técnica proviene de las
  bibliotecas de Google ML Kit (envío de diagnósticos descrito arriba). La app
  no lo usa para nada más.

### Menores
La app no está dirigida a menores de 13 años y no recoge conscientemente datos
personales de nadie.

### Conservación y borrado
Los datos locales se conservan hasta que los borras (Diario, borrar datos de la
app o desinstalar). Las fotos se borran automáticamente tras leerlas. Los
diagnósticos de ML Kit los gestiona Google según su política.

### Ilustraciones
Las ilustraciones de las cartas son la baraja original de 1909 de Pamela
Colman Smith, de dominio público.

### Cambios
Publicaremos cualquier cambio en esta página con su nueva fecha.

### Contacto
david.cheuquen@gmail.com

---

## English

### Summary
The app has no accounts, shows no ads and never sends your readings, notes or
photos to any server. The only data that leaves the device is technical
diagnostic data sent by the Google ML Kit library when you use photo reading
(see below).

### Data stored on your device
- **Settings**: language, colour palette, whether reversed cards are used,
  whether you have seen the welcome screens and, if you turn it on, the time
  of the daily reminder.
- **Reading journal**: spread, cards, interpretation, the optional note you
  write and whether you marked it as a favourite. Stored only in the app's
  private storage.
- **Card of the day**: the date and card of each day you reveal it (to show
  your streak). Stored only on the device.
- "Copy reading" puts the text on the system clipboard only when you ask.
- **Share as image**: the image is created on the device and only leaves it
  when you send it with the system share sheet to the app or person you
  choose. Your personal note only appears on the image if you turn on
  "Include my note".
- **Backup**: "Export journal" creates a file with your readings, notes,
  favourites and card-of-the-day history and hands it to the system share
  sheet; you decide where to save it or whom to send it to. "Import journal"
  only reads the file you choose with the system picker. The app does not
  upload these files anywhere.

This data is not transmitted to anyone unless you share it. You can delete each reading in the
Journal, or everything by clearing the app's data or uninstalling it.

### Photos (photo reading)
- "Take photo" opens the system camera; "Choose from gallery" opens the system
  photo picker, which only gives the app the photo you select (no storage or
  photo permissions are requested).
- The photo is processed **on the device**: Google ML Kit text recognition uses
  a model bundled with the app and does not send the image or the recognised
  text to any server.
- The app works on a temporary copy of the photo in its cache and **deletes it
  as soon as it has been read**. Photos are not saved in the journal.

### Third-party services
- **Google ML Kit – Text Recognition** (on-device). According to the
  [ML Kit data disclosure](https://developers.google.com/ml-kit/android-data-disclosure),
  the library sends Google, encrypted (HTTPS), technical data for diagnostics
  and usage analytics of ML Kit itself: device information (manufacturer,
  model, OS version), app information (package name and version),
  per-installation identifiers (not intended to identify a person or device),
  performance metrics, API configuration (e.g. image format and resolution),
  event type and error codes. Google states it does not transfer this data to
  third parties. It does not include the image or the text. Google's policy:
  <https://policies.google.com/privacy>.
- The camera and the photo picker are components of the operating system.

### Daily reminder (optional)
- It is off by default. If you turn it on in Settings, the app asks for
  permission to show notifications (Android 13 or later) and schedules on the
  phone itself one notification a day at the time you choose, only if you
  have not revealed your card of the day yet. You can turn it off at any time.
- Notifications are scheduled locally; no online notification service is used.

### Permissions
- No camera, photo or storage permission is requested: the system camera and
  photo picker hand the image to the app only when you choose it.
- **Notifications** (`POST_NOTIFICATIONS`): only requested when you turn on
  the daily reminder. **Device start-up** (`RECEIVE_BOOT_COMPLETED`): to
  reschedule the reminder after a restart. **Vibration**: declared by the
  notification library.
- Any Internet access listed in the technical details comes from the Google ML
  Kit libraries (diagnostics described above). The app does not use it for
  anything else.

### Children
The app is not directed at children under 13 and does not knowingly collect
personal data from anyone.

### Retention and deletion
Local data is kept until you delete it (Journal, clear app data or uninstall).
Photos are deleted automatically after being read. ML Kit diagnostics are
handled by Google under its policy.

### Illustrations
The card illustrations are the original 1909 deck by Pamela Colman Smith, in
the public domain.

### Changes
Any change will be published on this page with a new date.

### Contact
david.cheuquen@gmail.com
