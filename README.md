# First OpenAI API Call

A simple Python script that demonstrates how to make API calls to OpenAI's GPT model.

## What This Script Does

This script:
- Takes user input as a prompt
- Makes an API call to OpenAI's GPT model
- Displays the AI's response
- Shows token usage statistics

## Requirements

- Python 3.7 or higher
- OpenAI Python package
- OpenAI API key

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install openai
   ```

2. Create a `.env` file in the project root directory:
   ```bash
   cp .env.example .env
   ```

3. Add your OpenAI API key to the `.env` file:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Script

1. Make sure you're in the project directory
2. Run the script:
   ```bash
   python first_ApiCall.py
   ```

The script will prompt you for input and display the AI's response along with token usage statistics.

## Security Note

- The `.env` file containing your API key is gitignored for security reasons
- Never commit your actual API key to version control
- Always use `.env.example` as a template for other developers

## License

MIT License