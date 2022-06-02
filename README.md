# Housing_price_app


# What?
<br>Create a Dockerfile that adds the flask app created as part of previous assignments.
<br>Expose the port 5000 in the Dockerfile
<br>Use guicorn command that adds the flask app as the entry point
<br>Build the docker image
<br>Test the docker image locally
<br>Push the Dockerfile to the repo

# How to Run Image
<br> 1. Build the Image from the Dockerfile using command ```docker build -t ombhuyan2710/nanotest:latest .```
<br> 2. To check if the image is created on local host and its size use command ```docker images```
<br> 3. Start a Container Using the Image. ```docker run --name nanotest -it ombhuyan2710/nanotest```
<br> 4. Once the image is running test the app on localhost,once the app is running fine stop and delete the container from docker Desktop.


# Screenshots



![Screenshot (31)](https://user-images.githubusercontent.com/92777791/169530173-ba3517de-d05f-4e0d-8a37-e09135c4e1b8.png)




![Screenshot (32)](https://user-images.githubusercontent.com/92777791/169530195-ccb8bc42-557b-49fd-87d9-a4550383df3e.png)





![Screenshot (33)](https://user-images.githubusercontent.com/92777791/169530210-4e885b8f-cb48-475b-ba45-f00a1e454672.png)


# How external user run the app
<br>1.clone the repo into their system.
<br>2. Run the app.py file.
<br>3. Browse the the link given below.

# Flask App URL
http://localhost:5000/

