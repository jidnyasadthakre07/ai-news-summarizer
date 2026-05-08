# 📰 AI News Summarizer & Headline Generator

An AI-powered multilingual newsroom assistant built using **Gemini AI, Streamlit, and Python** that generates concise news summaries, professional headlines, and automated news category classification in real time.

This project demonstrates practical applications of **Generative AI, Prompt Engineering, NLP, and AI Workflow Automation** for modern digital publishing and newsroom operations.

---

# 🚀 Live Demo

### 🚀 [Launch App](https://huggingface.co/spaces/Jidnyasa11/AI-News-Summarizer)
---

# 📌 Features

## ✅ AI News Summarization

* Generates concise 3-point summaries from long-form news articles
* Produces fact-focused outputs using Gemini AI
* Supports structured newsroom-style summarization

## ✅ AI Headline Generation

* Generates multiple professional headlines automatically
* Supports tone-controlled headline generation:

  * Formal
  * Catchy
  * SEO-Friendly
  * Breaking News

## ✅ Multi-language Support

Generate summaries and headlines in:

* English
* Hindi
* French
* Spanish
* German

## ✅ News Category Detection

Automatically classifies articles into categories such as:

* Technology
* Sports
* Politics
* Business
* Entertainment
* Health

## ✅ Interactive Streamlit UI

* User-friendly interface
* Real-time AI content generation
* Cloud deployable

## ✅ Hugging Face Deployment

Fully deployable using Hugging Face Spaces.

---

# 🏗️ System Architecture

```text
User Input Article
        ↓
Streamlit Frontend
        ↓
Prompt Engineering Layer
        ↓
Gemini API
        ↓
AI Summary Generation
        ↓
Headline Generation
        ↓
Category Detection
        ↓
Formatted Output
```

---

# 🛠️ Tech Stack

| Category             | Technology          |
| -------------------- | ------------------- |
| Programming Language | Python              |
| AI Model             | Gemini AI           |
| Frontend             | Streamlit           |
| Backend              | FastAPI (Optional)  |
| Deployment           | Hugging Face Spaces |
| NLP                  | Prompt Engineering  |
| Version Control      | Git & GitHub        |

---

# 📂 Project Structure

```text
NEWS-AI-PROJECT/
│
├── app.py
├── utils.py
├── prompts.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/jidnyasadthakre07/ai-news-summarizer.git
```

## 2. Navigate to Project Folder

```bash
cd ai-news-summarizer
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get Gemini API key from:

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧪 Example Input

```text
Apple announced a major AI update during its annual developer conference. The company introduced new AI-powered writing tools, smarter Siri capabilities, and real-time image generation features for iPhones, iPads, and Macs.
```

---

# ✅ Example Output

## 📌 Summary

* Apple introduced AI-powered tools across its devices.
* Siri received advanced AI and image generation capabilities.
* Apple emphasized privacy-focused on-device AI processing.

## 📰 Headlines

1. Apple Unveils Major AI Features Across Devices
2. Siri Gets Smarter With Apple AI Upgrade
3. Apple Expands Privacy-Focused AI Tools
4. Apple Introduces Real-Time AI Image Features
5. Apple Announces New AI Ecosystem Enhancements

## 🗂 Category

Technology

---

# 🌍 Deployment on Hugging Face

## Create Hugging Face Space

1. Go to Hugging Face Spaces
2. Create New Space
3. Select:

   * SDK: Streamlit
   * Hardware: CPU Basic
4. Upload project files
5. Add Gemini API key in:

   * Settings → Variables & Secrets

---

# 📈 Future Enhancements

* AI-powered SEO score generation
* Sentiment analysis
* Article URL scraping
* AI-based headline ranking
* Real-time news feed integration
* n8n workflow automation
* RAG-based contextual summarization
* Multi-agent AI newsroom workflows

---

# 💡 Key Learning Outcomes

This project demonstrates:

* Generative AI Integration
* Prompt Engineering
* NLP-based Text Processing
* Multilingual AI Applications
* Streamlit UI Development
* Cloud Deployment
* API Integration
* AI Workflow Design

---

# 🧠 Resume Highlights

* Developed a multilingual AI-powered news summarization and headline generation platform using Gemini APIs, Streamlit, and advanced prompt engineering techniques.

* Built and deployed an end-to-end Generative AI application with automated news category detection, tone-controlled headline generation, and real-time content summarization.

* Integrated Gemini AI with Python-based workflows and deployed the application on Hugging Face Spaces to deliver scalable AI-driven news content automation.

---

# 👨‍💻 Author

Jidnyasa Thakre

GitHub: https://github.com/jidnyasadthakre07 

LinkedIn: https://www.linkedin.com/in/jidnyasathakre/
