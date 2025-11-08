# 🚀 Fake News Detection using ML + Generative AI

### 🧠 Detect fake vs. real news headlines and explain the reasoning using OpenAI GPT-4o-mini.

---

## 🏗️ Project Overview
This upgraded version of the classic Fake News Detection project adds an **LLM-powered explainability layer**.  
Traditional ML models classify news articles, while **GPT-4o-mini** provides a human-readable justification of why an article is likely fake or real.

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| 🧩 Machine Learning | **Scikit-Learn** | Core fake/real classification |
| 🧠 Generative AI | **OpenAI GPT-4o-mini** | Natural-language explanations |
| 💻 Frontend | **HTML + CSS** | Simple, responsive web interface |
| 🌐 Backend | **Flask** | Web app for serving predictions |
| 💾 Storage | **joblib, pandas** | Model + dataset handling |

---

## 🧩 Features
- 📰 Classifies news as **FAKE** or **REAL** using Passive Aggressive Classifier.  
- 🔍 Generates **explanations** via GPT-4o-mini for every prediction.  
- 🌐 Flask-based web app with an easy-to-use text input box.  
- 📈 Confusion matrix & accuracy summary available on `/metrics`.  
- 🧱 Modular folder structure for quick extension or retraining.

---

## 📁 Folder Structure
```
Fake_News_Detection/
│
├── app.py                     # Flask entry point
├── requirements.txt            # Dependencies
├── model/
│   ├── fake_news_model.pkl     # Trained PAC model
│   └── tfidf_vectorizer.pkl    # TF-IDF vectorizer
│
├── data/
│   └── news.csv                # Dataset (Kaggle-style)
│
├── utils/
│   ├── gpt_explainer.py        # GPT-4o-mini text explanations
│   ├── model_loader.py         # Load + predict helpers
│   └── preprocess.py           # Text preprocessing utils
│
├── templates/
│   └── index.html              # Web interface
│
├── static/
│   └── style.css               # Styling
│
└── README.md
```

---

## 🧰 Setup Instructions

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ramarav/Fake_News_Detection.git
cd Fake_News_Detection

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows use venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your OpenAI API key (for explanations)
set OPENAI_API_KEY=your_api_key_here  # Windows
export OPENAI_API_KEY=your_api_key_here  # macOS/Linux

# 5️⃣ Run Flask app
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) 🎯

---

## 🧪 Sample Output

| Input | Prediction | Explanation |
|--------|-------------|--------------|
| “NASA confirms aliens discovered near Mars base.” | **FAKE** | “This resembles tabloid-style unverifiable claims.” |
| “UN reports global hunger dropped by 10% in 2024.” | **REAL** | “The phrasing and reference to official data suggest credibility.” |

---

## 🧮 Model Performance
| Metric | Value |
|---------|--------|
| Accuracy | **93.13%** |
| Classifier | PassiveAggressiveClassifier |
| Vectorizer | TF-IDF (max_df=0.7, stop_words='english') |

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-1.5-orange.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

---

## 📦 API Endpoint Example

**POST** `/predict`
```bash
curl -X POST http://127.0.0.1:5000/predict      -H "Content-Type: application/json"      -d '{"text": "Breaking: New vaccine approved by WHO"}'
```

**Response:**
```json
{
  "prediction": "REAL",
  "explanation": "WHO approvals are verified through credible institutional sources."
}
```

---

## 💡 Future Enhancements
- [ ] Integrate news source credibility scoring  
- [ ] Add multilingual detection  
- [ ] Deploy using Docker + Render  
- [ ] Support voice-based input (Speech-to-Text)

---

## 👨‍💻 Author
**Mekala Ramarao**  
AMD India  
Focus: AI/ML applications in NLP, GPU analytics, and intelligent automation.  
📧 [LinkedIn](https://www.linkedin.com/in/mekala-ramarao-a2b5a562/)
