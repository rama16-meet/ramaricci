from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("rama.html")

@app.route('/Hello/', methods=['POST'])
@app.route('/Hello/<name>')
def Hello():
	a = request.form['name']
	return render_template('rama3.html', name=a)

if __name__ == "__main__": 
	app.run()
