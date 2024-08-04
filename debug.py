import json
from pippin import Client, Wallet

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

telegram_bot_token = config.get('telegram_bot_token')
banano_node = config.get('banano_node')

# Initialize the Banano client
client = Client(rpc_url=banano_node)

# Create a test wallet to verify connection
try:
    test_wallet = Wallet(client=client)
    test_address = test_wallet.accounts[0].address
    print(f"Test wallet created successfully. Address: {test_address}")
except Exception as e:
    print(f"Error creating wallet: {str(e)}")

# Output Telegram bot token (for debugging, usually you don't want to print sensitive data)
print(f"Telegram Bot Token: {telegram_bot_token}")
