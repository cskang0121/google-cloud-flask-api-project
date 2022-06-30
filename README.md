# Project Description

- This repository is for self-learning purposes
- Topic : Communication between Flask API and RDBMS

## Configuration & Running the Flask API 
1. Run ```pip install flask flask-restful``` if the packages is not already installed.
2. Run ```python3 flask_api.py``` to start the API on local server.
3. Now you can test the API with [Insomnia](https://insomnia.rest/download), i.e., an open source api client.

If you encountered the following error message on Insomnia while making a POST request :

```{ "message": "Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)" }```

Please change the setting from JSON to Plain on your Insomnia dashboard as shown below.

<img width="517" alt="Screenshot 2022-06-30 at 2 59 47 PM" src="https://user-images.githubusercontent.com/79074359/176613130-7d6f16ef-688a-43ec-b891-1d5d4f62db69.png">

## Resources

- Tutorial (Youtube) : https://www.youtube.com/watch?v=MF75aNH3Gjs
- Tutorial (Medium) : https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f

- What is an API endpoint? : https://rapidapi.com/blog/api-glossary/endpoint/
