import argparse
import pandas as pd
from data_helper import compare_growth_accross_regions_gender
from csv_helper import csv_helper
from global_var import states, sex, time


def city_population_increase(file1, file2):
    df = csv_helper(file1, file2)
    time2 = [2022, 2040]
    time3 = [2040, 2070]
    male_40, female_40 = compare_growth_accross_regions_gender(
                      df, time2, states[3], sex)
    male_70, female_70 = compare_growth_accross_regions_gender(
                      df, time3, states[3], sex)
    mf_40 = pd.concat([female_40, male_40],
                      keys=['Female', 'Male'], axis=1)
    mf_70 = pd.concat([female_70, male_70],
                      keys=['Female', 'Male'], axis=1)
    # Export to CSV
    mf_40.to_csv('../results/cli/text/city_pop_increase/city_pop_mf40.txt',
                 sep='\t')
    mf_70.to_csv('../results/cli/text/city_pop_increase/city_pop_mf70.txt',
                 sep='\t')
    print("Data stored : ../results/cli/text/city_pop_increase/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse German future population")
    parser.add_argument("files", nargs=2,
                        default=None, help="Path to the first CSV file")
    args = parser.parse_args()
    file1, file2 = args.files
    city_population_increase(file1, file2)
