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
I have the html code to structure my page, to form the basis of my pages._

#### CSS
_For my project this is what really bought life to my page, adding colour to the from the navigation bar, allowing me
to place a background of my choice, colouring the containers for the collapsibles where you can view, add and manipulate
information. This was helpful as it allowed me to differentiate the colours of for example, so elements that I needed to 
reflect different colours depending of if they clicked on or hovered over._

#### Javascript
_I needed to use some Javascript because for my code to function in terms of my date picker, collpasibles. This 
was needed as without it I was having some errors as it was causing the code not to run properly. I placed this in
my ("base.html") so I can extent this using a block ("{% extends 'base.html'%} {% block content %}"), this allowed
the scripts to be pushed onto other pages, saving me having to enter it on multiple pages._

#### Materialize

_This was very useful for certain functions like collapsible, buttons and forms. I liked using similar to bootstrap
, the code I had used ran due to including a Materialize Javascript link within my code. The benifit is not having create 
the code manually but be able to paste in a code and manipulate it to fit your needs._

# TESTING

#### HTML Validator 

_I used this html validator to check my code and make sure I do not have any syntax errors. I did this by 
going to ("https://validator.w3.org/") and selecting the validate by direct input; this simply alllowed
me to enter the whole html code, then once I did that I clicked the check button located beneath this section.
The validator helped me as I found that syntax errors can appear over just even a small mistake such as, a letter or symbol
iI did find this difficult at
the start as my code wouldn't function until I fixed the code. Whenever, I tried to fix the code I found it was always
a typo somewhere which was causing me problems. However, the main issue was my divs were closed properly or I had 
child elements closed after the parent. In the end fixing this helped me gain a better understanding of my code._
 
#### CSS Validator 
_This use of the validator was really helpful for me, as there were quite a few changes I had to make for my code to
run the color schemes I had chosen. In this situation if I did not have this, I would of find this difficult but I could 
of used inspect element. However, this would not of been productive as the time it would of taken to do this and Technologies
make the changes. To use this I went to ("https://jigsaw.w3.org/css-validator/"), which is slightly different url
compared to the one for my html. I entered the code in the same way using direct input, then clicking the check button
placed underneath._

#### Navigation Bar

_I did run into some trouble with this, as my logo name was placed on the right and I needed the links to show on the left.
Also, with my navigation bar I had the links falling below the bar, which meant part of the link text was being cut off.
I had change the padding for this, so I decided to inspect element by right clicking on the section and finding the area to target.
Once I worked that out the padding I could just adjust then copy the code into my style.css file. However, I could not just change
the side the links would be on by padding or margins. I had to really look at the code closely to realise there was a class
("class="right hide-on-med-and-down"), I had to the right to a left. In the end it seemed simple but it was different to what I had
used in bootstrap. This was a learning as even if am seeing similarities in bootstrap and materialize, they are different technologies._

#### Buttons

_For my project I did have some colours clashing because of the background colours and the text colour. This was difficult for me as 
I needed one set of colours for when I hover over the button, and another set when I am not hovering over. I used the class I had created
btn_small but as I did this, the colour would be the same in both conditions. I then using inspect element, next the filter selected :hov,
this allowed me to add a hover state. The filter is located above the code on the right hand side, when you inspect element._All

#### Select Genre

_This was the most difficult part as I really struggled at first as I could not what to target. I had to select state like the previous
section. Once I saw the colour changing through hover I changed the background-colour. I kept the colour black once it was outside the hover
state and this took me the longest to resolve._

# Deployment

#### Github
 
_I used github to post my code online as some issues I had with gitpod was if it timed out I would lose the code. I would first enter 
into the terminal ("git status"), to find any files that have not been submitted. Once I find they have not I would enter (" git add .")
so they are submitted. After I have gone past first two stages, I would enter ("git commit -m (enter reason for commit)"). When I had done this
I just had to push it online using command ("git push"). Now as I wanted to push the whole project online, I went to my github page where my 
repository was saved and clicked settings in the top of the page. After this I went to github pages and within there I selected source, as that had
a dropdown which was called master branch. Once I did this a green section appeared Your site is published at and this allows you to now access the project._

#### Gitpod

_For my project I have been using gitpod to create the project, and to commiting the code onto my github. I did find it easy as I used the code (git push),
it pushed my code instantly without having to enter my username and password. This ide is what allowed to create the code, create pages and folders which
really form my project. I did come across the difficulty as when it timed and I had to refresh the page, I was losing the all the code I had not previously
entered. This was difficult but I way I worked around this was simply (git commit -m "Enter Commit Here), this stopped me losing my code and it saved it for me._

# Created and Edited by Michael Singh
