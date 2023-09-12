import csv
from telethon.sync import TelegramClient
from telethon.tl import functions, types

# Replace these with your own values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Create a new session file or use an existing one
session_file = 'telegram_session'
client = TelegramClient(session_file, api_id, api_hash)

async def main():
    # Start the Telegram client
    await client.start(phone_number)
    
    # Specify the chat entity (replace with your chat)
    chat_entity = await client.get_entity('https://t.me/YOUR_CHAT_USERNAME')
    
    # Fetch all messages from the chat
    messages = await client.get_messages(chat_entity, limit=None)
    
    # Create a CSV file to write messages
    with open('telegram_chat_messages.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write header
        csv_writer.writerow(['Message ID', 'Date', 'Sender', 'Message'])
        
        # Write messages to the CSV file
        for message in messages:
            if isinstance(message, types.Message):
                sender = message.sender_id.user_id if message.sender_id else ''
                csv_writer.writerow([message.id, message.date, sender, message.text])
    
    print('Messages have been successfully exported to telegram_chat_messages.csv')

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
