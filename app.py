from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import quandl

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
  quandl.ApiConfig.api_key = "CeGipRSorrpnDyvyQNx7"
  data = quandl.get("WIKI/TSLA")
  plot = figure()
  plot.circle(data.index, data.Close)
  return file_html(plot, CDN, "TSLA Price")

if __name__ == '__main__':
  app.run(port=33507)
