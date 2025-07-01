// CreaCheck Assistent Chatbot Application
class CreacheckChatbot {
    constructor() {
        this.isOpen = false;
        this.responses = {
            "rechnungen": "Ihre Rechnungen finden Sie nach dem Login im Dashboard unter \"letzte Rechnungen\" oder unter \"Funktionen\" > \"Rechnungen\". Sie können alle Rechnungen dort einsehen und herunterladen.",
            "werbemittel_erstellen": "Klicken Sie in Ihrer Kampagne auf \"neues Werbemittel anlegen\", wählen Sie das gewünschte Format aus der Übersicht und geben Sie eine Bezeichnung ein. Danach gelangen Sie direkt in den Editor.",
            "bilder_hochladen": "Klicken Sie auf ein Bildelement und wählen Sie \"Bildupload\" für neue Dateien oder \"Mediathek\" für bereits hochgeladene Bilder. Sie können den Bildausschnitt anpassen, drehen und spiegeln.",
            "seiten_hinzufuegen": "Um weitere Seiten hinzuzufügen, klicken Sie bei Faltblättern auf \"+2\" oder \"-2\", bei Broschüren auf \"+4\" oder \"-4\" unter der entsprechenden Seite in der Seitenübersicht.",
            "support": "Sie erreichen unser Support-Team per E-Mail unter dialog@creacheck.com oder telefonisch unter 0631-366-888. Unsere Öffnungszeiten sind Montag bis Freitag von 8:00 bis 17:00 Uhr.",
            "anmeldung": "CDU-Mitglieder können sich selbst registrieren. Klicken Sie einfach auf \"Neu registrieren\" und folgen Sie den Anweisungen. Sie erhalten einen Aktivierungslink per E-Mail.",
            "kampagne": "Um eine neue Kampagne anzulegen, klicken Sie in der Menüleiste auf \"Kampagnen\" > \"neue Kampagne anlegen\", vergeben Sie einen Namen und passen Sie bei Bedarf den Herausgeber an.",
            "default": "Das ist eine interessante Frage! Können Sie spezifischer beschreiben, womit ich Ihnen helfen kann? Sie können mich auch nach folgenden Themen fragen: Werbemittel erstellen, Rechnungen finden, Bilder hochladen oder Kampagnen verwalten."
        };

        this.keywords = {
            "rechnung": "rechnungen",
            "rechnungen": "rechnungen",
            "invoice": "rechnungen",
            "werbemittel": "werbemittel_erstellen",
            "erstellen": "werbemittel_erstellen",
            "anlegen": "werbemittel_erstellen",
            "design": "werbemittel_erstellen",
            "bild": "bilder_hochladen",
            "bilder": "bilder_hochladen",
            "foto": "bilder_hochladen",
            "upload": "bilder_hochladen",
            "hochladen": "bilder_hochladen",
            "seite": "seiten_hinzufuegen",
            "seiten": "seiten_hinzufuegen",
            "hilfe": "support",
            "support": "support",
            "kontakt": "support",
            "problem": "support",
            "registrieren": "anmeldung",
            "anmelden": "anmeldung",
            "account": "anmeldung",
            "kampagne": "kampagne",
            "kampagnen": "kampagne"
        };

        this.init();
    }

    init() {
        this.bindEvents();
        this.showQuickReplies();
    }

