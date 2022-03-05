from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/innerpage")
def base():
    return render_template("inner-page.html")

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-details.html')    
if __name__=="__main__":
    app.run(debug=True)    