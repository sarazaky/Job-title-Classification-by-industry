# Job-title-Classification-by-industry
(Multi-text Text Classification Task)
In order to run the application (via cmd)

1- Download the repository

2- create a virtual enviroment >py -m venv .env  ((optional))

3- activate the virtual environment  >.env\scripts\activate  ((optional))

4- install libraries from requirements.txt  >pip install -r requirements.txt

5- run the app >flask run     (or)      >python app.py

______________________________________

then you can go to http://127.0.0.1:5000/ in the browser to test the prediction model and get the result in html GUI form

to get the result as json format you can test  http://127.0.0.1:5000/predict_api/teacher   (( you can replace teacher with any job title ))
___________________________________________

to see a test for predict_api from cmd :

1- while the server is running open another cmd window

2- navigate to the repository folder 

3- activate the virtual environment  >.env\scripts\activate

4- run request.py     >request.py "teacher"   (( you can replace teacher with any job title ))
