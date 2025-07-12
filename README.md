# 🤖 My Hugging Face AI Chat Agent

This is a beginner-friendly **AI chatbot app** built using 🤗 Hugging Face's `transformers` library and the `gradio` UI framework. It uses a lightweight instruction-tuned model (`google/flan-t5-small`) to understand and respond to your messages, just like a simple version of ChatGPT — but runs entirely for free on your own machine!

> 🚀 Built by [Vedant Rajurkar](https://github.com/vedant4122006) as a hands-on learning project and showcase for GitHub + LinkedIn.

---

## 💡 What This Project Does

- ✅ Accepts a question or message from the user
- ✅ Uses Hugging Face transformer model to generate a reply
- ✅ Displays everything in a clean Gradio web interface
- ✅ Runs **locally**, no paid API or cloud setup needed
- ✅ 100% open-source and easy to customize

---

## 🧠 Technologies Used

| Tool / Library      | Purpose                              |
|---------------------|---------------------------------------|
| Python              | Main programming language             |
| Transformers (Hugging Face) | Loads the AI model (`flan-t5-small`) |
| Gradio              | Builds the web chat UI                |
| PyTorch             | Backend deep learning framework       |
| VS Code             | Code editor used                      |

---

## 🛠️ How to Run It Locally

### 1. Clone the Repo
```bash
git clone https://github.com/vedant4122006/AI_Agent.git
cd AI_Agent
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
