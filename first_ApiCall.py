from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    system_prompt = "You are a helpful and concise assistant."
    user_prompt = input("What would you like to ask : ")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
        )
        reply = response.choices[0].message.content
        print("\nAssistant's reply:\n" + reply)
        usage = response.usage
        print(f"\nToken usage: {usage.total_tokens} tokens (Prompt: {usage.prompt_tokens}, Completion: {usage.completion_tokens})")

    except Exception as e:
        print("Error while API call:", str(e))

if __name__ == "__main__":
    main()