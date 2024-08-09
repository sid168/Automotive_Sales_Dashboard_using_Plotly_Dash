# Automotive Sales Dashboard

## Aim
The aim of this project is to analyze historical trends in automobile sales, focusing on how these trends were affected during periods of recession. Specifically, the goal is to provide insights into the sales performance of XYZAutomotives, a company specializing in automotive sales, during economic downturns.

This dashboard project serves as a demonstration of skills in creating visualizations using Plotly and Dash. The project involves preparing a report on findings from an analysis of automobile sales data, with two primary reports being developed:

1. **Yearly Automobile Sales Statistics**
2. **Recession Period Statistics**

The analysis covers the period between 1980 and 2023.

## Components of the Report

### 1. Yearly Automobile Sales Statistics
This report includes the following visualizations:

- **Yearly Automobile Sales (Line Chart):** 
  - Displays the average automobile sales for each year across the entire period.

- **Total Monthly Automobile Sales (Line Chart):** 
  - Shows the total monthly automobile sales for a selected year.

- **Average Vehicles Sold by Vehicle Type (Bar Chart):** 
  - Illustrates the average number of vehicles sold for each vehicle type in the selected year.

- **Total Advertisement Expenditure by Vehicle Type (Pie Chart):** 
  - Represents the total advertising expenditure for each vehicle type in the selected year.

### 2. Recession Period Statistics
This report includes the following visualizations:

- **Average Automobile Sales Fluctuation Over Recession Periods (Line Chart):** 
  - Displays the average automobile sales for each year during recession periods.

- **Average Number of Vehicles Sold by Vehicle Type (Bar Chart):** 
  - Shows the average number of vehicles sold for each vehicle type during recession periods.

- **Total Expenditure Share by Vehicle Type During Recessions (Pie Chart):** 
  - Represents the total advertising expenditure share by vehicle type during recession periods.

- **Effect of Unemployment Rate on Vehicle Type and Sales (Bar Chart):** 
  - Illustrates the effect of the unemployment rate on automobile sales by vehicle type during recession periods.

## Dashboard Requirements

### Dropdown Menus

Two dropdown menus are created for user interaction:

1. **Report Type Selection:**
   - Allows the user to choose between "Yearly Statistics" or "Recession Period Statistics."

2. **Year Selection:**
   - Enables the user to select a specific year, but only when "Yearly Statistics" is selected. This dropdown is disabled when "Recession Period Statistics" is chosen, as the year selection is not applicable.

### App Layout
The app layout is structured to include titles, dropdown menus, and containers for displaying the output of the selected report type. The four visualizations are displayed in a 2x2 grid layout (2 rows and 2 columns).

### Callback Functions for Interactivity

1. **Update Input Container:**
   - A callback function controls the state (enabled or disabled) of the year dropdown based on the selected report type:
     - If "Yearly Statistics" is selected, the year dropdown is enabled.
     - If "Recession Period Statistics" is selected, the year dropdown is disabled.

2. **Callback for Plotting:**
   - Callback functions are used to update the output container based on the selected report type and year. The relevant plots are generated and displayed within the dashboard.

## Visualization Example

Below is an example of how the dashboard might be structured:

```
---------------------------------------------------
|       Yearly Automobile Sales (Line Chart)      |
---------------------------------------------------
|       Total Monthly Sales (Line Chart)          |
---------------------------------------------------
|       Average Vehicles Sold (Bar Chart)         |
---------------------------------------------------
|       Advertisement Expenditure (Pie Chart)     |
---------------------------------------------------
```

## Conclusion
This dashboard provides a comprehensive view of how automobile sales have been impacted during different economic conditions, particularly during recession periods. By interacting with the dashboard, users can gain insights into the trends and make data-driven decisions based on historical sales performance.
