import argparse
import matplotlib.pyplot as plt
import pandas as pd
from data_helper import create_df_based_on_states, percent_change
from data_helper import sum_df_by_state_all_ages
from csv_helper import csv_helper
from global_var import states, sex, time


def trend_plot(group, region):
    if region == 'east':
        # Create the bar plot
        index = ['Brandenburg', 'Sachsen', 'Sachsen-Anhalt', 'Thueringen']
        df_east = pd.DataFrame(group, index=index)
        # Plot the DataFrame
        df_east.drop(
            columns='Percentage Change').plot(kind='bar', figsize=(10, 6))
        plt.title('Population trend - east german states')
        plt.xlabel('State')
        plt.ylabel('Population')
        plt.xticks(rotation=0)
        # save the plot
        plt.savefig('../results/cli/plots/east_trend-2022-70.png')
        # Display the plot
        # plt.show()

    elif region == 'west':
        # Create the bar plot
        index = ['Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Bremen',
                 'Hamburg', 'Hessen', 'Niedersachsen',
                 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland',
                 'Schleswig-Holstein']
        df_west = pd.DataFrame(group, index=index)
        # Plot the DataFrame
        df_west.drop(
            columns='Percentage Change').plot(kind='bar', figsize=(10, 6))
        plt.title('Population trend -  est german states')
        plt.xlabel('State')
        plt.ylabel('Population')
        plt.xticks(rotation=0)
        # save the plot
        plt.savefig('../results/cli/plots/west_trend-2022-70.png')
        # Display the plot
        # plt.show()
    else:
        pass

    print(
        "Plot successfully created in: ../results/cli/plots/*_trend-2022-70.png")
    print("Data stored : ../results/cli/text/trends/")


def east_west_trend(file1, file2):
    df = csv_helper(file1, file2)
    group1_df = create_df_based_on_states(df, time, states[0], sex[2])
    group2_df = create_df_based_on_states(df, time, states[1], sex[2])
    # Calculate population for 2022 and 2070 for West and East states
    group1 = sum_df_by_state_all_ages(group1_df, time)
    group2 = sum_df_by_state_all_ages(group2_df, time)
    # Calculate percentage change
    group1_percentage_change = percent_change(group1, time)
    group2_percentage_change = percent_change(group2, time)
    group1.to_csv(
        '../results/cli/text/trends/west_trends_2022-70.txt', sep='\t')
    group2.to_csv(
        '../results/cli/text/trends/east_trends_2022-70.txt', sep='\t')
    trend_plot(group2, 'east')
    trend_plot(group1, 'west')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse German future population")
    parser.add_argument("files", nargs=2,
                        default=None, help="Path to the first CSV file")
    args = parser.parse_args()
    file1, file2 = args.files
    east_west_trend(file1, file2)
