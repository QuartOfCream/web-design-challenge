from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def echo():
    flask_server = ["Ricky", "Bobby", "Cougar"]
    return render_template("index.html", text="flask_server")

if __name__ == "__main__":
    app.run(debug=True)


