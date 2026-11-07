---
title: "NecroVox — Privacy Policy / Política de privacidad"
---

# Política de privacidad — NecroVox

**Desarrollador:** neurozerox
**Fecha de entrada en vigor:** 2026-11-06
**Contacto:** david.cheuquen@gmail.com

## Español

### Resumen
NecroVox es un generador de palabras para entretenimiento que funciona con los sensores del teléfono. **No recopila, no envía y no comparte datos personales.** La app no tiene cuentas, anuncios, analítica ni acceso a internet.

### Datos que usa la app y cómo
- **Magnetómetro y acelerómetro:** se leen en tiempo real para mostrar el campo magnético (µT) y el movimiento, y para generar palabras. Las lecturas se procesan solo en el dispositivo.
- **Micrófono (opcional):** si concedes el permiso, el audio se analiza **en memoria** para calcular un único valor de nivel de sonido (dBFS) varias veces por segundo. Cada fragmento de audio se descarta inmediatamente después de medir su volumen. **No se graba, no se guarda en archivos y no se envía audio** a ningún sitio. Puedes desactivar el micrófono en Ajustes o denegar el permiso: la app sigue funcionando solo con el magnetómetro.
- **Almacenamiento local:** la app guarda en el propio dispositivo tus preferencias (idioma, paleta, voz, vibración, micrófono, sensibilidad) y el registro de palabras (palabra, hora y las lecturas numéricas de sensores de ese momento: µT, dBFS y m/s²), además de las notas que escribas para cada sesión. Estos datos no salen del dispositivo; si copias un informe al portapapeles, eres tú quien decide dónde pegarlo.
- **Voz:** las palabras se pronuncian con el motor de texto a voz instalado en el sistema (por ejemplo, el de Google o el del fabricante). La app solo le entrega la palabra que debe pronunciar. El tratamiento que haga ese motor se rige por la política de su proveedor (p. ej. Google: https://policies.google.com/privacy).

### Permisos
- `RECORD_AUDIO` (micrófono): solo para medir el nivel de sonido ambiente, como se explica arriba. Opcional.
- Los sensores de movimiento y magnetómetro no requieren permiso.

### Terceros
La app no integra SDK de anuncios, analítica ni servicios en la nube. Usa bibliotecas de código abierto que funcionan en el dispositivo (`sensors_plus`, `record`, `permission_handler`, `flutter_tts`, `shared_preferences`).

### Menores
La app no está dirigida a menores de 13 años y no recopila datos de ningún usuario.

### Conservación y eliminación
Los datos locales permanecen en tu dispositivo hasta que los borres. Puedes borrar el registro con "Limpiar registro" y eliminar todos los datos borrando los datos de la app en los ajustes del sistema o desinstalándola.

### Cambios
Si esta política cambia, se publicará la nueva versión con su fecha.

### Contacto
david.cheuquen@gmail.com

---

## English

### Summary
NecroVox is an entertainment word generator driven by the phone's sensors. **It does not collect, send or share personal data.** The app has no accounts, ads, analytics or internet access.

### Data the app uses and how
- **Magnetometer and accelerometer:** read in real time to show the magnetic field (µT) and motion, and to generate words. Readings are processed on the device only.
- **Microphone (optional):** if you grant the permission, audio is analysed **in memory** to compute a single sound level value (dBFS) several times per second. Each audio chunk is discarded immediately after its loudness is measured. **No audio is recorded, saved to files or sent** anywhere. You can turn the microphone off in Settings or deny the permission: the app keeps working with the magnetometer only.
- **Local storage:** the app stores on the device your preferences (language, palette, voice, vibration, microphone, sensitivity) and the word log (word, time and the numeric sensor readings at that moment: µT, dBFS and m/s²), plus any notes you write for each session. This data never leaves the device; if you copy a report to the clipboard, you decide where to paste it.
- **Voice:** words are spoken with the text-to-speech engine installed on the system (e.g. Google's or the manufacturer's). The app only hands it the word to pronounce. Any processing by that engine is governed by its provider's policy (e.g. Google: https://policies.google.com/privacy).

### Permissions
- `RECORD_AUDIO` (microphone): only to measure the ambient sound level, as described above. Optional.
- Motion and magnetometer sensors need no permission.

### Third parties
The app includes no advertising, analytics or cloud SDKs. It uses open-source libraries that run on the device (`sensors_plus`, `record`, `permission_handler`, `flutter_tts`, `shared_preferences`).

### Children
The app is not directed to children under 13 and collects no data from any user.

### Retention and deletion
Local data stays on your device until you delete it. You can clear the log with "Clear log" and remove all data by clearing the app's data in the system settings or uninstalling it.

### Changes
If this policy changes, the new version will be published with its date.

### Contact
david.cheuquen@gmail.com
