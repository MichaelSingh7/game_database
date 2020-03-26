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
back to the page showing all the genre, which would show the remaining genre that have been created.


### Review sections

_I have decided to use a collapsible accordian to allow the user to simply click and the section will reveal the review content, clicking again will
simply hide the content. The sections do include buttons that will allow the user to delete the review showing or edit the review._