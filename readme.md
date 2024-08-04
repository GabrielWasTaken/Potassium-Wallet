# Potassium Wallet - Banano Telegram Bot

Potassium Wallet is a Telegram bot that allows users to create and manage Banano wallets directly from Telegram. The bot provides functionalities such as creating a new wallet, sending and receiving BAN, adding additional accounts, and automatically monitoring for pending transactions.

You can access the bot directly at [t.me/Wallet19bot](https://t.me/Wallet19bot).

## Features

- **Create Wallet**: Users can create a new Banano wallet.
- **Check Balance**: Users can check their current BAN balance.
- **Send BAN**: Users can send BAN to other addresses.
- **Request BAN**: Generate a receive address to request BAN from others.
- **Add Account**: Users can add additional accounts to their wallet.
- **Auto-Receive**: The bot automatically checks and notifies users of pending transactions.

## Requirements

- Python 3.6 or higher
- A Telegram bot token (create one using [BotFather](https://core.telegram.org/bots#6-botfather))
- An accessible Banano RPC node (e.g., [Kalium Node](https://kaliumapi.appditto.com/api))

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/potassium-wallet.git
    cd potassium-wallet
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configuration**:

    - Create a `config.json` file in the root directory and add your Telegram bot token and Banano node URL.

    ```json
    {
        "telegram_bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
        "banano_node": "https://kaliumapi.appditto.com/api"
    }
    ```

4. **Run the bot**:

    ```bash
    python bot.py
    ```

## Usage

### Commands

- **/start**: Create a new Banano wallet.
- **/balance**: Check your current BAN balance.
- **/send**: Send BAN to another address. Usage: `/send <recipient_address> <amount>`.
- **/request**: Generate a receive address to request BAN.
- **/addaccount**: Add an additional account to your wallet.
- **/receive**: Manually receive all pending transactions.

The bot automatically checks for pending transactions every minute and notifies users when new transactions are received.

## Debugging

To test your configuration and setup, you can run the `debug.py` script:

```bash
python debug.py
```

This script will help you verify the connection to the Banano node and ensure that your Telegram bot token is set up correctly.

Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Any contributions or improvements are welcome.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
