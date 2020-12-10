import pandas as pd
import plotly.figure_factory as pf

with open('data.csv') as file:
  df = pd.read_csv(file)
  
pf.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=True).show()
