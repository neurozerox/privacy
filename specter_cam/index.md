---
title: "Specter SLS Cam — Privacy Policy / Política de privacidad"
---

# Política de privacidad — Specter SLS Cam

**Fecha de entrada en vigor:** 2026-11-06
**Desarrollador:** neurozerox
**Contacto:** david.cheuquen@gmail.com

## Español

### Resumen
Specter SLS Cam es una app de entretenimiento. No tiene cuentas de usuario, no muestra anuncios, no incluye analítica ni SDK de terceros que recojan datos, y no se conecta a internet. Todo lo que la app guarda queda **solo en tu dispositivo**.

### Datos que la app trata
| Dato | Para qué | Dónde se guarda | ¿Sale del dispositivo? |
| --- | --- | --- | --- |
| Imagen de la cámara en vivo | Mostrar el visor con filtros y detectar cambios entre fotogramas (movimiento). Se procesa en memoria y se descarta al instante. | No se guarda | No |
| Fotos que capturas | Archivo interno de "evidencias" con el filtro aplicado y un sello de texto. | Almacenamiento privado de la app (PNG) | No |
| Lecturas del magnetómetro y acelerómetro | Medidor de campo magnético (µT) y rumbo. | Solo el valor del momento de cada captura, junto al registro | No |
| Notas que escribes y ajustes (idioma, paleta, modo, sensibilidad) | Funcionamiento de la app. | Preferencias locales (`shared_preferences`) | No |
| Sesiones de investigación (hora de inicio y fin, hora y valor de cada pico EMF, movimiento y captura, campo máximo, notas) | Línea de tiempo e informe de la sesión. No incluye ubicación. | Preferencias locales (`shared_preferences`) | Solo si tú lo compartes |

**Compartir:** si pulsas "Compartir foto" o "Compartir informe", la foto (PNG con su sello) o el texto del informe se entregan a la app que elijas mediante el menú de compartir del sistema. A partir de ahí, su tratamiento depende de esa app. La app nunca comparte nada por sí sola.

La app **no** recoge ubicación, contactos, identificadores del dispositivo, audio ni ningún dato personal. No vende ni comparte datos con nadie.

### Permisos
- **Cámara (`CAMERA`)**: visor en vivo, detección de movimiento y fotos. Se pide después del aviso inicial. Si lo rechazas, la app sigue funcionando como medidor magnético.
- **Sensores (magnetómetro, acelerómetro)**: no requieren permiso en Android; se usan solo mientras la app está en primer plano.
- La app no solicita micrófono, ubicación ni acceso al almacenamiento compartido. La cámara y los sensores se liberan cuando la app pasa a segundo plano.

### SDK de terceros
La app usa bibliotecas de código abierto de Flutter (`camera`, `sensors_plus`, `permission_handler`, `path_provider`, `shared_preferences`, `share_plus`) que funcionan dentro del dispositivo y no envían datos a terceros. No se integra ningún SDK de publicidad, analítica ni de reconocimiento en la nube.

### Conservación y eliminación
Los registros, fotos y sesiones se conservan hasta que los elimines desde el "Archivo Forense" o "Sesiones de investigación" (la foto se borra cuando ya no es posible deshacer) o hasta que desinstales la app o borres sus datos desde los ajustes del sistema. No existe copia en servidores.

### Menores
La app no está dirigida específicamente a menores de 13 años y no recoge datos personales de nadie.

### Cambios
Si esta política cambia, se publicará la nueva versión con su fecha de entrada en vigor.

### Contacto
david.cheuquen@gmail.com

---

## English

### Summary
Specter SLS Cam is an entertainment app. It has no user accounts, shows no ads, includes no analytics or third-party data-collecting SDKs, and does not connect to the internet. Everything the app stores stays **only on your device**.

### Data the app handles
| Data | Purpose | Where it is stored | Leaves the device? |
| --- | --- | --- | --- |
| Live camera image | Show the filtered viewfinder and detect changes between frames (motion). Processed in memory and discarded immediately. | Not stored | No |
| Photos you capture | In-app "evidence" archive with the filter applied and a text stamp. | App-private storage (PNG) | No |
| Magnetometer and accelerometer readings | Magnetic field meter (µT) and heading. | Only the value at capture time, with the log entry | No |
| Notes you type and settings (language, palette, mode, sensitivity) | App functionality. | Local preferences (`shared_preferences`) | No |
| Investigation sessions (start/end time, time and value of each EMF peak, motion and capture, max field, notes) | Session timeline and report. No location. | Local preferences (`shared_preferences`) | Only if you share it |

**Sharing:** if you tap "Share photo" or "Share report", the photo (stamped PNG) or the report text is handed to the app you pick through the system share sheet. From then on it is handled by that app. The app never shares anything on its own.

The app does **not** collect location, contacts, device identifiers, audio or any personal data. It does not sell or share data with anyone.

### Permissions
- **Camera (`CAMERA`)**: live viewfinder, motion detection and photos. Requested after the first-launch notice. If you decline, the app keeps working as a magnetic field meter.
- **Sensors (magnetometer, accelerometer)**: no permission required on Android; used only while the app is in the foreground.
- The app does not request microphone, location or shared-storage access. Camera and sensors are released when the app goes to the background.

### Third-party SDKs
The app uses open-source Flutter libraries (`camera`, `sensors_plus`, `permission_handler`, `path_provider`, `shared_preferences`, `share_plus`) that run on the device and do not send data to third parties. No advertising, analytics or cloud recognition SDK is included.

### Retention and deletion
Logs, photos and sessions are kept until you delete them from the "Forensic Archive" or "Investigation sessions" (the photo file is removed once undo is no longer possible), uninstall the app, or clear its data in the system settings. There is no server copy.

### Children
The app is not specifically directed at children under 13 and does not collect personal data from anyone.

### Changes
If this policy changes, the new version will be published with its effective date.

### Contact
david.cheuquen@gmail.com
