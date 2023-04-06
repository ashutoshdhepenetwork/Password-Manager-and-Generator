# Password-Manager-and-Generator
This program generates and manages secure passwords in Python, allowing users to generate, save, and check passwords using a command-line interface.
Password Generator and Manager
This program is a password generator and manager written in Python. It allows users to generate strong, random passwords, save them to a file, and check whether a password is correct for a given name.

Installation
To use the password generator and manager, you'll need to have Python 3.x installed on your system. You can download Python from the official website.

Next, you'll need to install the required libraries by running the following command:

Copy code
pip install -r requirements.txt
This will install the necessary libraries for the program to run.

Usage
To use the password generator and manager, run the password_manager.py file using Python. This will start the program and present you with a menu of options:

markdown
Copy code
1. Generate a password
2. Save a password
3. Check a password
4. Quit
To generate a password, select option 1 and enter the desired length of the password. The program will generate a random password using a combination of letters, numbers, and symbols.

To save a password, select option 2 and enter a name for the password (e.g. "Gmail", "Bank Account", etc.) and the password itself. The password will be hashed using the SHA-256 algorithm for added security and saved to a file.

To check a password, select option 3 and enter the name of the password you want to check. The program will prompt you to enter the password and will check whether it matches the hashed password stored in the password file.

To quit the program, select option 4.

License
This program is licensed under the MIT License.





