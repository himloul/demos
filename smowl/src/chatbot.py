import requests
import json

class Chatbot:

    @staticmethod
    def load_grammar(grammars):
        grammar_path = grammars['json']
        try:
            with open(grammar_path, 'r') as grammar_file:
                return grammar_file.read()
        except FileNotFoundError:
            print(f"Grammar file not found: {grammar_path}")
        return ""

    def __init__(self, url: str, functions: list, user_name: str, bot_name: str, grammar: str = None):
        self.conversation_history = ""
        self.grammar = grammar or ""
        self.user_name = user_name
        self.bot_name = bot_name
        self.functions = functions
        self.system_prompt = ""
        self.url = url

        if self.functions:
            self.system_prompt = prompt_template.format(functions=format_functions(functions=functions))

    def send_message(self, user_input):
        self.conversation_history = f"\n\n{self.system_prompt}\n{self.user_name}: {user_input}\n{self.bot_name}:"
        print("> PROMPT:", self.conversation_history)
        # conversation history is disabled

        payload.update({
            "grammar": self.grammar,
            "prompt": self.conversation_history,
            "image_data": [],
            "stop": ["</s>", f"{self.bot_name}:", f"{self.user_name}:"]
        })

        try:
            print("> PAYLOAD", payload)
            response = requests.post(self.url, json=payload, timeout=30)
            response.raise_for_status()
            bot_response = json.loads(response.text)["content"] # print response.text to check all keys
            self.conversation_history += bot_response
            return bot_response
        except requests.RequestException as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        self.conversation_history = ""

    def set_names(self, user_name=None, bot_name=None):
        if user_name:
            self.user_name = user_name
        if bot_name:
            self.bot_name = bot_name

    def get_names(self):
        return {"user": self.user_name, "bot": self.bot_name}


payload = {
    "stream": False,
    "n_predict": 400,
    "temperature": 0.7,
    "stop": ["</s>"],
    "repeat_last_n": 256,
    "repeat_penalty": 1.18,
    "penalize_nl": True,
    "dry_multiplier": 0,
    "dry_base": 1.75,
    "dry_allowed_length": 2,
    "dry_penalty_last_n": -1,
    "top_k": 40,
    "top_p": 0.95,
    "min_p": 0.05,
    "xtc_probability": 0,
    "xtc_threshold": 0.1,
    "typical_p": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "mirostat": 0,
    "mirostat_tau": 5,
    "mirostat_eta": 0.1,
    "grammar": "",
    "n_probs": 0,
    "min_keep": 0,
    "image_data": [],
    "cache_prompt": True,
    "api_key": "",
    "slot_id": -1,
    "prompt": ""
}

prompt_template = """
You are an expert that calls functions based on user requests. Available functions with required parameters:
{functions}

Rules:
- Select the most appropriate function based on the request.
- Format the function call using the exact syntax: [function_name(param1=value1, param2=value2, ...)]
- Include only the function call in your response.

Examples:

User: Find my phone
Assistant: [locate_device(mode="GPS")]

User: Translate 'Hello' to French
Assistant: [translate_text(text="Hello", target_language="French")]

User: Share location with John
Assistant: [share_location(to="John")]
"""



def format_functions(functions):
    return "\n\n".join(
        f"{func['name']}: {func['description']}\n" +
        "\n".join(f"- {arg}: {details.get('description', 'No description provided')}"
                  for arg, details in func.get('parameters', {}).get('properties', {}).items())
        for func in functions
    )
