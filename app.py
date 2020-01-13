from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)

@app.route('/')
def index():
  nquestions = 5
  return render_template('userinfo.html', num=nquestions)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/render')
def render():
  plot = figure()
  plot.circle([1, 2], [3, 4])
  return file_html(plot, CDN, "my plot")

if __name__ == '__main__':
  app.run(port=33507)
