from csv_helper import csv_helper


def create_df_based_on_states(df, year, states, sex):
    if states == 'all':
        # Filter based on Sex alone
        f_df = df[df['Sex'] == sex]
    else:
        # Filter based on Sex and State
        f_df = df[(df['State'].isin(states)) & (df['Sex'] == sex)]
    # Group and summarize by Age Group, Sex, and State
    summary = f_df.groupby(
        ['Age Group', 'Sex', 'State'])[year].sum().reset_index()
    return summary


def sum_df_by_state_all_ages(df, years):
    sum_pop = df.groupby('State')[years].sum()
    return sum_pop


def percent_change(df, years):
    df_year1 = sum_df_by_state_all_ages(df, years[0])
    df_year2 = sum_df_by_state_all_ages(df, years[1])
    df['Percentage Change'] = ((df_year2 - df_year1) / df_year1) * 100
    return df


def df_largest_change_relative_percent(df, years):
    df = percent_change(df, years)
    # df['Percentage Change'] = (df[2070] - df[year2]) / df[year1] * 100
    # Find the largest increase and decrease in percentage
    rel_increase = df.loc[df['Percentage Change'].idxmax()]
    rel_decrease = df.loc[df['Percentage Change'].idxmin()]
    return rel_increase, rel_decrease


def df_largest_change_absolute(df, years):
    df['Difference'] = df[years[1]] - df[years[0]]
    # Find the largest increase and decrease in absolute numbers
    abs_increase = df.loc[df['Difference'].idxmax()]
    abs_decrease = df.loc[df['Difference'].idxmin()]
    return abs_increase, abs_decrease


def pop_dif_cities(df, time, states, sex):
    # Question 1: Population size, Is there a difference between Hamburg,
    # Bremen and Berlin from 2022 - 2045 - 2070
    df = create_df_based_on_states(df, time, states, sex[2])
    city_pop = sum_df_by_state_all_ages(df, time)
    city_pop_percent = percent_change(city_pop, time)
    return city_pop_percent


def compare_growth_accross_regions_gender(df, time, states, sex):
    # Q4 Comparing nation wide data on total growth of male vs female
    male_df = create_df_based_on_states(df, time, states, sex[0])
    female_df = create_df_based_on_states(df, time, states, sex[1])
    sum_male_all_df = sum_df_by_state_all_ages(male_df, time)
    sum_female_all_df = sum_df_by_state_all_ages(female_df, time)
    percent_change_male = percent_change(sum_male_all_df, time)
    percent_change_female = percent_change(sum_female_all_df, time)
    # print(percent_change_male)
    return percent_change_male, percent_change_female


if __name__ == "__main__":
    compare_growth_accross_regions_gender()
    pop_dif_cities()
    create_df_based_on_states()
    sum_df_by_state_all_ages()
    percent_change()
    df_largest_change_absolute()
    df_largest_change_relative_percent()
