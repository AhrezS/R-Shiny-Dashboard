# R-Shiny-Dashboard
Interactive Data Dashboard built using R and Shiny

# Data Analytics Dashboard Project

## Overview
This project is an **Interactive Data Dashboard** developed using **R Shiny**. It allows users to filter and visualize business data, helping to make data-driven decisions. Additionally, it includes a **Python script** for automating data cleaning tasks.

## Project Features
- **Data Filtering**: Filter data by product category and profit range.
- **Dynamic Plotting**: Choose between different types of plots (Line Plot, Bar Chart, Scatter Plot) to visualize relationships between variables.
- **Interactive Data Table**: View filtered data in a dynamic, sortable table.
- **Downloadable Data**: Download the filtered data in CSV format.
- **Data Cleaning**: Python script for cleaning and processing raw data files.

## Technologies Used
- **R**: For building the Shiny web app and creating interactive visualizations.
- **Shiny**: Framework used for developing the web dashboard.
- **ggplot2**: Library used for creating dynamic plots.
- **dplyr**: For data manipulation and filtering.
- **DT**: For creating interactive tables.
- **Python**: For data cleaning automation.
- **pandas, matplotlib**: Python libraries used in the data cleaning script.

## Python Code:
The Python code in this repository performs the following tasks:
1. Loads the sales data from a CSV file.
2. Cleans the data by handling missing values, removing duplicates, and standardizing the format.
3. Categorizes sales and order quantities into 'Low', 'Medium', and 'High' categories.
4. Generates various visualizations (e.g., bar charts) to analyze revenue by product.
5. Saves the cleaned and categorized data to a new CSV file.

## Installation

### R Shiny App:
1. Clone this repository:
   ```bash
   git clone https://github.com/AhrezS/R-Shiny-Dashboard
