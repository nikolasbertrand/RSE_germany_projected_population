import pandas as pd
import argparse


def age_group(data):
    # Remove row with a total value in the age column and convert each into int
    df = data[data['Age'] != 'all'].copy()
    df.loc[:, 'Age'] = df.loc[:, 'Age'].astype(int)

    # Replace every value within the year column with a Float
    for column in df.columns:
        if isinstance(column, int):
            df[column] = df[column].str.replace(',', '.').astype(float)

    # Add column Age group include correct labels for each age group
    age_ranges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69',
              '70-79', '80-89', '30-99', '100-109']

    # Add age group to dataframe
    df.loc[:, 'Age Group'] = pd.cut(df['Age'], bins=age_ranges,
                                    labels=labels, right=False)
    return df


def de_germanize(data):
    # Remove German language elements that will get annoying for non german
    # speakers/keyboar-d users. Umlaute etc.
    df = data.replace(
            {'[äÄ]': 'ae', '[öÖ]': 'oe', '[üÜ]': 'ue', 'unter 1 Jahr': '0'},
            regex=True)
    df = df.replace(
            {'-Jaehrige': '', 'maennlich': 'male', 'weiblich': 'female',
             'Insgesamt': 'all', '100 Jahre und mehr': '100',
             'Geburten, LE und WS moderat (G2L2W2)': 'moderate LE WS'},
            regex=True)
    return df


def combine_data_frame(file1, file2):
    # Read the two CSV files
    df1 = pd.DataFrame(file1)
    df2 = pd.DataFrame(file2)

    # Drop the last 24 lines/rows of the dataframe
    droprows = 24
    df1, df2 = df1[:-droprows], df2[:-droprows]
    # Remove header from the second dataframe
    df2 = df2[1:]
    # Concatenate the two dataframes vertically
    combined_df = pd.concat([df1, df2], ignore_index=False)

    # add a correct header
    header = ['State', 'Variant', 'LE WS', 'Sex', 'Age', 2022,
              2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070]
    combined_df.columns = header
    return combined_df


def csv_helper(file1, file2):
    # Read the CSV file, skipping the header and top rows
    # Genesis Tables have a weird formatmating thus encoding latin1
    df1 = pd.read_csv(file1, skiprows=7, sep=';', encoding='latin1')
    df2 = pd.read_csv(file2, skiprows=7, sep=';', encoding='latin1')

    # Combine data frames and remove German language umlaute and QoL renaming
    df = combine_data_frame(df1, df2)
    df = de_germanize(df)
    df = age_group(df)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CSV helper: cleans + combines 2 csv")
    parser.add_argument("file1", help="Path to the first CSV file")
    parser.add_argument("file2", help="Path to the second CSV file")
    args = parser.parse_args()
    csv_helper(args.file1, args.file2)
