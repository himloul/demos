from src.chatbot import Chatbot
import json

colors = {
    "user": "\u001b[91m",
    "bot": "\u001b[92m",
    "reset": "\u001b[0m"
}

def load_config():
    with open('src/config.json', 'r') as f:
        config = json.load(f)
    config['grammars'] = Chatbot.load_grammar(config.get('grammar', ""))
    return config

config = load_config()

def main():
    # load the functions
    with open('src/functions.json', 'r') as file:
        functions = json.load(file)

    chatbot = Chatbot(
        url = config['api']['url'],
        user_name = config['names']['user'],
        bot_name = config['names']['bot'],
        functions=functions["functions"],
        grammar=config['grammars']
    )

    print("Welcome to the Chatbot CLI! Type 'exit' to end the conversation.")

    while True:
        names = chatbot.get_names()
        user_input = input(f"{colors['user']}{names['user']}: {colors['reset']}")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.send_message(user_input)
        print(f"{colors['bot']}{names['bot']}: {response}{colors['reset']}")

if __name__ == "__main__":
    main()
