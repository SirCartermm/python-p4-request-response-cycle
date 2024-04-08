from flask import Flask, request ,res
app = Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def index():
    # Get the request method
    method = request.method

    #Get the request data
    data = request.get_data()

    #Process the request and generate a response
    response = Response(f'Request method: {method}\nRequest data: {data}',mimetype='text\plain')

    #Return the response
    return response

if __name__ == '_main__'
    app.runO(debug=True)
    