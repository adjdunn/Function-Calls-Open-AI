def get_content(response):
    """
    Extract the text content from the model response.
    """
    if isinstance(response, dict):
        return response['choices'][0]['message']['content']
    else:
        return response.choices[0].message.content

        

def get_tool_calls(response):
    """
    Extract the list of tool calls from the model response.
    """
    return response.choices[0].message.tool_calls



def format_message(text_msg, msg_type):
    """
    Format a message to be sent to the model.
    """
    formatted_msg = {
        "role": msg_type,
        "content": [
            {
                "type": "text",
                "text": text_msg
            }
        ]
    }
    return formatted_msg



def get_tool_data(tool):
    """
    Extract the data from a tool call.
    """
    tool_object = {
        "id": tool.id,
        "type": "function",
        "function": {
            "name": tool.function.name,
            "arguments": f'{tool.function.arguments}'
        }
    }
    return tool_object



def tool_call_msg(tool_calls):
    """
    Create a message for tool calls.
    """
    tools = [get_tool_data(tool) for tool in tool_calls]

    tool_msg = {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": ""
            }
        ],
        "tool_calls": tools
    }
    return tool_msg



def tool_output_msg(tool_id, output):
    """
    Create a message for tool outputs.
    """
    output_msg = {
        "role": "tool",
        "content": [
            {
                "type": "text",
                "text": output
            }
        ],
        "tool_call_id": tool_id
    }
    return output_msg
