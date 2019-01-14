# Questioner-endpoints

[![Build Status](https://travis-ci.com/isaacizey/Questioner-endpoints.svg?branch=develop)](https://travis-ci.com/isaacizey/Questioner-endpoints)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[![Maintainability](https://api.codeclimate.com/v1/badges/270ba701286a85bbbc78/maintainability)](https://codeclimate.com/github/isaacizey/Questioner-endpoints/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/isaacizey/Questioner-endpoints/badge.svg)](https://coveralls.io/github/isaacizey/Questioner-endpoints)
# Framework 

Python 3.6, Flask

# overview
Crowd source questions for a meetup.Questioner helps the meetup organizer prioritize questions to be answered. Other uses can vote on asked questions and they bubble to the top or bottom of the log.

# Objctive 
Create API that power front end pages for questioner apllication

**The api should :**

 - Create a meetup record.
 - Create a question record
 - Get a specific meetup record.
- Get all meetup records.
- Upvote or downvote a question.
- Rsvp for a meetup

** API **
| Endpoint | Functionality |
----------|---------------
GET /index | View all questions and answers
POST /auth/signup | Register a user
POST /auth/login | Login a user
GET /questions | Fetch all questions
GET /questions/&lt;questionID&gt; | Fetch a specific question
POST /questions | Post a question
DELETE /questions/&lt;questionID&gt; | Delete a question
POST /questions/&lt;questionID&gt;/answers | Post an answer to a question
PUT /questions/&lt;questionID&gt;/answers/&lt;answerId&gt; | Mark an answer as accepted, or edit an answer

# Installation and Deployment
1. clone the github repository
`git clone https://github.com/isaacizey/Questioner-endpoints.git`
2. Install the requirments 
`pip install -r requiremnt.txt`
