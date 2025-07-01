# Erstelle CSS-Styles für den CreaCheck Assistenten
css_content = """/* CreaCheck Assistent Styles */
* {
    box-sizing: border-box;
}

/* CDU Farben */
:root {
    --cdu-blue: #0d47a1;
    --cdu-light-blue: #1976d2;
    --cdu-dark-blue: #002171;
    --cdu-orange: #ff6d00;
    --cdu-light-orange: #ff9800;
    --success-green: #4caf50;
    --text-dark: #333333;
    --text-light: #666666;
    --background-light: #f5f5f5;
    --border-color: #e0e0e0;
    --white: #ffffff;
    --shadow: 0 4px 20px rgba(13, 71, 161, 0.15);
    --shadow-hover: 0 6px 25px rgba(13, 71, 161, 0.25);
}

/* Chatbot Toggle Button */
.chatbot-toggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(135deg, var(--cdu-blue), var(--cdu-light-blue));
    border: none;
    border-radius: 50px;
    padding: 12px 20px;
    box-shadow: var(--shadow);
    cursor: pointer;
    z-index: 1000;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.3s ease;
    animation: pulse 2s infinite;
}

.chatbot-toggle:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-hover);
}

@keyframes pulse {
    0% { box-shadow: var(--shadow); }
    50% { box-shadow: 0 4px 20px rgba(13, 71, 161, 0.3); }
    100% { box-shadow: var(--shadow); }
}

.chatbot-icon {
    display: flex;
    align-items: center;
    justify-content: center;
}

.chatbot-text {
    color: var(--white);
    font-weight: 600;
    font-size: 14px;
    white-space: nowrap;
}

/* Chatbot Widget */
.chatbot-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 380px;
    height: 600px;
    background: var(--white);
    border-radius: 16px;
    box-shadow: var(--shadow-hover);
    z-index: 1001;
    display: none;
    flex-direction: column;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    border: 1px solid var(--border-color);
}

.chatbot-widget.active {
    display: flex;
    animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Header */
.chatbot-header {
    background: linear-gradient(135deg, var(--cdu-blue), var(--cdu-light-blue));
    color: var(--white);
    padding: 16px;
    border-radius: 16px 16px 0 0;
}

.chatbot-header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.chatbot-avatar {
    width: 40px;
    height: 40px;
    background: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 12px;
}

.chatbot-title {
    flex: 1;
}

.chatbot-title h3 {
    margin: 0;
    font-size: 16px;
    font-weight: 600;
}

.chatbot-status {
    font-size: 12px;
    opacity: 0.8;
    display: flex;
    align-items: center;
    gap: 6px;
}

.chatbot-status::before {
    content: '';
    width: 8px;
    height: 8px;
    background: var(--success-green);
    border-radius: 50%;
    display: inline-block;
}

.chatbot-close {
    background: none;
    border: none;
    color: var(--white);
    cursor: pointer;
    padding: 8px;
    border-radius: 50%;
    transition: background-color 0.2s ease;
}

.chatbot-close:hover {
    background: rgba(255, 255, 255, 0.1);
}

/* Messages */
.chatbot-messages {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    scroll-behavior: smooth;
}

.chatbot-messages::-webkit-scrollbar {
    width: 4px;
}

.chatbot-messages::-webkit-scrollbar-track {
    background: var(--background-light);
}

.chatbot-messages::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 2px;
}

.message {
    display: flex;
    margin-bottom: 16px;
    align-items: flex-start;
    gap: 8px;
}

.message.user-message {
    flex-direction: row-reverse;
}

.message-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.bot-message .message-avatar {
    background: var(--cdu-blue);
}

.user-message .message-avatar {
    background: var(--cdu-orange);
    color: var(--white);
    font-weight: 600;
    font-size: 14px;
}

.message-content {
    max-width: 80%;
    padding: 12px 16px;
    border-radius: 16px;
    position: relative;
}

.bot-message .message-content {
    background: var(--background-light);
    border-bottom-left-radius: 4px;
}

.user-message .message-content {
    background: var(--cdu-blue);
    color: var(--white);
    border-bottom-right-radius: 4px;
}

.message-content p {
    margin: 0;
    line-height: 1.4;
    font-size: 14px;
}

.message-time {
    font-size: 11px;
    color: var(--text-light);
    margin-top: 4px;
    align-self: flex-end;
}

/* Quick Replies */
.chatbot-quick-replies {
    padding: 0 16px 8px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.quick-reply {
    background: var(--white);
    border: 1px solid var(--cdu-blue);
    color: var(--cdu-blue);
    padding: 8px 12px;
    border-radius: 20px;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.quick-reply:hover {
    background: var(--cdu-blue);
    color: var(--white);
}

/* Input */
.chatbot-input {
    border-top: 1px solid var(--border-color);
    padding: 16px;
}

.input-container {
    display: flex;
    gap: 8px;
    align-items: center;
}

#user-input {
    flex: 1;
    border: 1px solid var(--border-color);
    border-radius: 24px;
    padding: 12px 16px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s ease;
}

#user-input:focus {
    border-color: var(--cdu-blue);
}

.send-button {
    background: var(--cdu-blue);
    border: none;
    color: var(--white);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
}

.send-button:hover {
    background: var(--cdu-dark-blue);
    transform: scale(1.05);
}

.send-button:disabled {
    background: var(--border-color);
    cursor: not-allowed;
    transform: none;
}

.chatbot-footer {
    margin-top: 8px;
    text-align: center;
}

.chatbot-footer small {
    color: var(--text-light);
    font-size: 11px;
}

.chatbot-footer a {
    color: var(--cdu-blue);
    text-decoration: none;
}

.chatbot-footer a:hover {
    text-decoration: underline;
}

/* Typing Indicator */
.typing-indicator {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 12px 16px;
    background: var(--background-light);
    border-radius: 16px;
    border-bottom-left-radius: 4px;
    max-width: 80%;
}

.typing-indicator span {
    width: 8px;
    height: 8px;
    background: var(--cdu-blue);
    border-radius: 50%;
    animation: typing 1.4s ease-in-out infinite;
}

.typing-indicator span:nth-child(1) { animation-delay: 0s; }
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
    0%, 60%, 100% { opacity: 0.3; transform: scale(0.8); }
    30% { opacity: 1; transform: scale(1); }
}

/* Responsive Design */
@media (max-width: 480px) {
    .chatbot-widget {
        width: calc(100vw - 20px);
        height: calc(100vh - 40px);
        right: 10px;
        bottom: 10px;
        border-radius: 12px;
    }
    
    .chatbot-toggle {
        right: 15px;
        bottom: 15px;
    }
    
    .chatbot-text {
        display: none;
    }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
    .chatbot-toggle {
        animation: none;
    }
    
    .chatbot-widget.active {
        animation: none;
    }
    
    .typing-indicator span {
        animation: none;
    }
}

/* Focus indicators for keyboard navigation */
.chatbot-toggle:focus,
.chatbot-close:focus,
.quick-reply:focus,
.send-button:focus,
#user-input:focus {
    outline: 2px solid var(--cdu-orange);
    outline-offset: 2px;
}"""

# Speichere CSS-Datei
with open('chatbot-styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS-Datei für CreaCheck Assistenten erstellt: chatbot-styles.css")