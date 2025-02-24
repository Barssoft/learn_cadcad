import sys
import itertools
import pandas as pd
import plotly.express as px
sys.path.append('..')

from model.run import df
df1 = df.copy(deep=True)
print(df1)

my_colors = ["#253659", "#BF665E", "#F28157"]

df2 = df1.copy(deep=True)
df2 = df2.groupby(['run', 'timestep']).last().reset_index()

fig = px.line(df2, x="timestep", y=[ 'start'], line_group='run',  title='Количество стартовых просмотров', height=600, color_discrete_sequence= my_colors)


fig.update_layout(xaxis_title='Месяцы', yaxis_title='Просмотры')

fig.show()