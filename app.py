from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_name = request.form.get("task")
        if task_name:
            tasks.append({"id": len(tasks)+1, "task": task_name, "done": False})
        return redirect(url_for("home"))
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
