# # # Import packages
# # from dash import Dash, html, dash_table, dcc, callback, Output, Input
# # import pandas as pd
# # import plotly.express as px

# # # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# # # Initialize the app
# # app = Dash()

# # # App layout
# # app.layout = [
# #     html.Div(children='My First App with Data, Graph, and Controls'),
# #     html.Hr(),
# #     dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
# #     dash_table.DataTable(data=df.to_dict('records'), page_size=6),
# #     dcc.Graph(figure={}, id='controls-and-graph')
# # ]

# # # Add controls to build the interaction
# # @callback(
# #     Output(component_id='controls-and-graph', component_property='figure'),
# #     Input(component_id='controls-and-radio-item', component_property='value')
# # )
# # def update_graph(col_chosen):
# #     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
# #     return fig

# # # Run the app
# # if __name__ == '__main__':
# #     app.run(debug=True)
# from dash import Dash, html

# app = Dash()

# app.layout = [html.Div(children='Hello World')]

# if __name__ == '__main__':
#     app.run(debug=True)
import subprocess
import re

def get_installed_packages():
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    packages = result.stdout.decode('utf-8').split('\n')
    return [re.split('==', package)[0] for package in packages if package]

def update_spec_file(spec_file_path):
    packages = get_installed_packages()
    with open(spec_file_path, 'r') as file:
        spec_content = file.read()
    
    hidden_imports_section = "hiddenimports=["
    for package in packages:
        hidden_imports_section += f"'{package}', "
    hidden_imports_section = hidden_imports_section.rstrip(", ") + "],"
    
    spec_content = re.sub(r'hiddenimports=\[.*?\],', hidden_imports_section, spec_content, flags=re.DOTALL)
    
    with open(spec_file_path, 'w') as file:
        file.write(spec_content)

# Update the .spec file
update_spec_file('main.spec')