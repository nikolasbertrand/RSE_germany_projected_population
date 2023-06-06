import argparse
import matplotlib.pyplot as plt
from data_helper import pop_dif_cities
from csv_helper import csv_helper
from global_var import states, sex, time


def population_dff_plot(city_df):
    # Create the bar plot
    city_df.drop(
        columns='Percentage Change').plot(kind='bar', figsize=(9, 6))
    plt.title('Population Comparison for Cities')
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.xticks(rotation=0)
    plt.legend(loc='upper right')
    # save the plot
    plt.savefig('../results/cli/plots/city_state_comparison_2022-70.png')
    # Display the plot
    # plt.show()
    print(
        "Plot successfully created in : ../results/cli/plots/city_state_comparison_2022-70.png")
    print(
        "Data stored : ../results/cli/text/city_state_comparison_2022-70.txt")


def population_diff_22_70(file1, file2):
    df = csv_helper(file1, file2)
    city_df = pop_dif_cities(df, time, states[2], sex)
    city_df.to_csv(
        '../results/cli/text/city_state_comparison_2022-70.txt', sep='\t')
    population_dff_plot(city_df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse German future population")
    parser.add_argument("files", nargs=2,
                        default=None, help="Path to the first CSV file")
    args = parser.parse_args()
    file1, file2 = args.files
    population_diff_22_70(file1, file2)
