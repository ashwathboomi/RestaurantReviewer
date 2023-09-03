# RestaurantReviewer
## Created a Full Stack application using Django and React for users to submit reviews for restaurants in a certain area

*Code contained in the master branch*

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/a459b1d4-b087-43c0-8dc7-f303a965c996)

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/b2f17091-8d3e-43c0-8c2a-99467f829d4e)

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/10c5abe3-838e-43dc-9391-d0bc12aef90a)

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/dcbbc924-b407-46bf-9563-7407aea9d567)

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/7b18d15e-9f4a-4e38-8374-f4eed7ebc927)

All pages contain a navigation bar on the top to quickly visit other pages. 

The home page displays all the locations as buttons. Clicking on them will redirect you to a page that contains the restaurant reviews in that location (receiving data from the backend database) with the more recent reviews being on top. 

The review page allows users to submit reviews that are stored in the backend database. The message must be under 500 characters, and the rating must be within 0-100.

To run the webpage locally, clone the master branch and run the following commands in the terminal/commmand prompt :

```
cd backend/project
python manage.py runserver
```
Ensure the directory hierarchy looks similar to this:

![image](https://github.com/ashwathboomi/RestaurantReviewer/assets/113210547/7ae13ae8-5683-4a43-9048-a7c59857bb63)

UPDATE 8/25/2023:

A future iteration of the webpage will include a user authentification to allow only verified critics to submit reviews for different restaurants. A search bar will be implemented to allow any user to search for a specific restaurant and view all the reviews for it.   





