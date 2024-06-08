from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def create_graph():
    filename = 'demo'

    # random but consistant data
    lst = [2,9,4,6,4]
    a = np.linspace(-4, 4, 16)
    b = np.linspace(-(max(lst)), max(lst), len(lst))
    x, y = np.meshgrid(a, b)
    z = np.sin(np.sqrt(x**2 + y**2))

    # clear buffer
    plt.clf()
    ax = plt.figure().add_subplot(projection='3d')
    ax.contour3D(x, y, z, 10, cmap=cm.cool)
    plt.savefig(f'static/img/{filename}.png')

@app.route('/', methods=['GET'])
def getIndex():
    create_graph()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)