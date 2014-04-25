from flask import *
from functools import wraps
from db import *
from json import dumps

app = Flask(__name__)
app.secret_key = '5RD{Hd1CRSwCoqct4Y497&4Ar12t5V'

# login decorator
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('Please login first.')
			return redirect(url_for('log'))
	return wrap

##################### routes #####################

# logout session
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('log'))

# login
@app.route('/log',methods=['GET','POST'])
def log():
	error = None
	if request.method == 'POST':
		if request.form['uid'] != 'admin' or request.form['pwd'] != 'ponytracks':
			error = 'Invalid Credentials. Please try again.'
			flash(error)
			return redirect(url_for('log'))
		else:
			session['logged_in'] = True
			return redirect(url_for('index'))
	return render_template('log.html',error=error)

# main
@app.route('/')
@login_required
@app.route('/main',methods=['GET','POST'])
def index():
	return render_template('main.html')

# principal
@login_required
@app.route('/principal',methods=['GET','POST'])
def principal():
	return render_template('principal.html')

# common core test
@login_required
@app.route('/commoncore',methods=['GET','POST'])
def commoncore():
	return render_template('cctest.html')

# julie test
@login_required
@app.route('/julie',methods=['GET','POST'])
def julie():
	return render_template('julie.html')

# update patter test
@login_required
@app.route('/updates',methods=['GET','POST'])
def updates():
	return render_template('updates.html')

# student view
@login_required
@app.route('/student',methods=['GET','POST'])
def student():
	return render_template('student.html')

################ data API's ################


@login_required
@app.route('/API/stanDesc/<domain>/<standard_index>',methods=['GET'])
def stanDesc(domain,standard_index):
	return standard_description(domain,standard_index)

@login_required
@app.route('/API/showSkills/<standard_index_code>',methods=['GET'])
def showSkills(standard_index_code):
	return make_response(dumps(show_skills(standard_index_code)))

@login_required
@app.route('/API/standardStrength/<standard_index_code>',methods=['GET'])
def standardStrength(standard_index_code):
	print make_response(dumps(standard_strength(standard_index_code)))
	return make_response(dumps(standard_strength(standard_index_code)))

# @login_required
# @app.route('/API/assessment/<skill_assessment_code>',methods=['GET'])
# def standardStrength(standard_index_code):
# 	print make_response(dumps(standard_strength(standard_index_code)))
# 	return make_response(dumps(standard_strength(standard_index_code)))

if __name__ == '__main__':
	app.run(debug=True)