from flask import Flask
from flask_restful import Resource,Api
from models.a import A
from models.b import B

app = Flask(__name__)

# @app.route('/hello', methods=['GET'])
# def hello():
#     A.greetuser()
    
# @app.route('/hellotwo', methods=['GET'])
# def mehtod():
#     pass

# @app.route('/hellotwo', methods=['POST'])
# def mehtod():
#     pass

# #FLASK - restful 
# class HelloWorld(Resource):
#     def __init__(self,name) -> None:
#         self.name = name
    
#     def greetUser(self):
#         return f"Hello {self.name}"
    
# Api.add_resource(HelloWorld, '/greetUser')

# I have a route item . GET / POST 
# @app.route('/item', methods=['GET'])
# def get_item():
#     pass

# @app.route('/item', methods=['POST'])
# def create_item():
#     pass

# using FLASK restful
# CRUD , -> http methods  -> POST , GET, PATCH/PUT , DELETE -> post() , get() , put() , patch() , delete()
class Item(Resource):
    def get(self):
        pass
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass
    
Api.add_resource(Item, '/item')
