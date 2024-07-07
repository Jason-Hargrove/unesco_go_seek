# UNESCO-Go-Seek

UNESCO-Go-Seek is a web application that suggests random UNESCO cities to visit. The project uses Django for the backend and Vue.js with Bootstrap for the frontend.

![Screenshot](images/unesco-go-seek-00.jpg)

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

## Create and Apply Migrations:

1.  ```zsh
    python manage.py makemigrations
    ```
2.  ```zsh
    python manage.py migrate
    ```

    #### Run the Script:

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

## Notes:

- Run Migrations on Heroku

  ```zsh
  heroku run python manage.py migrate
  ```

- Run the collectstatic command locally and commit the changes to make sure the static files are collected and pushed to Heroku.

  ```zsh
  python manage.py collectstatic --noinput
  git add staticfiles
  git commit -m "Collect static files"
  git push heroku main
  ```

## Troubleshooting

- Sometimes, Django’s static files cache can cause issues. Clear the cache by running this in the root:

  ```zsh
  python manage.py collectstatic --noinput
  ```

- Clearing your browser cache and rebuild the Vue.js project to ensure no cached versions of the old code are being used:

  - In Chrome: Go to Settings > Privacy and Security > Clear browsing data

- If you suspect caching issues, you can force a hard refresh in your browser:
  - In Chrome: Cmd + Shift + R (Mac) or Press Ctrl + F5 on (Win)
