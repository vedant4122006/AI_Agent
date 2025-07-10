from huggingface_hub import InferenceClient
import os

# Option 1: Set as an environment variable (recommended for security)
# Before running your script, set the environment variable:
# export HF_TOKEN="hf_YOUR_COPIED_API_KEY"
# In Python:
hf_token = os.environ.get("HF_TOKEN")

# Option 2: Pass directly (less secure for production, but okay for quick tests)
# hf_token = "hf_YOUR_COPIED_API_KEY"

if not hf_token:
    print("Please set the HF_TOKEN environment variable or provide your API key directly.")
else:
    # Initialize the InferenceClient with your API key
    # You can specify a model directly here, or later when making requests
    client = InferenceClient(token=hf_token)

    # Example: Using the Serverless Inference API for text generation
    # Replace 'openai-community/gpt2' with any model you want to use from the Hugging Face Hub
    try:
        response = client.text_generation(
            model="openai-community/gpt2",
            prompt="Hello, my AI agent is learning to",
            max_new_tokens=50
        )
        print("Generated Text:", response)
    except Exception as e:
        print(f"Error making inference request: {e}")
        print("Remember that free tier models have rate limits and some models might be too large for serverless inference.")

    # Another example: Getting model info (doesn't require an API key for public models, but good for auth check)
    from huggingface_hub import HfApi
    api = HfApi(token=hf_token)
    try:
        user_info = api.whoami()
        print(f"\nLogged in as Hugging Face user: {user_info['name']}")
    except Exception as e:
        print(f"\nCould not get user info (API key might be invalid or no write access): {e}")