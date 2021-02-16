
#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker 1 container! <a href="http://localhost:5001">link</a> '

app.run(debug=True, port=5000, host='0.0.0.0')
