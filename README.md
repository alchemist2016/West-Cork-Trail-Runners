## Data Centric Development Project - Code Institute
---
# West Cork Trail Runners
Do you enjoy spending time in the nature? Do you love running and challenging yourself? Well we just might have the right thing for you. We are a small group of enthusiast who love running and open air. We have runners of all levels. The aim we are striving to is not who can run furthest or fastest but to share quality time together in a breathtaking scenery of West Cork and Kerry. Come join us on our next adventure!

#### Click on the picture to see live demo!
[![Demo](https://github.com/alchemist2016/Milestone3/blob/master/static/img/heroku.PNG?raw=true)](https://west-cork-trail-runners.herokuapp.com/)

---
## Summary
* [Project Background](#project-background)
* [User Experience](#ux)
    * [User Stories](#user-stories)
    * [Five planes](#strategy)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Information Architecture](#information-architecture)
* [Technology used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

---
## Project Background

Welcome to a Milestone 3 Project.

The main aim of this endeavor is to provide CRUD Create, Read, Update and Delete functionality to a website.

This project theme is based on a increasingly popular Trail running in West Cork and Kerry Counties. It is real existing group whom I have approached and asked for permission to build their website as my project, which they bravely accepted. So no pressure...

There is much to say about this topic but my priorities were to present skills in creating a fully operational website connected to NoSQL Mongo Atlas DB and deployed on Heroku server.

 [Back to top](#summary)

---

## UX
### User Stories
#### From the users perspective I would like to be able to:

* **see current members**
  - all members access and delete, edit existing members

<p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/img/members.PNG?raw=true" width="500" height="300" alt="Marketplace image">
</p>

* **see current trails**
  - access current trails and delete, edit them
  
<p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/img/trails.PNG?raw=true" width="600" height="300" alt="Trails">
</p>

* **User can Add New Members**
  - Adding new Members into DB 

<p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/img/addmember.PNG?raw=true" width="500" height="150" alt="Add new members">
</p>

* **User can Add New Trail**
  - user can add new trail to the db 
<p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/img/addtrail.PNG?raw=true" width="400" height="600" alt="Add new trail">
</p>

* **User can Contact the club**
  - user can write an email to the club and short description 
<p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/img/contact.PNG?raw=true" width="400" height="200" alt="Contact Us">
</p>

#### As a club, I would like to:
* **attract as many members as possible**
Promoting healthy life style and meeting new people

[Back to top](#summary)

### Strategy

**West Cork Trail Runners** is designed to support running community and to give opportunity and courage to people who are not familiar with this type of sport to join us.

### Scope

When I was designing this website I was planning first from backend functionality then the mobile first front end and UI design. The customer can easily surf through the pages and find relevant information about the club and it's members. Drop down menu in Nav Bar is available as well as burger menu on mobile sizes. All media queries are set to industry standards.

### Structure

User is greeted at home page with a short description of the club and image of forest trail. The user has nav bar with menu of all pages available as well as links in the footer. By clicking on a Nav Bar Logo user will be brought to home page.

Next page is Trails page where user can get informed about different trails including their start point, end point, description, difficulty and length. At the form for Trails user can use Edit button that will edit any currently saved trail, or delete button which will delete any picked trail. Form is drop down accordion style. Also there is a hero image in the background.

Editing and deleting will affect the information stored in a database also.

If Edit button is used user is brought to a new page called Edit Trail where there is a form with fields Trail Name, Starting Place, Ending Place, Description, Difficulty and Length. When Edit Trail button is clicked all fields are required and after submitting to database under section trail_running and user is brought back to Trails page where he can see his updated Trail.

Delete button will delete only the trail that is chosen.

Next page is Add Trail page where a user can add a new trail through form on the page. All fields are required and length of the trail is limited between 1km to 200 km. The Add Trail button will collect and store all the data from the form in a database under unique primary key.

Following Trails Section is the Members section. The Members page is formed with same accordion form as in Trails page to keep the consistency throughout the website. On the Form and bellow the Members Logo there are two buttons for edit and delete of the members. The form is gathering information about First Name, Last Name, Running Experience, Email and Date Joined. All fields are required with email being verified and date joined field which when clicked pops up a calendar for user to choose the date.

The delete button will delete member from the form and database.

If the user clicks the Edit button new Edit Member page will pop up where user can use the form that has fields for First Name, Last Name, Running Experience, Email, Date Joined. All fields are required and calendar pops up when date joined field is clicked so that user can choose a date.

Next page on the menu is Add Member page with a form consistent to Add Trail in design and with fields of First Name, Last Name, Running Experience, Email and Date Joined. All fields are required and validated as in other forms with calendar pop up for date joined. When user clicks the Add Member button the data will be stored in Members database and will bring user back to Members page where he can see his addition on the members form.

The last page of the website is the Contact us page where user can use a form to fill out Full Name and email and Enquiries that will be sent to designated email address through EmailJs API once Submit button is clicked.

Footer is visible on any page and icons themselves are clickable and leading to clubs Facebook, Instagram and YouTube pages.
All links are target_blank marked and will bring user to a new page opening thus keeping the integrity of the website.

#### Further description of buttons, icons and elements used is in the next section [Features](#existing-features).

### Wireframes

* **Home page**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/Home.jpg?raw=true" width="500" height="300" alt="Home page">
</p>

* **Trails page**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/Trails.jpg?raw=true" width="400" height="500" alt="Marketplace page">
</p>

* **Edit Trail**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/EditTrail.jpg?raw=true" width="500" height="300" alt="View advert">
</p>

* **Add Trail**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/AddTrail.jpg?raw=true" width="400" height="500" alt="Add/Edit page">
</p>

* **Members**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/Members.jpg?raw=true" width="400" height="500" alt="Add/Edit page">
</p>

* **Edit Member**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/EditMember.jpg?raw=true" width="400" height="500" alt="Add/Edit page">
</p>

* **Add Member**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/AddMember.jpg?raw=true" width="400" height="500" alt="Add/Edit page">
</p>

* **Contact**
  
  <p align="center">
  <img src="https://github.com/alchemist2016/Milestone3/blob/master/static/wireframes/ContactUs.jpg?raw=true" width="400" height="500" alt="Add/Edit page">
</p>
### Surface 
I am using throughout the website consistent coloring of Nav Bar and Footer as well as coloring of the forms, buttons, and fonts.


 + Main colors used throughout the web-site : 
    - Navigation bar - ![#ee6e73](https://placehold.it/15/ee6e73/000000?text=+) `#ee6e73`
    - Footer - ![#ee6e73](https://placehold.it/15/ee6e73/000000?text=+) `#ee6e73`
    - Body of the website - ![#00000)](https://placehold.it/15/00000/000000?text=+) `#00000`
    - Footer Links - ![#8f8f8f](https://placehold.it/15/8f8f8f/000000?text=+) `#8f8f8f`
    - Menu and Submit Buttons - ![ #4db6ac](https://placehold.it/15/4db6ac/000000?text=+) ` #4db6ac`

[Back to top](#summary)

---
## Features
### Existing Features
* Navigation bar
  -On the top of the Pages is Navigation Bar that is consisted of Logo which is wired to bring back to home page if clicked from any other page. Also on the right hand side is the drop down menu with hover effect and displaying links to all pages. On Mobile size the navbar contains Logo and on the left side a burger menu that links to all pages.

* Footer
  - Footer is always present on all sizes and displays social links that open in new tab.

* Trails
  - Trails page is consisting of accordion Materialize form that drop down when clicked with transparent background. It contains all relevant data for each trail. Data can be modified by edit button that leads to new page Edit Trial.
  - All fields are required.
  - Data can be also deleted by using Delete button. 

* Edit Trail 
  - Edit trail page is shown when user clicks the edit button on Trails page. It shows a form which can be filled with data and submitted to db and once submitted then the user will be returned to Trails page where in the form user can see new entry. All fields are required.

* Add Trail
 - Add Trail contains a form to enter details of new Trail. Once submitted to db it will bring back user to Trials page and show the new entry. All fields are required and length is limited to 1 - 200Km.
    
* Members
 - Members page has the same type of form as Trails page for consistency and ease of use. It has the same functionality as the form above and shows basic information about members. The Edit button is taking to new page called Edit Member.
 - Data can be also deleted by using Delete button.

* Edit Member 
  - Once on the Edit member page there is a form for basic information about the member. All fields are required and date joined has a pop up calendar that user can utilize. When the form is finished and the user clicks the Edit Member button the information is stored in db and it will bring the user back to Members page.

* Access key - security
  - On adding advert, user will be asked to put in "Access key" which will then be used for deleting or editing advert. It is made as a security measure from unauthorized deleting or editing on the site.

* Add Member
  - There is a standard form for filling out the basic members details and date joined with GUI calendar. Once user clicks the Add Member button the information from the form is stored in a db and user is brought back to the Members page.
  - All fields are required.

* Contact Us
  - On this page we have a form for the user if they decide to write to the club with their enquiries and questions. The form is connected to EmailJS API and emails to specific address all the queries. It will also print out Success in console window of dev tools. 

* Social icons
  - I have included 3 icons in the Footer that once clicked lead to a new tab with appropriate address and keeping the website always available to the user. For this I have used target=_blank attribute.

[Back to top](#summary)

### Future Features
  - For the future development I would certainly consider to use much more validation and backfeed to user if anything goes wrong. Also I could reduce the number of pages by introducing more action buttons if some of the forms. Further and more comprehensive testing is needed. 
  - 
[Back to top](#summary)

---
## Information Architecture

### Database
- For the Backend I have used the NoSQL database Mongo DB Atlas which is cloud based also [MongoDB](https://www.mongodb.com/). 

### Collections
 - Under Database called treck_running there are also two collections called:
 - member and
 - trail_running 
And they contain information from the forms in website whether for member or trail using these data types:
- ObjectId
- String
- Integer

### Data Structure 

Below is the data base collection:

Members Collection

[JSON file showing members collection structure](https://github.com/alchemist2016/Milestone3/blob/master/static/database/member.json) 

Trail Running Collection

[JSON file showing trail_running collection structure](https://github.com/alchemist2016/Milestone3/blob/master/static/database/trail_running.json) 


[Back to top](#summary)

---
## Technology used

* HTML5 & CCS3: 
* Materialize - 
 - https://materializecss.com/getting-started.html
 - Icons
 - Accordion form
 - Date picker for calendar
 - Nav Bar
 - Side Nav
* Font Awesome: icons library used for Social links
    - https://fontawesome.com/
* JavaScript and jQuery:
    - Used for form validation, calendar GUI, EmailJS API
    - https://jquery.com/
* EmailJS: API that is free and easy to apply.
    - https://www.emailjs.com/
* Python: Python is used as a programming language which is a back bone of the Backend and logical functionality
    - https://www.python.org/
* Flask: Lightweight WSGI web application framework. 
    - https://palletsprojects.com/p/flask/
* MongoDB: NoSQL document-oriented database program that uses JSON like documents with schema used by the site to store user detail and trail details.
    - https://www.mongodb.com/
* Github: Provides hosting for software development version control using Git and is used to store this projects repository.
    - https://github.com/
* Heroku: Cloud platform as a service supporting several programming languages and is used to deploy this project
    - https://www.heroku.com

[Back to top](#summary)

---

## Testing

### Testing section is located [here](https://github.com/alchemist2016/Milestone3/blob/master/testing.md)

### Validating code
HTML
 - code is validated through [W3 validator](https://validator.w3.org/).

CSS
 - code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

JavaScript
 - code is validated through [JS Hint](https://jshint.com/).

Python
 - code is validated through [PEP8](http://pep8online.com/).

 [Back to top](#summary)

---

## Deployment
The project was written and developed in the Gitpod IDE.

A local repository was initialized using Github. Regular changes were committed to the local repository.

The process for deployment on Heroku was:

  -Create a new app in Heroku with "west-cork-trail-runners"
  - In the workspace, log into Heroku with command Line and the set of commands provided to create a connection between the application and Heroku.
  - Create a new Git repository and add the files, then associate the Heroku application and push to Heroku once the requirements.txt file and Procfile have been created.
  - Configuration variables had to be set in order to get the project running. These had to be set in both the Gitpod IDE and on Heroku. These included, PORT, IP and Mongo URL.
  - Open the app to test successful deployment.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/alchemist2016/Milestone3.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to top](#summary)

---

## Credits
### Content
+ All content was written by myself and by users.

### Acknowledgement
* Videos on [CodeInstitute](https://codeinstitute.net/).
* Thanks to my tutor Cormac for feedback and ideas.
* w3 Schools.
* StackOverflow
*Background photos are used from [Unsplash](https://unsplash.com/) and from private stock of images property of West Cork Trail Runners.
* Big thanks to tutors in CodeInstitute and Roman Grubic for helping me with formatting ReadMe file.

#### This is for educational use.
[Back to top](#summary)