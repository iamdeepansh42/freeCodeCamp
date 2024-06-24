import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit for all data
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extend_all = pd.Series([i for i in range(1880, 2051)])
    sea_levels_all = intercept_all + slope_all * years_extend_all
    plt.plot(years_extend_all, sea_levels_all, 'r', label='Fitted Line (1880-2050)')

    # Create second line of best fit for data from year 2000
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extend_2000 = pd.Series([i for i in range(2000, 2051)])
    sea_levels_2000 = intercept_2000 + slope_2000 * years_extend_2000
    plt.plot(years_extend_2000, sea_levels_2000, 'g', label='Fitted Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data
    plt.savefig('sea_level_plot.png')
    return plt.gca()
