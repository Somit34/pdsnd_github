import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        # get user input for city
        city = input('Enter city name (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a valid city name.')


    # get user input for month (all, january, february, ... , june)
    while True:
        # get user input for month
        month = input('Enter month (all, january, february, ... , june): ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input. Please enter a valid month or "all".')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        # get user input for day of week
        day = input('Enter day of the week (all, monday, tuesday, ... sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid input. Please enter a valid day or "all".')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" for no month filter
        (str) day - name of the day of the week to filter by, or "all" for no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('Calculating The Most Frequent Times of Travel...')
    print('Most Common Month:', df['Month'].mode()[0])
    print('Most Common Day of Week:', df['Day of Week'].mode()[0])
    print('Most Common Start Hour:', df['Hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', most_common_end_station)


    # display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most Frequent Combination of Start Station and End Station Trip:', most_common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {} seconds'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:')
    print(user_types)


    # Display counts of gender (if available in the dataset)
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nGender data not available for this city.')



    # Display earliest, most recent, and most common year of birth (if available in the dataset)
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('\nBirth year data not available for this city.')

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Prompt the user if they want to see raw data
        start_index = 0
        while True:
            raw_data_request = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if raw_data_request.lower() == 'yes':
                print(df.iloc[start_index:start_index+5])
                start_index += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
