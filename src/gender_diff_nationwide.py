import argparse
import matplotlib.pyplot as plt
import pandas as pd
from data_helper import compare_growth_accross_regions_gender
from csv_helper import csv_helper
from global_var import states, sex, time


def gender_diff_nationwide_plot(df, gender):
    # Create the bar plot
    if gender == 'female':
        df.drop(
            columns='Percentage Change').plot(kind='bar', figsize=(10, 6))
        plt.title('Population Comparison by State - Female')
        plt.xlabel('State')
        plt.ylabel('Population')
        plt.xticks(rotation=45)
        plt.savefig(
            '../results/cli/plots/female_population_change_2022-70.png')
        # Display the plot
        # plt.show()

    elif gender == 'male':
        df.drop(
            columns='Percentage Change').plot(kind='bar', figsize=(10, 6))
        plt.title('Population Comparison by State - Female')
        plt.xlabel('State')
        plt.ylabel('Population')
        plt.xticks(rotation=45)
        plt.savefig(
            '../results/cli/plots/female_population_change_2022-70.png')
        # Display the plot
        # plt.show()
    else:
        pass
    print("Plot successfully created in : ../results/cli/plots/")
    print("Data stored : ../results/cli/text/gender_diff/")


def gender_diff_nationwide(file1, file2):
    df = csv_helper(file1, file2)
    male, female = compare_growth_accross_regions_gender(
        df, time, states[3], sex)
    mf_combined = pd.concat([female, male], keys=['Female', 'Male'], axis=1)
    mf_combined.to_csv(
        '../results/cli/text/gender_diff/gender_diff_nationwide.txt', sep='\t')

    gender_diff_nationwide_plot(male, 'male')
    gender_diff_nationwide_plot(female, 'female')
    # print(mf_combined)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse German future population")
    parser.add_argument("files", nargs=2,
                        default=None,
                        help="Path to the first CSV file")
    args = parser.parse_args()
    file1, file2 = args.files
    gender_diff_nationwide(file1, file2)
