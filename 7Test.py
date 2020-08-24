import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    cities = ['all','chicago', 'new york city', 'washington']
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = [ 'All', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday' , 'Sunday']

    city = ""
    month = ""
    day = ""
    while city not in cities:
        city = input("would you like to see data from chicago, new york city, washington: ").lower()

    while month not in months:
        month = input("which month 'january', 'february', 'march', 'april', 'may', 'june': ").lower()

    while day not in days:
        day = input("which day 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday' , 'Sunday': ").title()


    print('-'*40)
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # we are gonna use index to return exaxt month beacuse our data contain
        # months like that 1,2,3 ...,6 not name
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week to create the new dataframe
        if day != 'All':
            df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most Common Month Is: ",df['month'].mode()[0])

    # display the most common day of week
    print("The most Common Day Is: ",df['day_of_week'].mode()[0])


    # display the most common start hour
    print("The most Common Start Hour Is: ",df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("commonly used start station Is: ",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("commonly used end station Is: ",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("most frequent combination IS: ",(df['Start Station'] + ';' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print("total travel time: ",df['Trip Duration'].sum())
    # display mean travel time
    print("mean travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print("counts of user types: ",df['User Type'].count())
    # Display counts of gender
    try:
        print("counts of gender: ",df['Gender'].count())
    except KeyError:
        print("There's no column called df['Gender']")
    # Display earliest, most recent, and most common year of birth
    try:
        # Display earliest, most recent, and most common year of birth
        print("earliest year: ",df['Birth Year'].min())
        print("recent year: ",df['Birth Year'].max())
        print("common year: ",df['Birth Year'].mode()[0])
    except KeyError:
        print("There's no column called df['Birth Year']")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start = 5
    end = 10
    while True:
        user = input("Do you want to see raw data >>> Yes or No: ").title()
        if user == 'Yes':
            # this will return first five raw if user == yes otherwise break
            print(df.head())
            while True:
                # this will ask user if he wants to see more raw data
                more = input("Do you want to see More raw data >>> Yes or No: ").title()
                if more == 'Yes':
                    print(df.iloc[start:end])
                start +=5
                end += 5
                if more == 'No':
                    break

        elif user == 'No':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
