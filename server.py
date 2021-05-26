from flask_app import app

from flask_app.controllers import controller_note,controller_user,controller_account,controller_media,countroller_search

if __name__ == "__main__":
    app.run(debug=True)