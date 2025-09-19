import os
import requests
from flask import Blueprint, request, jsonify

telegram_bp = Blueprint('telegram', __name__)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    """Send a message to a Telegram chat."""
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

@telegram_bp.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming Telegram webhook updates."""
    try:
        update = request.get_json()
        
        # Check if the update contains a message
        if 'message' in update:
            message = update['message']
            chat_id = message['chat']['id']
            
            # Check if the message has text
            if 'text' in message:
                # Reply with "وعليكم السلام" to any message
                send_message(chat_id, "وعليكم السلام")
        
        return jsonify({'status': 'ok'}), 200
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@telegram_bp.route('/set_webhook', methods=['POST'])
def set_webhook():
    """Set the webhook URL for the bot."""
    webhook_url = request.json.get('webhook_url')
    
    if not webhook_url:
        return jsonify({'error': 'webhook_url is required'}), 400
    
    url = f"{TELEGRAM_API_URL}/setWebhook"
    payload = {'url': webhook_url}
    
    try:
        response = requests.post(url, json=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@telegram_bp.route('/get_webhook_info', methods=['GET'])
def get_webhook_info():
    """Get current webhook information."""
    url = f"{TELEGRAM_API_URL}/getWebhookInfo"
    
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@telegram_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'bot_token_set': bool(BOT_TOKEN)}), 200

