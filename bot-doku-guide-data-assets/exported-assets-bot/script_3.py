# Erstelle JavaScript für den CreaCheck Assistenten
js_content = """/**
 * CreaCheck Assistent - Chatbot Widget
 * Version: 1.0.0
 * Author: CreaCheck GmbH
 */

class CreaCheckAssistant {
    constructor() {
        this.isOpen = false;
        this.isTyping = false;
        this.knowledgeBase = this.initializeKnowledgeBase();
        this.conversationHistory = [];
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadWelcomeMessage();
        console.log('CreaCheck Assistent initialisiert');
    }

    bindEvents() {
        // Toggle Button Event
        const toggleBtn = document.getElementById('chatbot-button');
        toggleBtn.addEventListener('click', () => this.toggleWidget());

        // Close Button Event
        const closeBtn = document.getElementById('chatbot-close');
        closeBtn.addEventListener('click', () => this.closeWidget());

        // Send Button Event
        const sendBtn = document.getElementById('send-button');
        sendBtn.addEventListener('click', () => this.sendMessage());

        // Input Enter Key Event
        const input = document.getElementById('user-input');
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        // Quick Reply Events
        const quickReplies = document.querySelectorAll('.quick-reply');
        quickReplies.forEach(btn => {
            btn.addEventListener('click', () => {
                const message = btn.getAttribute('data-message');
                this.sendUserMessage(message);
            });
        });

        // Click outside to close
        document.addEventListener('click', (e) => {
            const widget = document.getElementById('chatbot-widget');
            const toggleBtn = document.getElementById('chatbot-button');
            
            if (this.isOpen && 
                !widget.contains(e.target) && 
                !toggleBtn.contains(e.target)) {
                this.closeWidget();
            }
        });
    }

    initializeKnowledgeBase() {
        return {
            'rechnungen': {
                keywords: ['rechnung', 'rechnungen', 'bezahlung', 'zahlung', 'invoice'],
                response: 'Ihre Rechnungen finden Sie nach dem Login im Dashboard unter "letzte Rechnungen" oder unter "Funktionen" > "Rechnungen". Sie können alle Rechnungen dort einsehen und herunterladen.'
            },
            'anmeldung': {
                keywords: ['anmeldung', 'registrierung', 'login', 'zugang', 'anmelden'],
                response: 'CDU-Mitglieder können sich selbst registrieren. Klicken Sie einfach auf "Neu registrieren" und folgen Sie den Anweisungen. Sie erhalten einen Aktivierungslink per E-Mail.'
            },
            'passwort': {
                keywords: ['passwort', 'kennwort', 'ändern', 'vergessen', 'password'],
                response: 'Sie können Ihr Passwort unter "Profil" > "Passwort ändern" > "speichern" ändern. Falls Sie Ihr Passwort vergessen haben, klicken Sie auf "Passwort vergessen" auf der Login-Seite.'
            },
            'werbemittel_erstellen': {
                keywords: ['werbemittel', 'erstellen', 'neu', 'anlegen', 'material'],
                response: 'Um ein neues Werbemittel zu erstellen, klicken Sie in Ihrer Kampagne auf "neues Werbemittel anlegen", wählen Sie das gewünschte Format aus der Übersicht und geben Sie eine Bezeichnung ein. Danach gelangen Sie direkt in den Editor.'
            },
            'werbemittel_arten': {
                keywords: ['auswahl', 'verfügbar', 'arten', 'typen', 'formate'],
                response: 'CreaCheck bietet eine große Auswahl an Werbemitteln: Flyer, Plakate, Social Media Posts, Visitenkarten, Broschüren, Landingpages, Anzeigen, Give-Aways und vieles mehr. Alle entsprechen automatisch dem CDU Corporate Design.'
            },
            'bestellen': {
                keywords: ['bestellen', 'warenkorb', 'bestellung', 'order'],
                response: 'Sie können Werbemittel auf zwei Wege bestellen: 1) Im Editor über den "Bestellen"-Button oder 2) In der Kampagnenübersicht über "in den Warenkorb". Wählen Sie dann Auflage, Lieferzeit und Zahlungsart aus.'
            },
            'lieferzeit': {
                keywords: ['lieferzeit', 'versand', 'dauer', 'schnell', 'express'],
                response: 'Es gibt drei Lieferoptionen: Standard (mehrere Werktage), Express (Bestellung bis 11:30 Uhr) und Overnight (Bestellung bis 9:30 Uhr). Die genauen Zeiten werden im Bestellprozess angezeigt.'
            },
            'seiten_hinzufügen': {
                keywords: ['seiten', 'hinzufügen', 'mehr', 'zusätzlich', 'pages'],
                response: 'Um weitere Seiten hinzuzufügen, klicken Sie bei Faltblättern auf "+2" oder "-2", bei Broschüren auf "+4" oder "-4" unter der entsprechenden Seite in der Seitenübersicht.'
            },
            'text_bearbeiten': {
                keywords: ['text', 'bearbeiten', 'formatierung', 'schrift', 'writing'],
                response: 'Klicken Sie in das gewünschte Textfeld. Die Formatierungsoptionen erscheinen automatisch entsprechend dem Corporate Design. Sie können Überschriften, Absätze, Schriftschnitte und Ausrichtung anpassen.'
            },
            'bilder_hochladen': {
                keywords: ['bilder', 'hochladen', 'upload', 'fotos', 'images'],
                response: 'Klicken Sie auf ein Bildelement und wählen Sie "Bildupload" für neue Dateien oder "Mediathek" für bereits hochgeladene Bilder. Sie können den Bildausschnitt anpassen, drehen und spiegeln.'
            },
            'speichern': {
                keywords: ['speichern', 'sichern', 'automatisch', 'save'],
                response: 'Das System speichert automatisch alle 5 Minuten. Sie können auch jederzeit manuell über den "Speichern"-Button sichern. Verwenden Sie "Speichern unter" um das Werbemittel in einer anderen Kampagne zu sichern.'
            },
            'mediathek': {
                keywords: ['mediathek', 'ordner', 'organisation', 'struktur'],
                response: 'In der Mediathek können Sie Ordnerstrukturen anlegen, Bilder hochladen und verwalten. Klicken Sie auf "neuer Ordner" um Ordner zu erstellen und "Medien Hochladen" um Bilder hinzuzufügen.'
            },
            'kampagne': {
                keywords: ['kampagne', 'anlegen', 'erstellen', 'neu'],
                response: 'Um eine neue Kampagne anzulegen, klicken Sie in der Menüleiste auf "Kampagnen" > "neue Kampagne anlegen", vergeben Sie einen Namen und passen Sie bei Bedarf den Herausgeber an.'
            },
            'landingpage': {
                keywords: ['landingpage', 'webseite', 'website', 'online'],
                response: 'Wählen Sie bei "neues Werbemittel anlegen" eine Landingpage-Vorlage aus. Sie können Kontaktformulare, Social Media Links, Google Maps und viele weitere interaktive Elemente hinzufügen.'
            },
            'support': {
                keywords: ['support', 'hilfe', 'kontakt', 'help'],
                response: 'Sie erreichen unser Support-Team per E-Mail unter dialog@creacheck.com oder telefonisch unter 0631-366-888. Unsere Öffnungszeiten sind Montag bis Freitag von 8:00 bis 17:00 Uhr.'
            }
        };
    }

    toggleWidget() {
        if (this.isOpen) {
            this.closeWidget();
        } else {
            this.openWidget();
        }
    }

    openWidget() {
        const widget = document.getElementById('chatbot-widget');
        const toggleBtn = document.getElementById('chatbot-button');
        
        widget.classList.add('active');
        toggleBtn.style.display = 'none';
        this.isOpen = true;
        
        // Focus auf Input setzen
        setTimeout(() => {
            document.getElementById('user-input').focus();
        }, 300);
    }

    closeWidget() {
        const widget = document.getElementById('chatbot-widget');
        const toggleBtn = document.getElementById('chatbot-button');
        
        widget.classList.remove('active');
        toggleBtn.style.display = 'flex';
        this.isOpen = false;
    }

    sendMessage() {
        const input = document.getElementById('user-input');
        const message = input.value.trim();
        
        if (message) {
            this.sendUserMessage(message);
            input.value = '';
        }
    }

    sendUserMessage(message) {
        this.addMessage(message, 'user');
        this.conversationHistory.push({ role: 'user', content: message });
        
        // Bot-Antwort nach kurzer Verzögerung
        setTimeout(() => {
            this.showTypingIndicator();
            setTimeout(() => {
                this.hideTypingIndicator();
                const botResponse = this.generateResponse(message);
                this.addMessage(botResponse, 'bot');
                this.conversationHistory.push({ role: 'bot', content: botResponse });
            }, 1500);
        }, 500);
    }

    addMessage(content, sender) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        
        if (sender === 'bot') {
            avatar.innerHTML = `
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C17.5228 2 22 6.47715 22 12V20.5C22 20.7761 21.7761 21 21.5 21H12C6.47715 21 2 16.5228 2 12C2 6.47715 6.47715 2 12 2Z" fill="#0d47a1"/>
                    <circle cx="9" cy="10" r="1" fill="white"/>
                    <circle cx="15" cy="10" r="1" fill="white"/>
                    <path d="M8 14C8 15.1046 9.79086 16 12 16C14.2091 16 16 15.1046 16 14" stroke="white" stroke-width="1" stroke-linecap="round"/>
                </svg>
            `;
        } else {
            avatar.textContent = '👤';
        }
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = `<p>${this.formatMessage(content)}</p>`;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = this.getCurrentTime();
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        
        messagesContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }

    formatMessage(message) {
        // Einfache Formatierung für Links und wichtige Begriffe
        return message
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/\n/g, '<br>');
    }

    generateResponse(userMessage) {
        const message = userMessage.toLowerCase();
        
        // Durchsuche Knowledge Base
        for (const [key, data] of Object.entries(this.knowledgeBase)) {
            if (data.keywords.some(keyword => message.includes(keyword))) {
                return data.response;
            }
        }
        
        // Allgemeine Antworten für nicht erkannte Anfragen
        const generalResponses = [
            'Das ist eine interessante Frage! Können Sie spezifischer beschreiben, womit ich Ihnen helfen kann? Sie können mich auch nach folgenden Themen fragen: Werbemittel erstellen, Rechnungen finden, Bilder hochladen oder Kampagnen verwalten.',
            'Entschuldigung, ich habe Ihre Frage nicht ganz verstanden. Versuchen Sie es mit konkreteren Begriffen wie "Werbemittel", "Rechnung", "Mediathek" oder "Kampagne". Unser Support-Team hilft Ihnen gerne unter dialog@creacheck.com weiter.',
            'Leider kann ich Ihnen zu diesem Thema keine spezifische Antwort geben. Für detaillierte Hilfe wenden Sie sich bitte an unser Support-Team unter 0631-366-888 oder dialog@creacheck.com.'
        ];
        
        return generalResponses[Math.floor(Math.random() * generalResponses.length)];
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatbot-messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        typingDiv.id = 'typing-indicator';
        
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C17.5228 2 22 6.47715 22 12V20.5C22 20.7761 21.7761 21 21.5 21H12C6.47715 21 2 16.5228 2 12C2 6.47715 6.47715 2 12 2Z" fill="#0d47a1"/>
                    <circle cx="9" cy="10" r="1" fill="white"/>
                    <circle cx="15" cy="10" r="1" fill="white"/>
                    <path d="M8 14C8 15.1046 9.79086 16 12 16C14.2091 16 16 15.1046 16 14" stroke="white" stroke-width="1" stroke-linecap="round"/>
                </svg>
            </div>
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;
        
        messagesContainer.appendChild(typingDiv);
        this.scrollToBottom();
        this.isTyping = true;
    }

    hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
        this.isTyping = false;
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbot-messages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString('de-DE', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
    }

    loadWelcomeMessage() {
        // Willkommensnachricht ist bereits im HTML definiert
        this.conversationHistory.push({
            role: 'bot',
            content: 'Willkommensnachricht geladen'
        });
    }

    // API Integration für erweiterte Funktionen
    async sendToAPI(message) {
        try {
            // Beispiel für API-Aufruf (zu implementieren)
            const response = await fetch('/api/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    history: this.conversationHistory
                })
            });
            
            if (response.ok) {
                const data = await response.json();
                return data.response;
            }
        } catch (error) {
            console.warn('API-Aufruf fehlgeschlagen, verwende lokale Antworten:', error);
        }
        
        return null;
    }

    // Analytik und Tracking
    trackEvent(event, data) {
        // Beispiel für Event-Tracking
        if (typeof gtag !== 'undefined') {
            gtag('event', event, {
                'custom_parameter': data
            });
        }
        
        console.log('Chatbot Event:', event, data);
    }
}

// Initialisierung nach DOM-Load
document.addEventListener('DOMContentLoaded', () => {
    window.creaCheckAssistant = new CreaCheckAssistant();
});

// Export für Module
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CreaCheckAssistant;
}"""

# Speichere JavaScript-Datei
with open('chatbot-script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("JavaScript-Datei für CreaCheck Assistenten erstellt: chatbot-script.js")