# Project Description

This project focuses on how to build a Flask API that enforces REST design principles. It is meant for beginner or intermediate learners to improve on coding knowledge and API architecture. Also, we will learn how to deploy this simple API on Google Cloud Platform! PS : Feel free to file an issue if you need any clarification.  

## Configuration & Running the Flask API 
1. Run ```pip install flask flask-restful``` if the package is not already installed.
2. Run ```python3 flask_api.py``` to start the API on local server.
3. Now you can test the API with [Insomnia](https://insomnia.rest/download), i.e., an open source api client.

If you encounter the following error message on Insomnia while making a POST request :

```{ "message": "Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)" }```

Please change the setting from JSON to Plain on your Insomnia dashboard as shown below.

<img width="517" alt="Screenshot 2022-06-30 at 2 59 47 PM" src="https://user-images.githubusercontent.com/79074359/176613130-7d6f16ef-688a-43ec-b891-1d5d4f62db69.png">

## Deployment of Flask API on Google Cloud

Upon testing the API logic with Insomnia, the API is ready to be deployed on Google Cloud. The step-by-step instructions are as follows:

1. Create a Google Cloud Platform(GCP) account.
2. Upon successful account creation, create a new project in the UI dashboard and you are able to retrieve the 'Project ID'.
3. Search for 'Cloud Build API' and enable it.
4. Install GCP SDK CLI [here](https://cloud.google.com/sdk/docs/install).
5. Follow the installation guide to install CLI service and setting the path.
6. Run ```gcloud app create --project=blissful-column-355016``` in the project terminal. Note that project is being set to YOUR OWN project id (the id shown above is mine).
7. You will be able to choose the region when you want the API engine located : ```Please enter your numeric choice:  7``` (7 represents asia-southeast1) 
8. After the app is successfully created, run ```gcloud components install app-engine-python``` in the project terminal.
9. To test if our API actually works before official deployment :
- Run ```pip install gunicorn``` 
- Run ```gunicorn -b :8000 main:app``` : This initialises and runs the app at port 8000.
- Copy and paste ```http://0.0.0.0:8000/users``` in the browser to see if the API is actually running smoothly.
- Run ```Ctrl + C``` to kill the running API.
10. Add app.yaml and requirements.txt in the project root folder.
11. Run ```gcloud config set project blissful-column-355016```
12. Run ```gcloud app deploy``` to officially deploy the API :

13. Now, retrieve the URL shown ```https://blissful-column-355016.as.r.appspot.com``` and the API is officially uploaded! Note that gcloud will create a .gcloudignore file for you to ignore unnecessary files.

## Credits 
> Special thanks to [James Briggs](https://www.youtube.com/watch?v=MF75aNH3Gjs) for creating this amazing project 🙏🏻

## Project Resources
- [Tutorial 1 (Youtube)](https://www.youtube.com/watch?v=MF75aNH3Gjs)
- [Tutorial 2 (Youtube)](https://www.youtube.com/watch?v=3fsIcMgUOY8&t=23s)
- [Tutorial (Medium)](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f)
- [What is an API endpoint?](https://rapidapi.com/blog/api-glossary/endpoint/)
- [IBM | REST API design principles](https://www.ibm.com/sg-en/cloud/learn/rest-apis)

## More Resources
- [Introduction to APIs in Python](https://www.youtube.com/watch?v=g_yMowQikOE)

