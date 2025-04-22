# library_management_system

### Resources to manage
- Members
- Books


### Endpoints

- Members

| Action         | Http Verb       | URL  Path       | Description       |               
| :---         |     :---:      |     :---:      |     :---:      |  
Read | GET |/api/member|Read a collection of members.
Create | POST |/api/member|Create a new member.
Read | GET |/api/member\<lname>|Read a particular member.
Update | UPDATE |/api/member\<lname>|Update an existing member.


- Books

| Action         | Http Verb       | URL  Path       | Description       |               
| :---         |     :---:      |     :---:      |     :---:      |  
Create | POST |/api/book|Create a new book.
Read | GET |/api/book\<lname>|Read a particular book.
Update | UPDATE |/api/book\<lname>|Update an existing book.
Delete | DELETE |/api/book\<lname>|Delete an existing book.



### Folder structure
Reference: https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy