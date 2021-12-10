# Spinny-DRF
python manage.py makemigrations\
python manage.py migrate \
python manage.py createsuperuser <br>

Give staff access to users after creating users on http://localhost:8000/admin <br>

python manage.py runserver 

The API service consist of 4 URLs: <br>
1. To Add boxes\
   http://localhost:8000/add <br>
   contains 3 parameters : length,widh and height

2. To edit/update the boxes\
   http://localhost:8000/edit/<id>  <br>
   Here, ID is the id of box of you want to update\
   Example : http://localhost:8000/edit/21    

3. To delete the box\
   http://localhost:8000/delete/<id> <br>
   Here, ID is the id of box of you want to delete <br> 
   Example : http://localhost:8000/delete/21  <br>
  
4. To list all the boxes\
   http://localhost:8000/listAll/ <br>
   Also, to add filter link will be updated to something like:\
   http://localhost:8000/listAll/?user=&min_length=1&max_length=1&min_width=2&max_width=10&min_height=1&max_height=10&min_area=1&max_area=20&min_volume=&max_volume=&before_date= <br>
  
5. To list boxes created by the logged in user\
   http://localhost:8000/listMyBoxes/ <br>
   Also, after adding filter link will be like <br>
   http://localhost:8000/listMyBoxes/?user=&min_length=&max_length=&min_width=1&max_width=10&min_height=&max_height=&min_area=&max_area=&min_volume=&max_volume=&before_date=
  
