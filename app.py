from flask import Flask, jsonify, render_template

app = Flask(__name__)
PROJECTS = [{
    'id': 1,
    'title': 'Vidya AI',
    'Description': 'An AI Tutor for one on one Learning Experience',
    'image':'/static/vidyaAI.jpg'
    
}, {
    'id': 2,
    'title': 'Tic-Tac-Toe',
    'Description': 'A human Size board Game , Programmed with Aurduino',
    'image':'/static/tic-tac-toe.jpg'
    
},
{
    'id': 4,
    'title': 'flappy bird',
    'Description': 'Flappy bird game played by NEAT',
    'image':'/static/flappybird.jpg'
    
}
]


@app.route("/")
def hello_faris():
  return render_template('home.html', projects=PROJECTS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(PROJECTS)

if __name__ == "__main__":
  app.run(host='127.0.0.1', debug=True)
