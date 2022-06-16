import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import argparse
import seaborn as sns

import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure



data = pd.read_csv('train.csv')
var1 = data['Age']
var2 = data['Sex']
hue = data['Sex']

app = Flask(__name__)
@app.route("/")

def distribution_sns():
               
                
                           # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = sns.boxplot(x=var1, y=var2 ,hue=hue)
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    #sns.boxplot(x=var1, y=var2 ,hue=hue)
    


#distribution_sns()

