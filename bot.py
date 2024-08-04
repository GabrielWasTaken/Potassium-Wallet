import json
from telegram.ext import Updater, CommandHandler, JobQueue
import pippin

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

TELEGRAM_BOT_TOKEN = config.get('telegram_bot_token')
BANANO_NODE = config.get('banano_node')
client = Client(rpc_url=BANANO_NODE)

# Dictionary to store user wallets
user_wallets = {}

# Function to start the bot and create a wallet
def start(update, context):
    user_id = update.message.from_user.id
    if user_id not in user_wallets:
        wallet = Wallet(client=client)
        user_wallets[user_id] = wallet
        seed = wallet.seed
        address = wallet.accounts[0].address
        update.message.reply_text(f'Your wallet has been created!\n\nSeed: {seed}\nAddress: {address}')
    else:
        update.message.reply_text(f'You already have a wallet!\nAddress: {user_wallets[user_id].accounts[0].address}')

# Function to add an additional account to the wallet
def add_account(update, context):
    user_id = update.message.from_user.id
    if user_id in user_wallets:
        wallet = user_wallets[user_id]
        new_account = wallet.new_account()
        update.message.reply_text(f'New account added!\nAddress: {new_account.address}')
    else:
        update.message.reply_text('You need to create a wallet first with /start.')

# Function to check balance
def balance(update, context):
    user_id = update.message.from_user.id
    if user_id in user_wallets:
        account = user_wallets[user_id].accounts[0]
        account.update()
        bal = account.balance
        update.message.reply_text(f'Your current balance is: {bal} BAN')
    else:
        update.message.reply_text('You need to create a wallet first with /start.')

# Function to send BAN
def send(update, context):
    user_id = update.message.from_user.id
    if user_id in user_wallets:
        try:
            recipient_address = context.args[0]
            amount = context.args[1]
            account = user_wallets[user_id].accounts[0]
            account.send(recipient_address, amount)
            update.message.reply_text(f'Successfully sent {amount} BAN to {recipient_address}')
        except (IndexError, ValueError):
            update.message.reply_text('Usage: /send <recipient_address> <amount>')
        except Exception as e:
            update.message.reply_text(f'Failed to send BAN: {str(e)}')
    else:
        update.message.reply_text('You need to create a wallet first with /start.')

# Function to request BAN (generate a receive address)
def request_ban(update, context):
    user_id = update.message.from_user.id
    if user_id in user_wallets:
        address = user_wallets[user_id].accounts[0].address
        update.message.reply_text(f'Send BAN to this address: {address}')
    else:
        update.message.reply_text('You need to create a wallet first with /start.')

# Function to automatically receive pending transactions
def auto_receive(context):
    user_id = context.job.context
    if user_id in user_wallets:
        wallet = user_wallets[user_id]
        for account in wallet.accounts:
            account.update()
            pending = account.pending
            if pending > 0:
                account.receive_all()
                context.bot.send_message(chat_id=user_id, text=f'{pending} BAN received on account {account.address}')

# Function to receive BAN manually
def receive(update, context):
    user_id = update.message.from_user.id
    if user_id in user_wallets:
        account = user_wallets[user_id].accounts[0]
        account.receive_all()
        update.message.reply_text('All pending transactions have been received.')
    else:
        update.message.reply_text('You need to create a wallet first with /start.')

# Setting up the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    jq = updater.job_queue

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('addaccount', add_account))
    dp.add_handler(CommandHandler('balance', balance))
    dp.add_handler(CommandHandler('send', send))
    dp.add_handler(CommandHandler('request', request_ban))
    dp.add_handler(CommandHandler('receive', receive))

    # Add a job to automatically check for pending transactions every minute
    jq.run_repeating(auto_receive, interval=60, first=0, context=None)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
