import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city 'chicago', 'new york city', 'washington': ").lower()
        if city in CITY_DATA:
            break
        else: 
            print('Invalid city.')
    # TO D0 O: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month 'january', 'february', ... 'june' or 'all': ").lower()
        if month in MONTHS:
            break
        else: 
            print('Invalid Month.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'april', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Choose a day 'monday', 'tuesday', ... 'sunday' or 'all': ").lower()
        if day in days:
            break
        else: 
            print('Invalid day.')
            
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
    # convert to datetime the Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # add colum m = month and dow = day of week
    df['m'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.day_name().str.lower()

    # filter month
    m = MONTHS.index(month)
    if m != 0:                                  # 0 = all else is a month
        df = df[df['m'] == m]               # filter by num of month

    # filter by day 
    if day != 'all':
        df = df[df['dow'] == day]       # filter by day of week to create the new dataframe

    return df

def time_stats(df):
    try: 
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        print('- The most common month is: ' + MONTHS[df['m'].value_counts().idxmax()].title())

        # TO DO: display the most common day of week
        print('- The most common day of week is: ' + df['dow'].value_counts().idxmax().title() )

        # TO DO: display the most common start hour
        print('- The most common start hour is: %s ' % df['Start Time'].dt.hour.value_counts().idxmax() )

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except :
        print("An error has occurred in the query to the DataFrame")

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:     
        # TO DO: display most commonly used start station
        print('- The most commonly used start station is: ' + df['Start Station'].value_counts().idxmax())

        # TO DO: display most commonly used end station

        print('- The most commonly used end station is: ' + df['End Station'].value_counts().idxmax())

        # TO DO: display most frequent combination of start station and end station trip
        start,end = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('- The most frequent combination of start station and end station trip is: ' + start + ' and ' + end )

    except:
        print("An error has occurred in the query to the DataFrame")
        if  'Start Station' not in df.columns : 
            print("Column Start Station does not exist") 
        if  'End Station' not in df.columns : 
            print("Column End Station does not exist") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):  
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:  
        # TO DO: display total travel time
        print('- Total travel time is: %s' % df['Trip Duration'].sum())

        # TO DO: display mean travel time
        print('- Mean travel time is:  %s' % df['Trip Duration'].mean())

    except:
        print("An error has occurred in the query to the DataFrame")
        if  'Trip Duration' not in df.columns : 
            print("Column Trip Duration does not exist") 
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:
        # TO DO: Display counts of user types
        usertype = df['User Type'].unique()
        print(f"- There are { len(usertype)} user types: {usertype}")

    # TO DO: Display counts of gender

        print(f"- Counts of gender: {df['Gender'].value_counts()} \n")
        
    # TO DO: Display earliest, most recent, and most common year of birth

        print(f"\n- Earliest year of birth: {df['Birth Year'].min()}")
        print(f"- Most recent year of birth: {df['Birth Year'].max()}")
        print(f"- Most common year of birth: {df['Birth Year'].value_counts().idxmax()}")
        
    except :
        print("An error has occurred in the query to the DataFrame")
        if  'User Type' not in df.columns : 
            print("Column User Type does not exist") 
        if  'Gender' not in df.columns : 
            print("Column Gender does not exist") 
        if  'Birth Year' not in df.columns : 
            print("Column Birth Year does not exist") 
        
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_rows(df):
    """Show DataFrame rows."""
    view_display = input("Do you want to see 5 rows of data? Enter yes or no : ").lower()
    if view_display == 'yes':
        start_loc = 0 
        while (start_loc <= len(df)): 
            print(df.iloc[start_loc : (start_loc + 5) ])             
            view_display = input("Do you want to continue viewing 5 more lines? Enter yes or no : ").lower()
            if view_display != 'yes':
                break
            start_loc += 5 
    print('-'*40)
    
# Edited comment in Github Project
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_rows(df)

        restart = input('\n Would you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()