from api_modules import data, DocIndex, Client

api = data.api
app = data.app


api.add_resource(DocIndex.DocIndex, '/')
api.add_resource(Client.ClientPost, '/user')
api.add_resource(Client.Client, '/user/<string:fullname>')

if __name__ == '__main__':
    app.run(debug=True)
