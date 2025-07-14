import gradio as gr
from transformers import pipeline

chatbot = pipeline("text2text-generation", model="gpt2")

def chat_fn(message):
    prompt = f"Answer the following question clearly:\n{message}"
    result = chatbot(prompt,   max_new_tokens=100,
        temperature=1,             # add randomness
        top_k=100,                    # limit to top 50 predictions
        top_p=0.95,                  # nucleus sampling
        repetition_penalty=1,      # reduce repeating loops
        do_sample=True               # allow sampling
    )[0]["generated_text"]
    response = result[len(prompt):].strip()
    return response

gr.Interface(fn=chat_fn, inputs="text", outputs="text", title="My Hugging Face AI Agent").launch()
