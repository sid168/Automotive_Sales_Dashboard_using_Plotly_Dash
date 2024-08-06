# Automotive_sales


The objective of this part of the Final Assignment is to analyze the historical trends in automobile sales during recession periods, as you did in the previous part. The goal is to provide insights into how the sales of XYZAutomotives, a company specializing in automotive sales, were affected during times of recession.

In this final assignment, you will have the opportunity to demonstrate the Dashboarding skills you have acquired in this course.

This lab aims to assess your abilities in creating various visualizations using Plotly and Dash. As a data scientist, you have been given a task to prepare a report on your finding from Automobile Sales data analysis.
You decided to develop a dashboard representing two main reports:-

Yearly Automobile Sales Statistics
Recession Period Statistics
NOTE: Year range is between 1980 and 2013.

Components of the report items

1. Yearly Automobile Sales Statistics

This report mainly consists of the following items:

Yearly Automobile Sales Using Line Chart for the Whole Period (line chart):This line chart displays the average automobile sales for each year across the entire period.

Total Monthly Automobile Sales Using Line Chart (line chart):This line chart displays the total monthly automobile sales for the selected year.

Average Vehicles Sold by Vehicle Type in the Selected Year (bar chart):This bar chart shows the average number of vehicles sold for each vehicle type in the selected year.

Total Advertisement Expenditure for Each Vehicle Using Pie Chart (pie chart):
This pie chart represents the total advertising expenditure for each vehicle type in the selected year.

2. Recession Period Statistics

Average Automobile Sales Fluctuation Over Recession Period (Year-wise):This line chart shows the average automobile sales for each year during recession periods.

Average Number of Vehicles Sold by Vehicle Type:This bar chart displays the average number of vehicles sold for each vehicle type during recession periods.

Total Expenditure Share by Vehicle Type During Recessions:This pie chart represents the total advertising expenditure share by vehicle type during recession periods.

Effect of Unemployment Rate on Vehicle Type and Sales:This bar chart shows the effect of unemployment rate on automobile sales by vehicle type during recession periods.



Requirements to create the expected Dashboard

You will be creating two dropdown menus:

The first dropdown allows selection of the report type (Yearly Statistics or Recession Period Statistics).

The second dropdown is for selecting the year. This should be enabled only when the user selects Yearly Statistics report and will be disabled if Recession Period Statistics is selected.

Each dropdown will be placed within a separate division.
You can refer to this link for understanding the concept of dropdowns in plotly dash.

App Layout: This define the layout of the app, including titles, dropdown menus, and containers for displaying output.

Callback functions for Interactivity:

Update Input Container:

Here we define a callback function to update the input container based on the selected statistics.

The purpose of this function is to control the state (enabled or disabled) of the year dropdown based on the user's selection of the report type.

Specifically:

Enabled (returns True) when Yearly Statistics is selected, allowing the user to choose a year.

Disabled (returns False) when Recession Period Statistics is selected, preventing the user from selecting a year because it is irrelevant in the context of recession statistics.

Callback for Plotting:

Here we define a callback functions to update the output container based on selected statistics and year, creating various plots for the dashboard.

The four plots have to be displayed in 2 rows, 2 column representation
