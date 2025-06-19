########################
### Install Packages ###
########################

import subprocess
import sys

def install_packages(pacotes):
    for pacote in pacotes:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# List of packages
packages_list = ["numpy", "pandas", "matplotlib", "scipy", "seaborn","statsmodels", "plotly", "gurobipy",
"yfinance", "scikit-learn", "panel", "datashader", "param", "colorcet", "transformers","einops","accelerate", 
"bitsandbytes"]

install_packages(packages_list)

#####################
### Load Packages ###
#####################

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.colors import LinearSegmentedColormap
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from scipy.stats import skew, boxcox

df = pd.read_csv("https://drive.google.com/uc?export=download&id=1wMapByTvMFt16zz9Bd2643eTHJXtEhnX")
df

df.describe()
df.dtypes

PyMC

#####################################
### Análise Exploratória de Dados ###
#####################################

# Verificar a presença de valores nulos

df.isnull().sum()
df.count()

# Substituindo pela média
df['TV_Spend'] = df['TV_Spend'].fillna(df['TV_Spend'].mean())
df['Radio_Spend'] = df['Radio_Spend'].fillna(df['Radio_Spend'].mean())
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Eliminando valores nulos
#
#