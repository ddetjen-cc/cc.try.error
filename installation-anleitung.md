# CreaCheck Assistent - Installationsanleitung

## Übersicht

Der CreaCheck Assistent ist ein intelligenter Chatbot, der speziell für die CDU-Wahlkampf-Website entwickelt wurde. Er unterstützt Benutzer bei Fragen rund um das CreaCheck-Portal und bietet sofortigen Support.

## Systemanforderungen

### Frontend
- Moderne Webbrowser (Chrome, Firefox, Safari, Edge)
- JavaScript aktiviert
- Responsive Design für Mobile und Desktop

### Backend (Optional für erweiterte Funktionen)
- PHP 7.4 oder höher
- cURL-Erweiterung
- OpenAI API Key (optional für KI-Integration)
- HTTPS-Verbindung empfohlen

## Installation

### Schritt 1: Dateien hochladen

Laden Sie folgende Dateien in Ihr Webverzeichnis hoch:

```
/chatbot/
├── chatbot-widget.html
├── chatbot-styles.css
├── chatbot-script.js
├── chatbot-api.php (optional)
└── creacheck_chatbot_knowledge_base.csv
```

### Schritt 2: Integration in bestehende Website

#### Option A: Vollständige Widget-Integration

Fügen Sie folgenden Code vor dem schließenden `</body>`-Tag Ihrer Website ein:

```html
<!-- CreaCheck Assistent -->
<link rel="stylesheet" href="/chatbot/chatbot-styles.css">

<!-- Chatbot Widget Button -->
<div id="chatbot-button" class="chatbot-toggle">
    <div class="chatbot-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C17.5228 2 22 6.47715 22 12V20.5C22 20.7761 21.7761 21 21.5 21H12C6.47715 21 2 16.5228 2 12C2 6.47715 6.47715 2 12 2Z" fill="white"/>
            <circle cx="9" cy="10" r="1.5" fill="#0d47a1"/>
            <circle cx="15" cy="10" r="1.5" fill="#0d47a1"/>
            <path d="M8 14C8 15.1046 9.79086 16 12 16C14.2091 16 15.1046 16 14" stroke="#0d47a1" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
    </div>
    <div class="chatbot-text">
        <span>Fragen?</span>
    </div>
</div>

<!-- Komplettes Chatbot Widget hier einfügen -->
<!-- Siehe chatbot-widget.html für vollständigen Code -->

<script src="/chatbot/chatbot-script.js"></script>
```

#### Option B: Iframe-Integration

Für eine einfachere Integration verwenden Sie ein Iframe:

```html
<iframe 
    src="/chatbot/chatbot-widget.html" 
    style="position: fixed; bottom: 20px; right: 20px; width: 380px; height: 600px; border: none; z-index: 1000;"
    title="CreaCheck Assistent">
</iframe>
```

### Schritt 3: Backend-Konfiguration (Optional)

#### OpenAI API Setup

