from website import create_app # importing from website

app = create_app()

if __name__ == '__main__': # with this condition app runs only when main.py runs
    app.run(debug=True) #Runs the application on a local development server.
                        #debug runs code changes