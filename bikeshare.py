import time
import pandas as pd
from tabulate import tabulate
# import numpy as np

pd.set_option("display.max_columns", 200)
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    cities = ['chicago', 'new york city', 'washington']
    city = input("Choose one of the cities: chicago, new york city, washington \n").lower()
    while city not in cities:
        city = input("You mistyped the city name! \n"
                     "Choose one of the cities: chicago, new york city, washington\n").lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Choose a month from January to June or all: \n').lower()
    while month not in months:
        month = input("You mistyped the month name! \n"
                      "Choose a month from January to June or all\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('Choose a day of the week or type all: \n').lower()
    while day not in days:
        day = input("You mistyped the month name! \n"
                    'Choose a day of the week or type all: \n').lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df.name = city
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[(df['month'] == month)]

    if day != 'all':
        df = df[(df['day_of_week'] == day.capitalize())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Month: ", df['month'].mode()[0])

    # display the most common day of week
    print("Day: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("Hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is: ",
          (df['Start Station'] + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: ", df['Trip Duration'].sum())

    # display mean travel time
    print("Mean travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    if df.name in ['chicago', 'new york city']:
        # Display counts of gender
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth: ", df['Birth Year'].min())
        print("Most recent year of birth: ", df['Birth Year'].max())
        print("Most common year of birth: ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    pd.set_option("display.max_columns", 200)
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        choice = input("\nWould you like to see 5 lined of row data? Enter yes or no.\n")
        start = 0
        while choice.lower() == 'yes':
            print(df.iloc[start:start+5])
            start += 5
            choice = input("more?\n")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
