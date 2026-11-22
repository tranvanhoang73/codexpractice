from flask import Flask, jsonify, request, send_from_directory


app = Flask(__name__)

CORRECT_ANSWERS = {
    "q1": "b",
    "q2": "c",
    "q3": "c",
    "q4": "a",
    "q5": "b",
}


@app.get("/")
@app.get("/python_quiz.html")
def home():
    return send_from_directory(app.root_path, "python_quiz.html")


@app.post("/submit")
def submit_quiz():
    selections = request.get_json(silent=True)
    if not isinstance(selections, dict):
        return jsonify(error="Không nhận được câu trả lời hợp lệ."), 400

    score = sum(
        selections.get(question) == correct_answer
        for question, correct_answer in CORRECT_ANSWERS.items()
    )
    return jsonify(score=score, total=len(CORRECT_ANSWERS), message=f"Bạn đạt {score}/5 điểm.")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
