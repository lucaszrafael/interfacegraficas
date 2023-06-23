from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from urllib import parse, request as req
# import json

app = Flask(__name__)
CORS(app)

@app.route('/api_gateway/<service>/<operation>')
def api_gateway(service, operation):

    if service == 'persistence':
        print("Persistência...") 
        url = 'http://localhost:5007'

        if operation == 'add_book':
            data = {'title':request.args.get('title'),
                    'author':request.args.get('author'),
                    'subject': request.args.get('subject'),
                    'publication_date': request.args.get('publication_date')}
            data_p = parse.urlencode(data).encode()                
            url_request = req.urlopen(url + '/' + operation,data=data_p)
            result = url_request.read()

        elif operation == 'list_books':
            url_request = req.urlopen(url + '/' + operation)
            result = url_request.read()

        elif operation == 'search_books':
            search = request.args.get('search')
            url_request = req.urlopen(url + '/' + operation + '/' + search)
            result = url_request.read()

        elif operation == 'get_book':
            book_id = request.args.get('id')
            url_request = req.urlopen(url + '/' + operation + '/' + book_id)
            result = url_request.read()

        elif operation == 'update_book':
            book_id = request.args.get('id')
            url = url + '/' + operation + '/' + book_id
            data = {'title':request.args.get('title'),
                'author':request.args.get('author'),
                'subject': request.args.get('subject'),
                'publication_date': request.args.get('publication_date')}
            data_p = parse.urlencode(data).encode()                
            url_request = req.Request(url = url, data = data_p,method = "PUT")
            result = req.urlopen(url_request).read()

        elif operation == 'delete_book':
            book_id = request.args.get('id')
            url = url + '/' + operation + '/' + book_id
            url_request = req.Request(url = url, method = "DELETE")
            result = req.urlopen(url_request).read()

        elif operation == 'list_subjects':
            url_request = req.urlopen(url + '/' + operation)
            result = url_request.read()

        elif operation == 'add_subject':
            data = {'name':request.args.get('name'),}
            data_p = parse.urlencode(data).encode()                
            url_request = req.urlopen(url + '/' + operation,data=data_p)
            result = url_request.read()

    return result
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

