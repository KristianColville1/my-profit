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

- To be able store and access accounts for users of various types
- Log in or create an account
- Update, check and monitor products in order to forecast future events

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

- Coolors to get some colors for the HTML in the website
- Chrome Developer Tools for checking and debugging the site in the browser
- Font Awesome for the footer icons 
### Python Packages Used

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
Object Orientated programming was used throughout the project. The CLI application consists of 5 classes and 3 subclasses.

- User
    - RapidUser
    - Employee
- PasswordManager
- ColorPrint
    - TextPrint
- Company
- Product

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
| 1 | 2 |
| 1 | 2 |
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