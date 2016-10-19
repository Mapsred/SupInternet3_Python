from api_modules import data, AddUser, GetUser, DocIndex

api = data.api
app = data.app


api.add_resource(DocIndex.DocIndex, '/')
api.add_resource(AddUser.AddUser, '/adduser')
api.add_resource(GetUser.GetUser, '/getuser')

if __name__ == '__main__':
    app.run(debug=True)
