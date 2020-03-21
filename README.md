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

### Review sections

_I have decided to use a collapsible accordian to allow the user to simply click and the section will reveal the review content, clicking again will
simply hide the content. The sections do include buttons that will allow the user to delete the review showing or edit the review._