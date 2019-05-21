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
