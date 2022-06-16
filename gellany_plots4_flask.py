import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Response
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)
@app.route('/')


def plot_png():
         x= data['Age']
         y= data['Sex']
         fig,ax=plt.subplots(figsize=(6,6))
         ax=sns.set(style="darkgrid")
         sns.boxplot(x=x,y=y,hue=y)
         canvas=FigureCanvas(fig)
         img = io.BytesIO()
         fig.savefig(img)
         img.seek(0)
         #return Response(img,mimetype='img/png')
         return Response(img.getvalue(), mimetype='image/png')


app.run(host="0.0.0.0", port=5000)
