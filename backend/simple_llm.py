import os
import sys
from litellm import completion

def main():
    # Default configuration from reporter/agent.py
    model_id = os.getenv("BEDROCK_MODEL_ID", "us.anthropic.claude-3-7-sonnet-20250219-v1:0")
    region = os.getenv("BEDROCK_REGION", "us-west-2")
    
    # Set AWS region for Bedrock
    os.environ["AWS_REGION_NAME"] = region
    
    model_name = f"bedrock/{model_id}"
    
    print(f"Using model: {model_name}")
    print(f"Region: {region}")
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        print(f"\nPrompt: {prompt}")
        try:
            response = completion(
                model=model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            print("\nResponse:")
            print(response.choices[0].message.content)
        except Exception as e:
            print(f"\nError: {e}")
        return

    # Interactive mode
    print("Enter your prompt (or 'quit' to exit):")
    
    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() in ('quit', 'exit'):
                break
            
            if not user_input.strip():
                continue
                
            print("Thinking...")
            response = completion(
                model=model_name,
                messages=[{"role": "user", "content": user_input}]
            )
            
            print("\nResponse:")
            print(response.choices[0].message.content)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
