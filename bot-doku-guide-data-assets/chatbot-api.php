<?php
/**
 * CreaCheck Assistent API Backend
 * Version: 1.0.0
 * 
 * Dieses PHP-Script behandelt die Chatbot-Anfragen und 
 * kann mit OpenAI GPT oder anderen KI-Services integriert werden.
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight requests
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

class CreaCheckChatbotAPI {
    private $openai_api_key;
    private $knowledge_base;

    public function __construct() {
        // OpenAI API Key (aus Umgebungsvariablen oder Config laden)
        $this->openai_api_key = getenv('OPENAI_API_KEY') ?: 'your-openai-api-key-here';
        $this->loadKnowledgeBase();
    }

    private function loadKnowledgeBase() {
        // Lade CreaCheck-spezifische Wissensdatenbank
        $this->knowledge_base = [
            'creacheck_info' => "CreaCheck ist ein webbasiertes All-in-One-Designtool für die Erstellung von professionellen Medien auf Basis des Corporate Designs der CDU. Es automatisiert Gestaltungsarbeiten und ermöglicht eine Zeitersparnis von bis zu 90%.",

            'wahlkampf_context' => "CreaCheck wird von CDU-Kandidaten für Kommunalwahlen eingesetzt. Das System bietet einheitliches Corporate Design, hohe Flexibilität bei der Mediengestaltung und schnelle Erstellung von Wahlkampfmaterialien.",

            'system_prompt' => "Du bist der CreaCheck Assistent für CDU-Wahlkampfkandidaten. Du hilfst bei Fragen rund um das CreaCheck-Portal, die Erstellung von Werbemitteln, Kampagnen-Management und technische Unterstützung. Antworte freundlich, präzise und praxisorientiert auf Deutsch.",

            'quick_answers' => [
                'rechnungen' => 'Ihre Rechnungen finden Sie nach dem Login im Dashboard unter "letzte Rechnungen" oder unter "Funktionen" > "Rechnungen".',
                'werbemittel_erstellen' => 'Klicken Sie in Ihrer Kampagne auf "neues Werbemittel anlegen", wählen Sie das gewünschte Format und geben Sie eine Bezeichnung ein.',
                'bilder_hochladen' => 'Klicken Sie auf ein Bildelement und wählen Sie "Bildupload" für neue Dateien oder "Mediathek" für bereits hochgeladene Bilder.',
                'support_kontakt' => 'Sie erreichen unser Support-Team per E-Mail unter dialog@creacheck.com oder telefonisch unter 0631-366-888 (Mo-Fr, 8-17 Uhr).'
            ]
        ];
    }

    public function handleRequest() {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            $this->sendError('Only POST requests allowed', 405);
            return;
        }

        $input = json_decode(file_get_contents('php://input'), true);

        if (!isset($input['message'])) {
            $this->sendError('Message parameter required', 400);
            return;
        }

        $user_message = trim($input['message']);
        $conversation_history = $input['history'] ?? [];

        // Prüfe zunächst auf schnelle Antworten
        $quick_response = $this->getQuickResponse($user_message);
        if ($quick_response) {
            $this->sendResponse($quick_response);
            return;
        }

        // Falls keine schnelle Antwort gefunden wurde, nutze OpenAI
        $ai_response = $this->getAIResponse($user_message, $conversation_history);
        $this->sendResponse($ai_response);
    }

    private function getQuickResponse($message) {
        $message_lower = strtolower($message);

        // Keyword-basierte Antworten
        $keywords = [
            'rechnung' => 'rechnungen',
            'werbemittel' => 'werbemittel_erstellen',
            'bild' => 'bilder_hochladen',
            'support' => 'support_kontakt',
            'hilfe' => 'support_kontakt'
        ];

        foreach ($keywords as $keyword => $response_key) {
            if (strpos($message_lower, $keyword) !== false) {
                return $this->knowledge_base['quick_answers'][$response_key];
            }
        }

        return null;
    }

    private function getAIResponse($user_message, $conversation_history) {
        if (empty($this->openai_api_key) || $this->openai_api_key === 'your-openai-api-key-here') {
            return $this->getFallbackResponse($user_message);
        }

        // Bereite Konversation für OpenAI vor
        $messages = [
            [
                'role' => 'system',
                'content' => $this->knowledge_base['system_prompt'] . "

" . 
                           "Kontext: " . $this->knowledge_base['creacheck_info'] . "
" .
                           "Wahlkampf-Kontext: " . $this->knowledge_base['wahlkampf_context']
            ]
        ];

        // Füge Gesprächsverlauf hinzu (nur die letzten 10 Nachrichten)
        $recent_history = array_slice($conversation_history, -10);
        foreach ($recent_history as $msg) {
            $messages[] = [
                'role' => $msg['role'] === 'user' ? 'user' : 'assistant',
                'content' => $msg['content']
            ];
        }

        // Aktuelle Benutzernachricht
        $messages[] = [
            'role' => 'user',
            'content' => $user_message
        ];

        // OpenAI API Aufruf
        $response = $this->callOpenAI($messages);
        return $response ?: $this->getFallbackResponse($user_message);
    }

    private function callOpenAI($messages) {
        $url = 'https://api.openai.com/v1/chat/completions';

        $data = [
            'model' => 'gpt-3.5-turbo',
            'messages' => $messages,
            'max_tokens' => 500,
            'temperature' => 0.7,
            'presence_penalty' => 0.1,
            'frequency_penalty' => 0.1
        ];

        $headers = [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $this->openai_api_key
        ];

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 30);

        $response = curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        if ($http_code === 200 && $response) {
            $decoded = json_decode($response, true);
            if (isset($decoded['choices'][0]['message']['content'])) {
                return trim($decoded['choices'][0]['message']['content']);
            }
        }

        // Log Fehler
        error_log("OpenAI API Fehler: HTTP $http_code, Response: $response");
        return null;
    }

    private function getFallbackResponse($message) {
        $fallback_responses = [
            "Vielen Dank für Ihre Frage! Für eine detaillierte Antwort wenden Sie sich bitte an unser Support-Team unter dialog@creacheck.com oder 0631-366-888.",
            "Das ist eine interessante Frage zu CreaCheck. Unser Support-Team kann Ihnen sicher weiterhelfen: dialog@creacheck.com oder 0631-366-888 (Mo-Fr, 8-17 Uhr).",
            "Entschuldigung, ich kann Ihnen zu diesem spezifischen Thema keine detaillierte Antwort geben. Kontaktieren Sie bitte unser Support-Team für individuelle Hilfe."
        ];

        return $fallback_responses[array_rand($fallback_responses)];
    }

    private function sendResponse($message) {
        $response = [
            'success' => true,
            'response' => $message,
            'timestamp' => date('c')
        ];

        echo json_encode($response, JSON_UNESCAPED_UNICODE);
    }

    private function sendError($message, $code = 400) {
        http_response_code($code);
        $response = [
            'success' => false,
            'error' => $message,
            'timestamp' => date('c')
        ];

        echo json_encode($response, JSON_UNESCAPED_UNICODE);
    }

    // Logging für Analytics
    private function logConversation($user_message, $bot_response) {
        $log_entry = [
            'timestamp' => date('c'),
            'user_message' => $user_message,
            'bot_response' => $bot_response,
            'ip' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
            'user_agent' => $_SERVER['HTTP_USER_AGENT'] ?? 'unknown'
        ];

        // Log in Datei oder Datenbank
        file_put_contents(
            'chatbot_logs.json', 
            json_encode($log_entry) . "
", 
            FILE_APPEND | LOCK_EX
        );
    }
}

// API Endpoint
try {
    $api = new CreaCheckChatbotAPI();
    $api->handleRequest();
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Internal server error',
        'timestamp' => date('c')
    ]);

    error_log("Chatbot API Error: " . $e->getMessage());
}
?>