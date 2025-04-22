# library_management_system


## Learning target
- [x] Understanding basic API + practice
- [ ] Understanding Flask basic components + practice
- [ ] Learning best approach (simplest) to deliver LMS project
- [ ] Learning interface for the project

      
## Preliminary internal discusion
- [] Data retainer? dict (json)--> only for proof of concepts
- [] Folder structure
- [] Flask dependencies


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


### References
- https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis
- https://medium.com/@hollyawheeler96/building-apis-and-restful-apis-in-flask-98b894507f76
- https://medium.com/@cakmak.erkut1/crud-operations-in-flask-with-restful-9de3148f32de
- https://medium.com/@zaidbinkhalid/handling-requests-in-flask-c7cdfd11e583
- https://medium.com/analytics-vidhya/understanding-flask-and-building-web-api-using-python-and-flask-5611e6f66e03
- https://medium.com/@dennisivy/flask-restful-crud-api-c13c7d82c6e5
