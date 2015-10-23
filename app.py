from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    peer_key = os.environ['PEERKEY']
    return render_template("home.html", peerkey=peer_key)

if __name__ == "__main__":
    app.run()
