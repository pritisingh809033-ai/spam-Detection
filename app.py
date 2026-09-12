from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

messages = [
    "Congratulations you won a free prize",
    "You have won a free lottery ticket",
    "Claim your free reward now",
    "You won a cash prize click now",
    "Get free money by clicking this link",
    "Urgent you have won a gift voucher",
    "Congratulations claim your reward",
    "Win a free mobile phone today",
    "You are selected for a cash reward",
    "Free offer available click now",
    "Hey, how are you?",
    "Are you coming to college today?",
    "Please call me when you are free",
    "I will reach home in ten minutes",
    "Can you send me the notes?",
    "Let's meet tomorrow",
    "Your class starts at 10 AM",
    "Please bring your project tomorrow",
    "I am going to the market",
    "See you at college tomorrow"
]

labels = [
    "spam", "spam", "spam", "spam", "spam",
    "spam", "spam", "spam", "spam", "spam",
    "ham", "ham", "ham", "ham", "ham",
    "ham", "ham", "ham", "ham", "ham"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.25, random_state=42, stratify=labels
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100


@app.route("/", methods=["GET", "POST"])
def home():
    prediction =
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            message_vector = vectorizer.transform([message])
            result = model.predict(message_vector)[0]

            if result == "spam":
                prediction = "SPAM"
            else:
                prediction = "NOT SPAM"

    return render_template(
        "index.html",
        prediction=prediction,
        message=message,
        accuracy=round(accuracy, 2)
    )
if __name__== "__main__":
    app.run(debug=True)

