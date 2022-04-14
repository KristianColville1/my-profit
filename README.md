# Rapid Silver

Developer: Kristian Colville

[Visit Rapid Silver](https://rapid-silver.herokuapp.com/)

(Image of final terminal)

## Table of Contents
* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owners Goals](#site-owners-goals)
* [User Experience](#user-experience-ux)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
* [User Stories](#user-stories)
    * [New User](#new-user)
    * [Returning User](#returning-user)
    * [Owner](#owner)
* [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Fonts](#color-scheme)
    * [Structure](#color-scheme)
    * [Wireframes](#wireframes)
* [Technologies & Tools](#technologies--tools)
    * [Main Tech](#main-tech)
    * [Python Packages Used](#python-packages-used)
* [Logic](#logic)
    * [Initial Flow](#initial-flow)
    * [Python Logic](#python-logic)
* [Features](#features)
* [Data Model](#data-model)
    * [Class Overview](#class-overview)
    * [Database Overview](#database-overview)
* [Testing](#testing)
    * [Testing User Stories](#testing-user-stories)
* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python validation](#python-validation)
        * [PEP8 validation](#pep8-validation)
        * [Linters](#Linters)
    * [LightHouse](#lighthouse)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Heroku](#heroku)
    * [Cloning this Repository](#cloning-this-repository)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)


## Project Goals

The goals of this project include:

- Designing a back-end application for users with in need of a software utility tool for business
- It should provide users with the ability to store and access data
- This is a CLI project so the application should work in a terminal
- Use the [python programming language](https://www.python.org/) to build the application

### User Goals

- To be able store and access an account within Rapid Silver
- Log in or create an account
- Add some form of data and manipulate it for specific needs

### Site Owners Goals

- Build a software utility tool for small business users
- Provide the ability for users to log in and create user accounts
- Design it so a user can set up a data in ways that are unique to them
- Build it using a [back-end language](https://en.wikipedia.org/wiki/Frontend_and_backend)

[Back to Top](#table-of-contents)

## User Experience
### Target Audience

- Any user who needs to use a software utility tool to analyze some form data
- Users who are self-employed or freelancing or run small businesses
- Users who may need to manage and update inventories of some form like employees/customers/products
- People starting new ventures in need to managing their new companies

### User Requirements and Expectations

- Clear navigation through the [CLI](https://en.wikipedia.org/wiki/Command-line_interface)
- Information provided to help guide users
- Any errors or actions are handled and work as expected
- There should be appropriate feedback displayed for the interactions provided
- Help should be provided where appropriate
- The user is guided through the program in a logical and meaningful way
- The user would expect to see log in options for the program
- Any user would expect the application to have a high degree of security

[Back to Top](#table-of-contents)

## User Stories
### New User

1. As a new user I want to understand how to use this CLI application
2. As a new user I want to create an account to store my personal information
3. As a new user I want to be able store and analyze some form of data

### Returning User

4. As a returning user I want to be able to log into the application
5. As a returning user I want to be able to update inventory/customers/products etc.
6. As a returning user I want to see available options

### Owner

7. As the owner I want my users data to be stored safely
8. As the owner I want my users passwords uniquely encrypted in the database for extra protection
9. As the owner I want users to see sample data and understand how to use the program

[Back to Top](#table-of-contents)
## Design
### Color Scheme

Although not a requirement for the CLI application some colors were chosen for the website containing the terminal. I chose to use Coolers to make a palette for the website. 

![Coolers colors](assets/images/rapid-silver.png)
### Fonts

As I mentioned above, the site itself was not a requirement for this project but fonts were chosen for the site containing the terminal.

I chose 'Anton', sans-serif as my website font. I got it from Google Fonts.

### Structure

The structure of the terminal application was designed to be easily navigated and in order of importance. The terminal consists of 80 columns and 24 rows. Each menu of navigation appears when needed.

- The application contains the following menus:
    - Welcome Menu with a prompt for the user to press enter so that the next menu can be printed to the terminal
    - Leading on from the welcome menu is another menu reminding the user of available options to them and prompting for the user to click enter again
    - After the user clicks enter on the reminder of options, the log in portal menu is shown and the user can either create a new account or log in as a returning user. This provides the user with flexibility to store and access their data.
    - Entering from the account creation route the next screens involve username and password validation and checking for conflicts in the database
    - From the login side for returning users the user is welcomed back.
    - Coming back to the main route in the main route menu which can be navigated seamlessly to and from the various options within

- From the main menu for the different selections the user has options for:
    - Setting up products
    - Setting up mailing lists
    - Setting up employee lists
    - Storing inventory/ updating inventory
    - Analyzing inventory data
    - Information on data protection
    - How data is stored and protected

### Wireframes

[Back to Top](#table-of-contents)
## Technologies & Tools
### Languages Used

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python)

### Frameworks, Libraries & Tools

- [Coolors](https://coolors.co/) to get palette colors for the website
- [Balsamiq](https://balsamiq.com/) used for creating wireframes for the terminal application
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) for checking and debugging the site in the browser
- [Font Awesome](https://fontawesome.com/) for the footer icons
- [Grammarly](https://app.grammarly.com/) for grammar and spell checking
- [Git](https://git-scm.com/) for version control with [VSCode](https://code.visualstudio.com/) to push commits to [GitHub](https://github.com/)
- [GitHub](https://github.com/) as a remote repository solution for project development
- [Google Fonts](https://fonts.google.com/) for the button and heading within the website hosting the terminal application
- [Heroku](https://dashboard.heroku.com) as a deployment solution and hosting the website containing the application
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) for validating CSS code 
- [JShint](https://jshint.com/) for validating JavaScript code
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) used inside [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) for testing the website hosting the terminal application
- [MongoDB](https://www.mongodb.com/) as a database solution for storing the users passwords
- [PEP8](http://pep8online.com/) for validating python code
- [Ubuntu](https://ubuntu.com/) as the operating system on the local machine
- [VSCode](https://code.visualstudio.com/) as a local repository
- [WC3 Validator](https://validator.w3.org/) for validating HTML code

### Python Packages Used

- [Colorama](https://pypi.org/project/colorama/) used for adding color to terminal
- [Bcrypt](https://pypi.org/project/bcrypt/) used to salt and hash passwords for new accounts and checking credentials for returning users
- [Better Profanity](https://pypi.org/project/better-profanity/) used in the user class to avoid profanity being entered
- [Getpass](https://docs.python.org/3/library/getpass.html) to hide the users password on the terminal for the user
- [OS](https://docs.python.org/3/library/os.html) used for manipulating and storing environment variables
- [Pymongo](https://pypi.org/project/pymongo/) for accessing the Mongo Database and storing users passwords
- [Random](https://docs.python.org/3/library/random.html) used for calculating random numbers and selecting random choices in the various classes
- [Sys] used to for accessing the system and exiting the program within the selection menu for the user
- [Time](https://docs.python.org/3/library/time.html) used throughout for adding delays between text on terminal and for the loading animations


[Back to Top](#table-of-contents)
## Logic
### Initial Flow
![Initial Flowchart](assets/images/flowcharts/rapid-silver.drawio.png)
### Python Logic
![Python Logic one](assets/images/flowcharts/python-logic.png)

[Back to Top](#table-of-contents)
## Features

[Back to Top](#table-of-contents)
## Data Model

### Class Overview
Object Orientated programming was used throughout the project. The CLI application consists of 4 classes and 1 subclasses.

- User
- PasswordManager
- DataManager
- ColorPrint
    - TextArt

### Database Overview


[Back to Top](#table-of-contents)
## Testing
### Testing User Stories


1. As a new user I want to understand how to use this CLI application

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

2. As a new user I want to create an account to store my personal information

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

3. As a new user I want to be able store and analyze some form of data

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

4. As a returning user I want to be able to log into the application

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

5. As a returning user I want to be able to update inventory/customers/products etc.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

6. As a returning user I want to see available options

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

7. As the owner I want my users data to be stored safely

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

8. As the owner I want my users passwords uniquely encrypted in the database for extra protection

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

9. As the owner I want users to see sample data and understand how to use the program

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<details>
<summary>See screenshot</summary>
</details>
<br>

[Back to Top](#table-of-contents)

## Validation
### HTML Validation
### CSS Validation
### JavaScript Validation
### Python validation
#### PEP8 validation
#### Linters
### LightHouse

[Back to Top](#table-of-contents)
## Bugs

| Bug | Fix |
| --- | --- |
| Environment variable for MongoDB password not being accessed, keep getting a NameError | Found the issue online and realized that the config variable was wrong, I removed the quotes and got access to the password for MongoDB |
| User not able to log into rapid silver | Discovered the issue was with the encoding for the password |
| Set mongo link as config var but not letting me create new accounts | Found the issue, unfortunately a typo was inserted into the environment variables name on Heroku, link was fixed |
| Type error being caught on account creation when user enters valid input, stuck on loop in menu | Converted the users input to a string and this resolved the issue |
| Bug found when user enters password incorrectly and then tries again, its not flowing properly after recursion | Found missing variable declarations and reassigned variables to password_one for checking and validation |
| Found an interesting bug when logging in after creating an account, it acknowledges the user is logged in but doesn't progress. I checked three times with the same data input and on the third try it works as intended | Checked the issue after some time and found that the recursion was one line above it's intended position. Issue resolved with relief |
| On testing routes and handling user errors I found that if a user enters wrong information that my handling of ValueError in password_manager is being used but not being raised effectively to be caught with the right intention | Issue resolved and error caught properly after indenting the intended code |
| Getting an AttributeError calling the users name from password manager object, I have not specified it as a private member but it is behaving as such | The username object was out of scope for the intended goal, I created an instance attribute and when password manager finishes main purpose it assigns the users name to it |
| After installing the Rich module, the terminal is reporting error and not loading terminal | Debugged and couldn't identify the issue so removed the virtual environment and reset it and the list of requirements for Heroku and it solved the issue |
| 1 | 2 |
| 1 | 2 |

[Back to Top](#table-of-contents)
## Deployment
### Version Control
I used [Visual Studio Code](https://code.visualstudio.com/) as a local repository and IDE & [GitHub](https://github.com/) as a remote repository.

1. Firstly, I needed to create a new repository on Github [rapid-silver](https://github.com/KristianColville1/rapid-silver).
2. I opened that repository on my local machine by copying the URL from that repository and cloning it from my IDE for use.
3. Visual Studio Code opened a new workspace for me.
4. I created files and folders to use.
5. To push my newly created files to GitHub I used the terminal by pressing Ctrl + shift + `.
6. A new terminal opened and then I used the below steps.

    - git add (name of the file) *This selects the file for the commit*
    - git commit -m "Commit message: (i.e. Initial commit)" *Allows the developer to assign a specific concise statement to the commit*
    - git push *The final command sends the code to GitHub*

### Heroku
As a deployment solution I chose [Heroku](https://dashboard.heroku.com).

To deploy a project using Heroku follow these steps:

- Log into heroku
- Go to the heroku dashboard
- Create a new app by selecting 'New'
- Give your application a name and select a preferred location
- Click the 'Create app' button
- If you have config variables in your application
    - Click on settings
    - Click 'Reveal config vars'
    - Input your deployment variables

- If you need specific build packs
    - Click on settings
    - Click on build pack
    - Add your packs as needed (Please be aware that the order matters)
    - For Rapid Silver, Python and then NodeJs was selected.

- Once these steps are completed
    - Go to the deploy section
    - Select your version control system
    - For Rapid Silver, GitHub was selected

- Connect your version control system
- Add your repository
- Connect the app selecting 'connect'
- Either choose automatic deployment or manual deployment
- Once all these steps are completed and the build is successful
    - You can click the 'view' button
    - It will reveal your deployed app
    
### Cloning this Repository
If you would like to clone this repository please follow the bellow steps.

Instructions:

1. Log into GitHub
2. Navigate to the repository you want to clone
3. Click on the green button labelled 'Code'
4. Copy the URL under the HTTPS option
5. Open an IDE of your choosing that has Git installed
6. Open a new terminal window in your IDE
7. Type this exactly: git clone the-URL-you-copied-from-GitHub
8. Hit Enter

You should have a local copy of the repository to use on your machine.

[Back to Top](#table-of-contents)
## Credits

Function for clearing the console if an error occurs taken from [Delf Stack](https://www.delftstack.com/howto/python/python-clear-console/).

[Back to Top](#table-of-contents)
## Acknowledgements
[Back to Top](#table-of-contents)