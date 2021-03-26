from flask import Flask, render_template

##########################################################

app = Flask('__main__')
##########################################################

edens = [{
	'name' : 'eden',
	'age' : '22',
	'fname' : 'takele',
	'mom' : 'lemlem',

},
{
	'name' : "tedy",
	'age' : '19',
	'fname' : 'tak',
	'mom' : 'lem',
}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', edens=edens)

##########################################################
@app.route("/about")
def about():
	return render_template('about.html', title = 'about')

##########################################################
@app.route("/contact")
def contact():
	return "<p>this is contact page watch out</p>"

##########################################################
@app.route("/layout")
def layout():
	return render_template('layout.html')
##########################################################

if __name__ == '__main__':
	app.run(debug = True)
