from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""<h1>Welcome to my webapp
            current time is {datetime.now()}</h1>
        """

if __name__=="__main__":
    app.run()
