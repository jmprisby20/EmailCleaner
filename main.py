# Jake Prisby

# Desc.: This program will work to clean the inbox of a given gmail account
#        This is the main file which handles io between with users and with config file

from pack import ConfigManager
from pack import test_creds
import keyring

CONFIG_HANDLER = ConfigManager()

# Check if program is in setup
import sys
if (len(sys.argv) > 1):
    # Here the user passed a runtime argument
    if sys.argv[1] == 'setup':
        # Get email login loop until valid credentials are given
        import imaplib # Import imaplib to test credentials
        login_status = False
        while(not login_status):
            # Get credentials
            uname = input('Enter your email: ')
            passw = input('Enter your password: ')
            # Attempt login with credentials
            try:
                test_creds(uname, passw) # Test these credentials
                # Here login was successful
                CONFIG_HANDLER.set_val('EMAIL', 'address', uname) # Save username
                keyring.set_password('Python_Email_Cleaner', uname, passw) # Save password to credential manager
                login_status = True # Break loop
            except Exception as e:
                # Here the login failed
                print('ERROR: Login Failed. ' + str(e))
        # Now setup email cleanup period
        period_status = False
        while (not period_status):
            try:
                num_days = int(input('Enter the cleanup period you desire in days: '))
                # Here a correct integer value has been inputted, save to ini
                CONFIG_HANDLER.set_val('EMAIL', 'cleanperiod', str(num_days))
                period_status = True # Break Loop
            except Exception as e:
                print('ERROR: Invalid input: ' + str(e))
    else:
        # Here the user passed an incorrect setup
        print('ERROR: Incorrect command line argument\nAdd argument "setup" to enter setup mode\nAdding no argument will run the script normally')
else:
    try:
        # Here the user didn't pass an argument, attempt to run program normally
        # Validate that user info is saved
        username = CONFIG_HANDLER.get_val('EMAIL', 'address')
        password = keyring.get_password('Python_Email_Cleaner', username)
        test_creds(username, password) # Now test the credentials
        period = CONFIG_HANDLER.get_val('EMAIL', 'cleanperiod')
        from pack import EmailHandler
        EMAIL_HANDLER = EmailHandler(username, password, int(period)) # Create handler for email account
        EMAIL_HANDLER.cleanup() # Run cleanup
    except Exception as e:
        print('ERROR: Failed to login with stored credentials, try running in setup mode again, ' + str(e))
