from flask import Flask, render_template

app = Flask('Scores Game')
@app.route('/')
def
  return 'Hello! I am a Flask application'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
