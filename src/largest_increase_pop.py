import argparse
from data_helper import create_df_based_on_states
from data_helper import sum_df_by_state_all_ages
from data_helper import df_largest_change_absolute
from data_helper import df_largest_change_relative_percent
from csv_helper import csv_helper
from global_var import states, sex, time


def largest_increase_pop(file1, file2):
    df = csv_helper(file1, file2)
    # Question 2: What state has the largest change from 2022 to 2070?
    # a) In absolute numbers
    # b) relative in percentage from its own population
    # Create DataFrame for all states
    all_states_df = create_df_based_on_states(df, time, states[3], sex[2])
    # Calculate absolute change from 2022 to 2070
    sum_pop = sum_df_by_state_all_ages(all_states_df, time)
    abs_increase, abs_decrease = df_largest_change_absolute(
        sum_pop, time)
    rel_increase, rel_decrease = df_largest_change_relative_percent(
        sum_pop, time)

    abs_increase.to_csv(
        '../results/cli/text/biggest_changes/absolute_increase.txt', sep='\t')
    rel_increase.to_csv(
        '../results/cli/text/biggest_changes/relative_increase.txt', sep='\t')
    abs_decrease.to_csv(
        '../results/cli/text/biggest_changes/absolute_decrease.txt', sep='\t')
    rel_decrease.to_csv(
        '../results/cli/text/biggest_changes/relative_decrease.txt', sep='\t')
    print(
        "successfully save the data in ../results/cli/text/biggest_changes/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse German future population")
    parser.add_argument("files", nargs=2,
                        default=None, help="Path to the first CSV file")
    args = parser.parse_args()
    file1, file2 = args.files
    largest_increase_pop(file1, file2)
