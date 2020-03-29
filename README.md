## Game Database

# Motivation

_The purpose of this project was allow the user to add, use and Manipulate date. I created the project to have three sections (home, add review, manage genre) 
this was placed in the top left, just to make this simple for the user to navigate._

### Navigation Bar

_For the design of my project I could have gone two ways; seperate pages for sections or jump links allowing users to move from section to
section instead of having seperate pages. I decided to go with the latter as it gives the page a more simplistic approach. _The

### Home 

_This can be found in the top left corner, allowinng user the to view all the reviews created. Also, I have created an " a href=/get_reviews" so the 
user can simply move back to the home page by simply clicking the link". For this to be possible, I create app route and by using "/get_reviews", 
this is simply a function that will access my database which is on mongo db as function contains the code "reviews.html",reviews=mongo.db.reviews.find())",
this finds the review which is within

### Add Review

_The add review link I have placed next to the home link allowing the user to jump to the page so you can create a review. This was made possible by
adding a (form action{{url for('insert_review')}}), by doing this it would allow the information I have entered to create a new review and be submitted.
I have made another app route but this time add_review and this will include the page addreview.html, this page includes all the code that creates the sections 
that would fill in to create a review. I made this possible by using sections from my mongo db database that include information such as, 
(review_name, review_content, review_date) and this basically created format for each review that has been created._

### Manage Genre

_This link allows the user to add, edit and manipulate genre for the reviews. I had simply created a container which includes (<li>) which allowed me to create horizontal
collapsible headers which contained two buttons; a delete, an edit button and an add genre button at the bottom of the page. For the edit genre and delete genre buttons
I had to create two app routes and place them inside a ({{url_for}}) within the buttons I had created. For example, if you click on the delete genre button, it would jump
back to the page showing all the genre, which would show the remaining genre that have been created._


### Review sections

_I have decided to use a collapsible accordian to allow the user to simply click and the section will reveal the review content, clicking again will
simply hide the content. The sections do include buttons that will allow the user to delete the review showing or edit the review. I needed to pull through
the names of the genre listed on my mongo db database, for that to be possible ({{genre.game_genre}}) by doing this it pullled through the names of the genre
as game_genre is the name of the section of my database which includes the name of the genre._

## Credits

_All the review content and images have been used for the purpose of this project created and I do not 
take credit for any of the content. For my game review project I have used images to form the background, and
the content for the basis of the reviews you can see._

## Backgrounds
_I had looked a number of background that would naturally fit with colour scheme I have chosen for my game 
database project. However, this did not work out as the text would not align or the image would conflict with 
the footer. In the end I came across the current background image by searching the image in https://www.google.com/
, this generated a number of images. I selected the image and it bought me to 
(https://wallpapersmug.com/w/download/1080x1920/jump-spider-man-in-avengers-infinity-war-0419d1).
I saved the image by right clicking, and saved to my directory on my computer I am using. The Credits
go the site as this image used just for project purpose._

# Technologies

#### HTML
_The html used in my project was to create the links for the sections in my project such as (home, manage genre and
add review). I used this mainly the structure of my buttons, the labels such as the name of the buttons and the
footer you seen on all of the pages. I have used to for my scripts in my (base.html) so that means the pages I 
have created will have them scripts as they have been extended using ({% extends 'base.html'%} {% block content %})
. Also, within my (nav-wrapper) I used a class with (brand logo-right) so I could use text as a logo right of my page.
I have the html code to structure my page, to form the basis of my pages 

#### HTML Validator 

_I used this html validator to check my code and make sure I do not have any syntax errors. The validator
helped me as I found that syntax errors can appear over just even a small mistake such as, a letter or symbol
iI did find this difficult at
the start as my code wouldn't function until I fixed the code. Whenever, I tried to fix the code I found it was always
a typo somewhere which was causing me problems. However, the main issue was my divs were closed properly or I had 
child elements closed after the parent. In the end fixing this helped me gain a better understanding of my code._

#### CSS Validator 

# TESTING