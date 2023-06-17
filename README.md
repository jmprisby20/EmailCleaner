# Python Gmail Inbox Cleaner

## Introduction

The purpose of this program is to clean out the inbox of a given gmail account.

## Features

- Designed to be run on schedule via a task manager.
- Uses keyring to store credentials securely.
- Logs are generated which list the subject of every email that was deleted during run time.

## Requirements

This script was developed using python version 3.11.4. The only additional requirement is the keyring library which can be installed using the following command: `pip install keyring`

## Instructions 

To set up script first run the script with the following command line arguments: `python main.py setup`.
This will run the script in setup mode which will allow the user to setup which gmail account they want to use and how old they want the deleted emails to be.

Once the script is setup it can be run using no command line arguments like follows: `python main.py`.
NOTE: Emails that are starred will not be deleted, also emails are just removed from inbox and not completely deleted.
