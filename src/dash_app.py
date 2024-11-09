import dash
from dash import html,dcc
import pandas as pd
import plotly.express as px

path=("C://Users//akhil//Desktop//MINE//Forage//quantium-task-1-model-answer//data//combined_data.csv")
app=dash.Dash(__name__)
data=pd.read_csv(path)

fig=px.line(data,x="date",y="sales",title="Pink Morsel price overtime.")
app.layout=html.Div([
    html.H1("Pink Morsel Price Track",style={'color':'#ff014d','textAlign':'center'}),
    dcc.Graph(
        id="price-line-graph",
        figure=fig
    )
])

if __name__=='__main__':
    app.run_server(debug=True)