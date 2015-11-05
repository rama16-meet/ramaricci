from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("homerama.html")

@app.route('/aboutrama')
def about():
	return render_template("aboutrama.html")

@app.route('/contactrama')
def contact():
	return render_template("contactrama.html")



if __name__ == "__main__": 
	app.run()
