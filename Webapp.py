from flask import Flask, render_template, redirect, request
from Finanical_Functions import EAR, HPR, APR

# Configure the Flask Object
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

# Index of the website
@app.route('/')
def index():
    return render_template('Index.html')

# Main function
if __name__ == "__main__":
    app.run()