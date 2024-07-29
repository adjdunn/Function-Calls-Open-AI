
# Function Calling Tutorial with OpenAI API

This repository contains a tutorial application demonstrating how to use OpenAI's API to call specific functions, such as retrieving stock prices and weather information. The application is composed of three main modules: `main.py`, `utils.py`, and `tools.py`.

## Table of Contents

- [Introduction](#introduction)
- [YouTube Tutorial](#youtube-tutorial)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [main.py](#mainpy)
  - [utils.py](#utilspy)
  - [tools.py](#toolspy)
- [License](#license)

## Introduction

This tutorial walks through the process of setting up a simple chatbot that uses function calling with OpenAI's API. The chatbot can respond to user queries and, when needed, call specific functions to retrieve stock prices or weather information.

## YouTube Tutorial

Watch the full tutorial on YouTube:

<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" frameborder="0" allowfullscreen></iframe>

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/function-calling-tutorial.git
   cd function-calling-tutorial
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

Run the chatbot application by executing the following command:

```bash
python main.py
```

You will be prompted to ask the chatbot a question. The chatbot can respond with answers and, if necessary, call functions to get stock prices or weather information.

## Modules

### main.py

The `main.py` module initializes the OpenAI client, defines the tools available for the chatbot, and contains the main conversation loop. It handles user input, sends it to the model, and processes the responses, including function calls.

Key functions:
- **execute_function_call(tool)**: Executes the function call based on the tool provided.
- **gpt_endpoint(messages, tools)**: Sends a request to the GPT model and retrieves the response.
- **run_conversation()**: Runs the interactive conversation loop with the chatbot.

### utils.py

The `utils.py` module contains utility functions used by the main module to handle message formatting and response processing.

Key functions:
- **get_content(response)**: Extracts the text content from the model response.
- **get_tool_calls(response)**: Extracts the list of tool calls from the model response.
- **format_message(text_msg, msg_type)**: Formats a message to be sent to the model.
- **get_tool_data(tool)**: Extracts data from a tool call.
- **tool_call_msg(tool_calls)**: Creates a message for tool calls.
- **tool_output_msg(tool_id, output)**: Creates a message for tool outputs.

### tools.py

The `tools.py` module contains the functions that the chatbot can call. These functions are currently set up with test data and should be replaced with actual API calls for a production environment.

Key functions:
- **get_stock_price(symbol)**: Retrieves the stock price for a given symbol.
- **get_weather(location, units='c')**: Retrieves the weather temperature for a given location.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!
