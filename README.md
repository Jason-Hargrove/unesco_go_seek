# UNESCO-Go-Seek

UNESCO-Go-Seek is a web application that suggests random UNESCO cities to visit. The project uses Django for the backend and Vue.js with Bootstrap for the frontend.

![Screenshot](images/unesco-go-seek-00.jpg)

## Links to Work

- Repo: [https://github.com/Jason-Hargrove/unesco_go_seek.git](https://github.com/Jason-Hargrove/unesco_go_seek.git)
- App: [https://unesco-go-seek-fd9ceca95862.herokuapp.com/](https://unesco-go-seek-fd9ceca95862.herokuapp.com/)

## Technologies Used

- Python 3.x
- Django
- Vue.js
- Bootstrap
- Node.js and npm

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Node.js and npm
- Vue CLI

## Install Dependencies

1. Install Python dependencies:

   ```zsh
    pip install -r requirements.txt
   ```

2. Install Node.js dependencies:
   ```zsh
    cd cities/frontend
    npm install
    cd ../..
   ```

## Create and Apply Migrations:

1.  ```zsh
    python manage.py makemigrations
    ```

2.  ```zsh
    python manage.py migrate
    ```

    #### Run and Load the Script Data:

3.  ```zsh
    python load_data.py
    ```

## Verify Vue.js Build

1. Navigate to the `frontend` directory

   ```zsh
   cd cities/frontend
   ```

2. Build the Vue.js project

   ```zsh
   export NODE_OPTIONS=--openssl-legacy-provider
   npm run build
   ```

3. Copy the Build Files to the "static" Folder From the frontend Directory:
   ```zsh
   cp -r dist/* ~/Documents/code/projects/unesco_go_seek/static/
   ```

## Run the Development Server

1. Start the Django Development Server from the root directory:

   ```zsh
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/`

## Deployment Checklist

- Ensure the dist folder is correctly built and contains the required files.
- Confirm the static folder in the root directory has the files copied from the dist folder.
- Verify the collectstatic command runs without warnings or errors.
- Check Heroku logs for any issues related to static files.

## Heroku

- Collect Static Files

  ```zsh
  heroku run python manage.py collectstatic --noinput
  ```

- Push to Heroku

  ```zsh
  git add .
  git commit -m "My message"
  git push heroku main
  ```

- Run the Management Command on Heroku

  ```zsh
  heroku run python manage.py load_cities --app unesco-go-seek
  ```

- Run Migrations on Heroku

  ```zsh
  heroku run python manage.py migrate --app unesco-go-seek
  ```

- After running the migrations, you can check it:

  ```zsh
  heroku run python manage.py showmigrations
  ```

## PSQL

- Verify Tables

  ```zsh
  heroku login
  heroku pg:psql --app unesco-go-seek
  ```

- List All Tables

  ```sql
  \dt
  ```

## Steps for Updating and Deploying

1. python load_data.py
2. Commit Changes
3. Push Changes to Heroku
4. Run Migrations on Heroku
5. Load Data on Heroku
6. Collect Static Files
7. Restart the Heroku App (optional)

   ```zsh
   heroku restart --app unesco-go-seek
   ```

8. Verify Tables

## Troubleshooting

- Sometimes, Django’s static files cache can cause issues. Clear the cache by running this in the root:

  ```zsh
  python manage.py collectstatic --noinput
  ```

- Clearing your browser cache and rebuild the Vue.js project to ensure no cached versions of the old code are being used:

  - In Chrome: Go to Settings > Privacy and Security > Clear browsing data

- If you suspect caching issues, you can force a hard refresh in your browser:

  - In Chrome: Cmd + Shift + R (Mac) or Press Ctrl + F5 on (Win)

- view the latest logs from Heroku
  ```zsh
    heroku logs --tail --app unesco-go-seek
  ```
