"""A simple date manipulation thing"""

from datetime import date, datetime

class InputError(Exception):
    """An exception class to handle expected problems"""
    pass

def get_birthday():
    # get input from the user - this will be a string
    bday_string = input("\nEnter your date of birth [DD/MM/YYYY]: ")
    try:
        # This code parses the string into a datetime and converts to a date
        # It will raise an exception if the input is not a valid date in the correct format
        return datetime.strptime(bday_string, "%d/%m/%Y").date()
    except ValueError:
        # Here we handle the ValueError potentially raised above and re-raise a more specific and useful error
        raise InputError("Invalid input '{}' (expecting valid date in 'DD/MM/YYYY' format)".format(bday_string))

def main():
    """Get user input and return some helpful feedback"""
    birthday = get_birthday()
    today = date.today()

    # raise an error for future dates
    if birthday > today:
        raise InputError("You haven't been born yet!")

    # Manipulate the data a bit
    age = today - birthday
    seconds = age.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    # Produce some output
    print("\nAt the time of your birth today you were/will be:")
    print("\n\t{:,.0f} seconds old".format(seconds))
    print("\n\t{:,.0f} minutes old".format(minutes))
    print("\n\t{:,.0f} hours old".format(hours))
    print("\n\t{:,.0f} days old".format(days))
    print("\n\t{:,.0f} years old".format(years))

if __name__ == "__main__":
    """Handle the potential error gracefully"""
    try:
        main()
    except InputError as exc:
        # If it raises an error we expect, then we can print the error message.
        print(exc)
    print("")
