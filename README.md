# UNESCO-Go-Seek

UNESCO-Go-Seek is a web application that suggests random UNESCO cities to visit. The project uses Django for the backend and Vue.js with Bootstrap for the frontend.

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

3. Copy the Build Files to the static Directory:
   ```zsh
   cp -r dist/* ../static/
   ```

## Run the Development Server

1. Start the Django Development Server from the root directory:

   ```zsh
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/`

## Troubleshooting

- Sometimes, Django’s static files cache can cause issues. Clear the cache by running this in the root:
  ```zsh
  python manage.py collectstatic --noinput
  ```
