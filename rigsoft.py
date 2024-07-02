from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def main():
  return render_template('main.html')
@app.route('/basic computation')
def basic_computation():
  return render_template('basic computation.html')
@app.route('/about')
def about():
  return render_template('about.html')
@app.route('/displacement')
def displacement():
  return render_template('displacement.html')
@app.route('/main_help')
def main_help():
  return render_template('main_help.html')
app.run(debug=True)