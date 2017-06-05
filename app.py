from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		number = request.form['number']
		#return render_template('index.html', number=number)
		return render_template('words-chart.html', number=number)
	return render_template('index.html')

@app.route('/words-chart')
def wchart(number):
	return render_template('words-chart.html', number=number)

if __name__ == '__main__':
 	app.run(port=33507)
