from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

# initialise flask application
app = Flask(__name__)

# initialize flask api
api = Api(app)

# initilize database path
db_path = "./database/users.csv"

# initialise endpoint : "Users" 
# inherit from "Resource" class for accessing common api methods
class Users (Resource):

    # To test GET request : http://127.0.0.1:5000/users
    def get(self):

        # read CSV
        data = pd.read_csv(db_path)  
        # convert dataframe to dictionary
        data = data.to_dict()   
        # return data and 200 OK code    
        return {'data': data}, 200  

    # To test POST request : http://127.0.0.1:5000/users?userId=abc123&name=The Rock&city=Los Angeles
    def post(self):

        # initializev
        parser = reqparse.RequestParser()  

        # add arguments
        parser.add_argument('userId', required=True)  
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        # parse arguments to dictionary
        args = parser.parse_args()  

        # read CSV
        data = pd.read_csv(db_path)

        if args['userId'] in list(data['userId']):
            return {
                'message': f"'{args['userId']}' already exists."
            }, 401
        else:
            
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'userId': args['userId'],
                'name': args['name'],
                'city': args['city'],
                'locations': [[]]
            })

            # add the newly provided values
            data = data.append(new_data, ignore_index=True)

            # save back to CSV
            data.to_csv(db_path, index=False)  

            # return data with 200 OK
            return {'data': data.to_dict()}, 200  

    # To test PUT request : http://127.0.0.1:5000/users?userId=abc123&location=0007
    def put(self):

        # initialize
        parser = reqparse.RequestParser()  

        # add args
        parser.add_argument('userId', required=True)  
        parser.add_argument('location', required=True)

        # parse arguments to dictionary
        args = parser.parse_args()  

        # read CSV
        data = pd.read_csv(db_path)
        
        if args['userId'] in list(data['userId']):
            # evaluate strings of lists to lists
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['userId'] == args['userId']]

            # update user's locations
            user_data['locations'] = user_data['locations'].values[0] \
                .append(args['location'])
            
            # save back to CSV
            data.to_csv(db_path, index=False)

            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404

    # To test DELETE request : 
    def delete(self):

        # initialize
        parser = reqparse.RequestParser()  

        # add userId arg
        parser.add_argument('userId', required=True)  

        # parse arguments to dictionary
        args = parser.parse_args()  
        
        # read othe CSV
        data = pd.read_csv(db_path)
        
        if args['userId'] in list(data['userId']):

            # remove data entry matching given userId
            data = data[data['userId'] != args['userId']]
            
            # save back to CSV
            data.to_csv(db_path, index=False)

            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:

            # otherwise we return 404 because userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404


# Bind the path "/users" to endpoint
api.add_resource(Users, '/users')

# Run the Flask app on local server
if __name__ == '__main__':
    # Set debug to True instructs Flask to automatically reload the server whenever changes are made
    app.run(debug=True)

