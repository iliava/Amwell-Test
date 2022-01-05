from flask import Flask, render_template
import requests

app = Flask('Scores Game')
@app.route('/')
def url_check():
    try:
        if (requests.get("http://10.2.3.233").status_code) == 200:
            return render_template('Good.html')
        else:
            return render_template('bad.html')
    except:
        return render_template('bad.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