    bindEvents() {
        // Toggle chatbot
        const toggleBtn = document.getElementById('chatbotToggle');
        const minimizeBtn = document.getElementById('chatbotMinimize');
        
        toggleBtn.addEventListener('click', () => this.toggleChatbot());
        minimizeBtn.addEventListener('click', () => this.closeChatbot());

        // Send message
        const sendBtn = document.getElementById('chatbotSend');
        const inputField = document.getElementById('chatbotInput');
        
        sendBtn.addEventListener('click', () => this.sendMessage());
        inputField.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Quick replies
        const quickReplyBtns = document.querySelectorAll('.quick-reply-btn');
        quickReplyBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const key = e.target.getAttribute('data-key');
                const text = e.target.textContent;
                this.handleQuickReply(key, text);
            });
        });

        // Close chatbot when clicking outside
        document.addEventListener('click', (e) => {
            const chatbotWidget = document.getElementById('chatbotWidget');
            if (!chatbotWidget.contains(e.target) && this.isOpen) {
                // Don't close immediately to allow for better UX
            }
        });
    }

    toggleChatbot() {
        const widget = document.getElementById('chatbotWidget');
        
        if (this.isOpen) {
            this.closeChatbot();
        } else {
            this.openChatbot();
        }
    }

    openChatbot() {
        const widget = document.getElementById('chatbotWidget');
        widget.classList.add('open');
        this.isOpen = true;
        
        // Focus on input field
        setTimeout(() => {
            document.getElementById('chatbotInput').focus();
        }, 300);
    }

    closeChatbot() {
        const widget = document.getElementById('chatbotWidget');
        widget.classList.remove('open');
        this.isOpen = false;
    }

    sendMessage() {
        const inputField = document.getElementById('chatbotInput');
        const message = inputField.value.trim();
        
        if (!message) return;

        // Add user message
        this.addMessage(message, 'user');
        
        // Clear input
        inputField.value = '';
        
        // Hide quick replies after first user message
        this.hideQuickReplies();
        
        // Show typing indicator and respond
        this.showTypingIndicator();
        
        setTimeout(() => {
            this.hideTypingIndicator();
            this.respondToMessage(message);
        }, 1500 + Math.random() * 1000); // Random delay for more natural feel
    }

    handleQuickReply(key, text) {
        // Add user message
        this.addMessage(text, 'user');
        
        // Hide quick replies
        this.hideQuickReplies();
        
        // Show typing indicator and respond
        this.showTypingIndicator();
        
        setTimeout(() => {
            this.hideTypingIndicator();
            const response = this.responses[key] || this.responses.default;
            this.addMessage(response, 'bot');
            
            // Show additional quick replies after response
            setTimeout(() => this.showAdditionalQuickReplies(), 500);
        }, 1200 + Math.random() * 800);
    }

    respondToMessage(message) {
        const lowerMessage = message.toLowerCase();
        let responseKey = 'default';
        
        // Check for keywords
        for (const [keyword, key] of Object.entries(this.keywords)) {
            if (lowerMessage.includes(keyword)) {
                responseKey = key;
                break;
            }
        }
        
        const response = this.responses[responseKey];
        this.addMessage(response, 'bot');
        
        // Show additional quick replies after response
        setTimeout(() => this.showAdditionalQuickReplies(), 500);
    }

    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chatbotMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message message--${sender}`;
        
        const now = new Date();
        const timeString = now.toLocaleTimeString('de-DE', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        
        const avatarText = sender === 'bot' ? 'CA' : 'Sie';
        
        messageDiv.innerHTML = `
            <div class="message__avatar">
                <span>${avatarText}</span>
            </div>
            <div class="message__content">
                <p>${text}</p>
                <span class="message__time">${timeString}</span>
            </div>
        `;
        
        messagesContainer.appendChild(messageDiv);
        
        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    showTypingIndicator() {
        const typingIndicator = document.getElementById('chatbotTyping');
        typingIndicator.classList.add('active');
        
        // Scroll to bottom
        const messagesContainer = document.getElementById('chatbotMessages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    hideTypingIndicator() {
        const typingIndicator = document.getElementById('chatbotTyping');
        typingIndicator.classList.remove('active');
    }

    showQuickReplies() {
        const quickRepliesContainer = document.getElementById('chatbotQuickReplies');
        quickRepliesContainer.style.display = 'flex';
    }

    hideQuickReplies() {
        const quickRepliesContainer = document.getElementById('chatbotQuickReplies');
        quickRepliesContainer.style.display = 'none';
    }

    showAdditionalQuickReplies() {
        const quickRepliesContainer = document.getElementById('chatbotQuickReplies');
        
        // Create new quick reply buttons for additional help
        quickRepliesContainer.innerHTML = `
            <button class="quick-reply-btn" data-key="support">Kontakt & Support</button>
            <button class="quick-reply-btn" data-key="kampagne">Kampagne erstellen</button>
            <button class="quick-reply-btn" data-key="seiten_hinzufuegen">Seiten hinzufügen</button>
        `;
        
        // Re-bind events for new buttons
        const newBtns = quickRepliesContainer.querySelectorAll('.quick-reply-btn');
        newBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const key = e.target.getAttribute('data-key');
                const text = e.target.textContent;
                this.handleQuickReply(key, text);
            });
        });
        
        quickRepliesContainer.style.display = 'flex';
    }
}

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', () => {
    // Initialize chatbot
    new CreacheckChatbot();
    
    // Smooth scrolling for anchor links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add some interactive behavior to CTA buttons
    const ctaButtons = document.querySelectorAll('.btn');
    ctaButtons.forEach(button => {
        if (!button.classList.contains('chatbot-toggle') && 
            !button.classList.contains('chatbot-minimize') &&
            !button.classList.contains('chatbot-input__send')) {
            button.addEventListener('click', (e) => {
                // Simulate button action for demo
                const originalText = button.textContent;
                button.textContent = 'Wird geladen...';
                button.disabled = true;
                
                setTimeout(() => {
                    button.textContent = originalText;
                    button.disabled = false;
                    
                    // Show a simple notification
                    showNotification('Vielen Dank für Ihr Interesse! In der echten Anwendung würden Sie jetzt weitergeleitet.');
                }, 2000);
            });
        }
    });
});

// Simple notification system
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: var(--cdu-blue);
        color: white;
        padding: 16px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 10000;
        max-width: 350px;
        font-size: 14px;
        line-height: 1.4;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after delay
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 4000);
}

// Add some scroll effects
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.backgroundColor = 'rgba(13, 71, 161, 0.95)';
        header.style.backdropFilter = 'blur(10px)';
    } else {
        header.style.backgroundColor = 'var(--cdu-blue)';
        header.style.backdropFilter = 'none';
    }
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe feature cards for scroll animations
document.addEventListener('DOMContentLoaded', () => {
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});

// Handle resize events for chatbot responsiveness
window.addEventListener('resize', () => {
    const chatbotContainer = document.querySelector('.chatbot-container');
    if (window.innerWidth <= 480 && chatbotContainer) {
        chatbotContainer.style.width = `${window.innerWidth - 32}px`;
    }
});