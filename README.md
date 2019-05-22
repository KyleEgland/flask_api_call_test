# Flask API Call Test
This repository is for reference.  Please use it if you find it useful!

## Environment File
This repository uses an environment file (.env) that must be created locally.  This file normally contains secrets, which is why it is not synced here.  Please find an example below:

```
FLASK_APP=flask_api_call_test.py
SECURITY_KEY=development
FLASK_ENV=development
# This is for linux
DATABASE_URL=sqlite:////home/<username>/<dir_to_repos>/flask_api_call_test/app.db
# This is for Windows
DATABASE_URL=sqlite:///C:/Users/<username>/<dir_to_repos>/flask_api_call_test/app.db
```

## Credits
There are, generally, a lot of online resources that I use to accomplish my coding tasks.  Should you find anything is the repository useful, please patronize these additional resources or, at the very least, credit them in your own work if you clone/fork this for your own purposes.

* [Using jQuery to Update a Page Without Refresh (Part 1 of 2)](https://youtu.be/Kcka5WBMktw) by [Pretty Printed](https://prettyprinted.com/)
* [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by [Miguel Grinbert](https://blog.miguelgrinberg.com/index)
