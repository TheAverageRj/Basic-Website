from Website import create_app

app = create_app()

#Only we run this file (not import), will execute line
if __name__ == '__main__':
    app.run(debug=False) #Run flask application and open the webserver. Any update will be applied to webserver
    
