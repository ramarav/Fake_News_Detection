from flask import Flask, render_template, request
from inference import predict_news
from explain_with_llm import explain_news_result

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result, explanation = None, None
    if request.method == "POST":
        news_text = request.form["news_text"]
        prediction = predict_news(news_text)
        explanation = explain_news_result(news_text, prediction)
        result = f"📰 Prediction: {prediction}"
    return render_template("index.html", result=result, explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