1. Erstellen Sie einen Account bei OpenAI (https://platform.openai.com)
2. Generieren Sie einen API-Key
3. Setzen Sie die Umgebungsvariable oder bearbeiten Sie `chatbot-api.php`:

```php
// In chatbot-api.php
$this->openai_api_key = 'your-actual-openai-api-key';
```

#### Server-Konfiguration

Stellen Sie sicher, dass Ihr Server folgende PHP-Erweiterungen unterstützt:
- cURL
- JSON
- mbstring

#### CORS-Konfiguration

Für Cross-Origin-Requests fügen Sie folgende Header hinzu:

```apache
# .htaccess
Header always set Access-Control-Allow-Origin "*"
Header always set Access-Control-Allow-Methods "POST, GET, OPTIONS"
Header always set Access-Control-Allow-Headers "Content-Type"
```

### Schritt 4: Anpassungen

#### Design-Anpassungen

Bearbeiten Sie `chatbot-styles.css` um das Design anzupassen:

```css
:root {
    --cdu-blue: #0d47a1;          /* Primärfarbe */
    --cdu-light-blue: #1976d2;    /* Sekundärfarbe */
    --cdu-orange: #ff6d00;        /* Akzentfarbe */
}
```

#### Inhalt-Anpassungen

Bearbeiten Sie die Wissensdatenbank in `chatbot-script.js`:

```javascript
// Neue Einträge zur Knowledge Base hinzufügen
'neues_thema': {
    keywords: ['keyword1', 'keyword2'],
    response: 'Ihre Antwort hier...'
}
```

## Konfigurationsmöglichkeiten

### JavaScript-Konfiguration

```javascript
// In chatbot-script.js
const CONFIG = {
    API_ENDPOINT: '/chatbot/chatbot-api.php',
    TYPING_DELAY: 1500,
    AUTO_CLOSE_DELAY: 300000, // 5 Minuten
    MAX_MESSAGE_LENGTH: 500,
    ENABLE_ANALYTICS: true
};
```

### CSS-Anpassungen

```css
/* Position des Chatbot-Buttons ändern */
.chatbot-toggle {
    bottom: 20px;     /* Abstand von unten */
    right: 20px;      /* Abstand von rechts */
    left: auto;       /* Für links: left: 20px; right: auto; */
}

/* Widget-Größe anpassen */
.chatbot-widget {
    width: 380px;     /* Breite */
    height: 600px;    /* Höhe */
}
```

## Sicherheit und Datenschutz

### Datenschutz-Überlegungen

1. **Logging**: Konversationen werden nur temporär gespeichert
2. **IP-Adressen**: Werden nur für Analytics erfasst (optional)
3. **Cookies**: Keine Cookies werden vom Chatbot gesetzt
4. **DSGVO-Compliance**: Implementieren Sie entsprechende Hinweise

### Empfohlene Datenschutz-Einstellungen

```php
// In chatbot-api.php
class CreaCheckChatbotAPI {
    private $log_conversations = false;  // Deaktiviert Logging
    private $store_ip_addresses = false; // Keine IP-Speicherung
    private $anonymize_data = true;      // Daten anonymisieren
}
```

## Wartung und Updates

### Regelmäßige Aufgaben

1. **Log-Dateien prüfen**: Überprüfen Sie `chatbot_logs.json` auf Fehler
2. **Knowledge Base aktualisieren**: Erweitern Sie die Wissensdatenbank
3. **Performance überwachen**: Prüfen Sie Antwortzeiten
4. **Backup erstellen**: Sichern Sie Konfigurationen regelmäßig

### Update-Prozess

1. Backup der aktuellen Dateien erstellen
2. Neue Dateien hochladen
3. Konfigurationen übertragen
4. Funktionalität testen
5. Cache leeren

## Fehlerbehebung

### Häufige Probleme

#### Chatbot öffnet sich nicht
- JavaScript-Konsole auf Fehler prüfen
- CSS-Dateien korrekt geladen?
- Pfade zu Dateien überprüfen

#### API-Aufrufe fehlschlagen
- PHP-Fehlerlog prüfen
- OpenAI API-Key validieren
- cURL-Erweiterung installiert?
- CORS-Header korrekt gesetzt?

#### Styling-Probleme
- CSS-Spezifität prüfen
- Browser-Cache leeren
- Responsive Design auf verschiedenen Geräten testen

### Debug-Modus aktivieren

```javascript
// In chatbot-script.js
const DEBUG_MODE = true;

// Debugging in der Browser-Konsole
if (DEBUG_MODE) {
    console.log('Chatbot Debug Modus aktiviert');
}
```

## Support und Kontakt

Bei Fragen zur Installation und Konfiguration wenden Sie sich an:

- **E-Mail**: dialog@creacheck.com
- **Telefon**: 0631-366-888
- **Öffnungszeiten**: Montag bis Freitag, 8:00 - 17:00 Uhr

## Erweiterte Funktionen

### Analytics-Integration

```javascript
// Google Analytics Integration
gtag('event', 'chatbot_interaction', {
    'event_category': 'chatbot',
    'event_label': 'message_sent'
});
```

### Multi-Language Support

Für mehrsprachige Unterstützung erweitern Sie die Knowledge Base:

```javascript
const LANGUAGES = {
    'de': {
        welcome_message: 'Willkommen beim CreaCheck Assistenten',
        // weitere Übersetzungen...
    },
    'en': {
        welcome_message: 'Welcome to CreaCheck Assistant',
        // weitere Übersetzungen...
    }
};
```

### Custom Branding

Für andere Organisationen können Sie das Branding anpassen:

```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-secondary-color;
    --brand-name: 'Ihr Markenname';
}
```

## Performance-Optimierung

### Empfohlene Optimierungen

1. **CSS/JS Minifizierung**: Komprimieren Sie die Dateien für Produktion
2. **CDN-Integration**: Laden Sie Assets über CDN
3. **Lazy Loading**: Laden Sie den Chatbot erst bei Bedarf
4. **Caching**: Implementieren Sie Browser-Caching

### Monitoring

Überwachen Sie folgende Metriken:
- Antwortzeiten der API
- Anzahl der Konversationen
- Häufigste Fragen
- Benutzer-Zufriedenheit

---

**Version**: 1.0.0  
**Letzte Aktualisierung**: Juni 2025  
**Kompatibilität**: Alle modernen Webbrowser