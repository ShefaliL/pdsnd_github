import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington':'washington.csv'}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs.
    cities = ('chicago','new york city', 'washington')
    '''generating a while loop to take input from user and simultaneously handling invalid inputs using if-else conditions.'''
    while True:
        city = input('\nPlease select the city you like to see the data for Chicago,New York City or Washington? ').lower()
        if city not in cities:
            input("\nInvalid city. Try again")
            break
        else:
            time = input("\nWould you like to analyse using month, day or all: ")

    # TO DO: get user input for month (all, january, february, ... , june)
        if time == 'month':
            months = ['january', 'february','march','april','may','june']
            '''obtaining input of duration of months from january to june from the user and handling the invalid inputs using if-else clause.'''
            month = input("\nPlease enter the month january, february, march, april, may, june or all: ").lower()
            if month not in months:
                input("\nInvalid month. Try again")
                break
            day='all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif time =='day':
            day = input("\nNow enter a day you need a data of? sunday,monday,tuesday,wednesday,thursday,friday,saturday or all: ").lower()
            days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            '''getting input from user for the weekdays while taking care of invalid inputs'''
            if day not in days:
                input("\nInvalid day. Try again")
                break
            month= 'all'
        else:
            input('\nAnswer not valid, please try again:')
            print(city,month,day)
        print('-'*40)
        return city, month, day


def load_data(city, month, day):
    '''generating a function to load data to help in searching for a particular query'''
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    if month != 'all':
        months = ['january', 'february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    '''defining a function for calculating the most frequent time of travelling'''
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    '''displaying most common intervals of travelling in  particular month'''
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(common_month)


    # TO DO: display the most common day of week
    '''displaying most common day of week in a month'''
    df['day_of_week'] = df['Start Time'].dt.day
    common_day = df['day_of_week'].mode()[0]
    print(common_day)


    # TO DO: display the most common start hour
    '''displaying most common  start hour in a week'''
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    '''displaying most popular destinations that users choose to travel'''
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    '''generating most common starting station'''
    comman_start_station = df['Start Station'].mode()[0]
    print(comman_start_station)

    # TO DO: display most commonly used end station
    '''calculating most common terminating station'''
    comman_end_station = df['End Station'].mode()[0]
    print(comman_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    '''calculating the required combination of starting and ending station trips'''
    df['Combination Station'] = str(df['Start Station'])+' TO '+str(df['End Station'])
    common_combination_station = df['Combination Station'].mode()[0]
    print(common_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    '''calculating trip duration of a particular trip'''
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    '''displaying total time travelled'''
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # TO DO: display mean travel time
    '''calculating mean travel time'''
    average_travel_time = df['Trip Duration'].mean()
    print(average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    '''generating a record of an user who has previously travelled'''
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('No gender found')

        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No Birth Year in this city')
    else:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print(most_recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def ask_view(df):
    '''asking user if  few lines of raw data is to be displayed'''
    while True:
        r = input('Would you like to see 5 lines of raw data?(Yes/No)').lower()
        if (r=='yes'):
            rc=input('Would you like to see  \n1. First 5 Lines \n2. Last 5 Lines \n(1/2):')
            if(rc=='1'):
                print(df.head(5))
            elif(rc=='2'):
                print(df.tail(5))
        else:
            break;

#Main function comment (refactoring)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
