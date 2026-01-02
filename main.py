import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable not set.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


print(f"User prompt: {args.user_prompt}")

generated_content_response = client.models.generate_content(
    model="gemini-2.5-flash", contents=args.user_prompt
)

usage_metadata = generated_content_response.usage_metadata
if not usage_metadata:
    raise RuntimeError("No usage metadata found in the response.")

print(f"Prompt tokens: {usage_metadata.prompt_token_count}")

print(f"Response tokens: {usage_metadata.candidates_token_count}")

print(f"Response:\n{generated_content_response.text}")


def main():
    print("Hello from py-ai-agent!")


if __name__ == "__main__":
    main()
