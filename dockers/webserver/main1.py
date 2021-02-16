
#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker 2 container! <a href="http://localhost:5000">link</a> '

app.run(debug=True, port=5001, host='0.0.0.0')
