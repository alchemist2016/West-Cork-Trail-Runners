## Summary
* [Responsiveness](#responsiveness)
* [CRUD](#crud)
    * [Create](#create-advert)
    * [Read](#read-advert)
    * [Update](#update-advert)
    * [Delete](#delete-advert)
* [Overall](#overall)
    * [Navigation](#navigation)
    * [Breadcrumbs](#breadcrumbs)
    * [Search and Filter](#search-and-filter)
    * [Most viewed/recent section](#section)
    * [Button "Go to top"](#button-"go-to-top")
    * [Pagination](#pagination)
    * [Footer](#footer)

#### Back to [Readme.md](https://github.com/romangrubic/database-project)

---

## Responsiveness
This site was was tested on multiple browsers (Google Chrome, Mozzila Firefox and Opera), multiple mobile devices (Samsung Galaxy, Huawei, Sony) and tablet device(Samsung Galaxy Tab) and it shown responsivness and compatibility.
Web-site is responsive for screens from 350px to 2k. Everything is in order and responsive. But, viewing it on a 4k desktop, Home page carousels are too small and they cover 2/3 of the width. 
Marketplace adverts card are 4 in a row and they appear stretched. It would be great if they would be showing 6 in a row instead of 4. Add advert and Edit advert are small pages and there is not enough content on them to fill a 4k screen height.
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Viewing on mobile device | Images adapted, no side adverts visible | As Expected | Pass |
| Viewing on tablet device | Side adverts visible, adverts not breaking out | As expected | Pass |
| Viewing on laptop device | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 2k | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 4k | All in order, no distortion | Home page distorted in carousel section, Marketplace page adverts are too big, on pages Add and Edit, footer is not covering bottom enough  | Fail |

[Back to top](#summary)

---

## CRUD

CRUD functionality is working as expected, no errors.

### Create Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Submit` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking on `Submit` button after filling all the forms | Redirect to the home page and the advert is added | As expected | Pass |
| Clicking on `Cancel` button | Redirect to the home page | As expected | Pass |


### Read Advert
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on advert cards | Displays advert in View advert page | As Expected | Pass |


### Update Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Edit` button | Displays `Access key` modal | As Expected | Pass |
| Typing wrong `Access key` in modal | Open 403 Page | As Expected | Pass |
| Typing correct `Access key` in modal | Opens Edit advert page | As Expected | Pass |
| Clicking outside modal | Closes `Access key` modal | As Expected | Pass |
| Clicking on `Save` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking `Save` button after changing some of the forms | Redirect to the view advert page and the advert is edited | As expected | Pass |
| Click on `Cancel` button | Cancel all changes and redirects to view advert page | As expected | Pass | 



### Delete Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Delete` button | Display `Access key` modal | As Expected | Pass |
| Typing wrong `Access key` in modal | Open 403 Page | As Expected | Pass |
| Typing correct `Access key` in modal | Deletes advert and redirects to Home page | As Expected | Pass |
| Clicking outside modal | Closes `Access key` modal | As Expected | Pass |

[Back to top](#summary)

---

## Overall

### Navigation 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Logo button | Opens "Home" page | As Expected | Pass |
| Clicking on `Marketplace` link | Opens "Marketplace" page | As expected | Pass |
| Clicking on `Add advert` link | Open "Add advert" page | As expected | Pass |

### Breadcrumbs 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on a link in breadcrumbs | Opens that specific page | As Expected | Pass |


### Search and Filter

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on filter button when choosing Motors | Displays all the adverts with category of "Motors" | As Expected | Pass |
| Clicking on filter button when choosing Home | Displays all the adverts with category of "Home" | As Expected | Pass |
| Clicking on filter button when choosing Electronics | Displays all the adverts with category of "Electronics" | As Expected | Pass |
| Searching for a word or part of a word | Shows all adverts with searched word in the name | As Expected | Pass |
| Searching for a word or part of a word that is NOT in database| Shows 404 Page with the users search entry | As Expected | Pass |
| Searching for a county | Shows all adverts in the searched county | As Expected | Pass |
| Searching for keyword with county | Shows all adverts with keyword in the searched county | As Expected | Pass |
| Clicking on `Additional` | Toggles `div` with search options and button | As Expected | Pass |
| Clicking on `Search` button without selecting options | Tooltip with "Select item from list" shows | As Expected | Pass |
| Clicking on `Choose category` | Shows list of categories | As Expected | Pass |
| Clicking on `Choose county` | Shows list of counties | As Expected | Pass |
| Clicking on `Search` button after selecting options | Results that have the selected options show up | As Expected | Pass |
| If there is no results with selected options | Shows 404 Page with the users selected options | As Expected | Pass |


### Section

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Most viewed advert` | Toggles div with Most viewed advert | As Expected | Pass |
| Clicking on `Most recent advert` | Toggles div with Most recent advert  | As Expected | Pass |
| Clicking on an advert | Open that advert in view advert page | As Expected | Pass |




### Button "Go to top" 

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Go to top` button | Scrolls up to top of the page | As Expected | Pass |



### Pagination
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `<< Previous` button | Open the previous page (if on page 3, open page 2) | As Expected | Pass |
| Clicking on button with page number | Opens that page (if clicked on `3`, opens third page)  | As Expected | Pass |
| Clicking on `Next >>` button | Open the next page (if on page 2, open page 3) | As Expected | Pass |


### Footer 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on My projects `Weather 360°` icon | Opens "Weather 360°" project in new tab | As Expected | Pass |
| Clicking on My projects `Memory game` icon  | Opens "Memory game" project in new tab | As expected | Pass |
| Clicking on `Github` icon | Opens "Github" profile in new tab | As expected | Pass |
| Clicking on `LinkedIn` icon | Opens "LinkedIn" profile in new tab | As expected | Pass |
| Clicking on `E-mail` icon | Opens contact modal for user to contact me | As expected | Pass |
| Clicking on `Submit` button without filling e-mail modal form | User is not able to send | As expected | Pass |
| Clicking on `Submit` button after filling e-mail modal form | Changes `Submit` button from red to green and modal closes itself  | As expected | Pass |

[Back to top](#summary)

