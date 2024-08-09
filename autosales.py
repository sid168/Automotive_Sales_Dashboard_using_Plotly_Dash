import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from IPython.display import display


# Load the data using pandas
data = pd.read_csv('/Users/x/PycharmProjects/pythonProject/Automobile.csv')
data = pd.DataFrame(data)
print(data.head())

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

# Create the dropdown menu options
# dropdown_options = [
#     {'label': 'Yearly Statistics report', 'value': 'Yearly Statistics'},
#     {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
# ]
# List of years
year_list = [i for i in range(1980, 2024, 1)]

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign': 'center', 'color':'#503D36', 'font-size':24}),
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics report', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            placeholder='Select a report type'
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year'
        )),
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ])
])

# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True

'''
return False:
If 'Yearly Statistics' is selected, the function returns False, which means the select-year component will be enabled (not disabled).
return True:
If any other option is selected, the function returns True, which disables the select-year component.
'''
# Callback for plotting
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='select-year', component_property='value')]
)

# children in Dash is a property that contains the content inside a Dash component.
# For example, in an html.Div component, children can be text, other HTML components, graphs, or any Dash component.

def update_output_container(select_statistics, input_year):
    if select_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # Plot 1: Automobile sales fluctuate over Recession Period (year wise)
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec,
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))

        # Plot 2: Average number of vehicles sold by vehicle type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2  = dcc.Graph(
            figure=px.bar(average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title="Average Automobile Sales by Vehicle Type"))

        # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
                             figure=px.pie(exp_rec,
                             names='Vehicle_Type',
                             values='Advertising_Expenditure',
                             title='Total expenditure share by vehicle type during recession'
                                           ))

        # Plot 4: Bar chart for the effect of unemployment rate on vehicle type and sales
        unemp_data = recession_data.groupby(['Vehicle_Type', 'unemployment_rate'])[
            'Automobile_Sales'].mean().reset_index()

        # We will now plot `unemployment_rate` on the x-axis and `Automobile_Sales` on the y-axis.
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data,
                                           x='unemployment_rate',
                                           y='Automobile_Sales',
                                           color='Vehicle_Type',
                                           labels={'unemployment_rate': 'Unemployment Rate',
                                                   'Automobile_Sales': 'Average Automobile Sales'},
                                           title='Effect of Unemployment Rate on Vehicle Type and Sales'))


        return [
             html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
             html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'})
            ]

    elif input_year and select_statistics == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]

        # Plot 1: Yearly Automobile sales using line chart for the whole period
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas,
                                            x='Year',
                                            y='Automobile_Sales',
                                            title='Yearly Automobile sales for the whole period'))

        # Plot 2: Total Monthly Automobile sales using line chart
        mas = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas,
            x='Month',
            y='Automobile_Sales',
            title='Total Monthly Automobile Sales'))

        # Plot 3: Bar chart for average number of vehicles sold during the given year
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
                                            x='Vehicle_Type',
                                            y='Automobile_Sales',
                                            title=f'Average Vehicles Sold by Vehicle Type in the year {input_year}'))

        # Plot 4: Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
            names='Vehicle_Type',
            values='Advertising_Expenditure',
            title='Total Advertisement Expenditure for each vehicle'))

        return [
                html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display': 'flex'}),
                html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display': 'flex'})]

    else:
        return html.Div()

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
