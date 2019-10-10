"""
Short script to test if the environment is correctly set up for the GRK Python
Workshop (14.10.-16.10.2019 in Freiburg).
"""
# Checking if the Python version is at least 3.7
import sys
python_version = sys.version_info
print("Your current python version is %i.%i.%i" % (python_version.major,
                                                   python_version.minor,
                                                   python_version.micro))
if python_version.major != 3:
    print("You don't have Python 3 installed.\n\
          Please install python 3.7 or higher.")
elif python_version.minor < 7:
    print("You don't have the correct python 3 version installed.\n\
          Please install python 3.7 or higher.")

import matplotlib
print("- matplotlib is available with version", matplotlib.__version__)

import pandas
print("- pandas is available with version", pandas.__version__)

import numpy
print("- numpy is available with version", numpy.__version__)

import scipy
print("- scipy is available with version", scipy.__version__)

import seaborn
print("- seaborn is available with version", seaborn.__version__)

import jupyter
print("- jupyter is available with version", jupyter.__version__)

import jupyterlab
print("- jupyterlab is available with version", jupyterlab.__version__)

import h5py
print("- h5py is available with version", h5py.__version__)

import mpld3
print("- mpld3 is available with version", mpld3.__version__)

import papermill
print("- papermill is available with version", papermill.__version__)

import pydot
print("- pydot is available with version", pydot.__version__)

import PIL
print("- pillow is available with version", PIL.__version__)

print("- matplotlib is available with version", matplotlib.__version__)

import ipywidgets
print("- ipywidgets is available with version", ipywidgets.__version__)

import tables
print("- tables is available with version", tables.__version__)

import tqdm
print("- tqdm is available with version", tqdm.__version__)

import pytest
print("- pytest is available with version", pytest.__version__)

import virtualenv
print("- virtualenv is available with version", virtualenv.__version__)

print("\nAll requirements are fullfilled.")
