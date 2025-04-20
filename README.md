# library_management_system

### Parties involved 
- Librarian
- Members

| Parties         | Rights       | 
| :---         |     :---:      |  
Librarian | Edit: add/delete/lend/return a book |  
Members | Preview: check status |


### Action 
- Librarian
- Members

| Action         | Http Verb       | URL  Path       | Description       |               
| :---         |     :---:      |     :---:      |     :---:      |  
Read | GET |/api/member|Read a collection of members.
Create | POST |/api/member|Create a new member.
Read | GET |/api/member\<lname>|Read a particular member.
Update | UPDATE |/api/member\<lname>|Update an existing member.


| Action         | Http Verb       | URL  Path       | Description       |               
| :---         |     :---:      |     :---:      |     :---:      |  
Create | POST |/api/book|Create a new book.
Read | GET |/api/book\<lname>|Read a particular book.
Update | UPDATE |/api/book\<lname>|Update an existing book.
Delete | DELETE |/api/book\<lname>|Delete an existing book.
