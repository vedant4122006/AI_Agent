import gradio as gr
from transformers import pipeline

# Load a proper instruction-tuned chat model
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

def chat_fn(message):
    prompt = f"Answer the following question clearly:\n{message}"
    result = chatbot(prompt, max_new_tokens=100)[0]["generated_text"]
    return result

gr.Interface(fn=chat_fn, inputs="text", outputs="text", title="My Hugging Face AI Agent").launch()
