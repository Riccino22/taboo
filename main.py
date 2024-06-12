from flask import Flask, render_template, redirect
import id_generator as id
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.post("/")
def new_game():
    return redirect(f"/game/{id.generate()}")

@app.route("/game/<game_id>")
def game(game_id):
    return render_template("game.html")


app.run(debug=True)