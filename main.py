from openai import OpenAI
import os
from tools import get_stock_price, get_weather
from utils import get_content, get_tool_calls, format_message, tool_call_msg, tool_output_msg
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


# Initialize conversation messages
messages = []



# Define available tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The stock symbol"
                    }
                },
                "required": ["symbol"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Determine weather in my location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["c", "f"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]



def execute_function_call(tool):
    """
    Execute the function call based on the tool provided.
    """
    func_name = tool['function']['name']
    func_args = json.loads(tool['function']['arguments'])

    tools_map = {
        "get_stock_price": get_stock_price,
        "get_weather": get_weather
    }

    func = tools_map[func_name]
    return str(func(**func_args))



def gpt_endpoint(messages, tools):
    """
    Send a request to the GPT model and retrieve the response.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        tools=tools
    )
    return response



def run_conversation():
    """
    Run the interactive conversation loop with the chatbot.
    """
    while True:
        user_input = input('Ask the chatbot a question: ')
        print()
        
        # Append user input to conversation
        messages.append(format_message(user_input, "user"))
        
        # Send user message to model and get response
        response = gpt_endpoint(messages, tools)
        
        # Get tool call list from response
        tool_calls = get_tool_calls(response)
        
        if tool_calls:
            print(f'Tools were called: {[tool["function"]["name"] for tool in tool_calls]}')
            # Append tool call response to conversation
            messages.append(tool_call_msg(tool_calls))
        
            # Append all the data to the conversation
            for tool in tool_calls:
                tool_output = tool_output_msg(tool['id'], execute_function_call(tool))
                messages.append(tool_output)
        
            # Send another call to the model
            response_after_tool_call = gpt_endpoint(messages, tools)
            final_text_response = get_content(response_after_tool_call)
        
            messages.append(format_message(final_text_response, "assistant"))
        
            print(f'Bot: {final_text_response}')
            print()
        
        else: 
            print("No tools called.")
        
            model_response_text = get_content(response)
        
            # Append model response to conversation
            messages.append(format_message(model_response_text, "assistant"))
        
            print(f'Bot: {model_response_text}')
            print()



if __name__ == "__main__":
    run_conversation()






