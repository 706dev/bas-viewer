# BAS Viewer
This project is made specifically to display images and videos on a BAS (big ass screen).

## Building Locally

Information that is relevant to this Django app is in `docker-compose.yml`. 

Variables you should definitely change:
 - `DJANGO_SUPERUSER_USERNAME`
 - `DJANGO_SUPERUSER_PASSWORD`

As long as you have Docker and docker-compose installed, you can just run 
```
docker-compose up -d
```

Doing that will run the service in a Docker container as a daemon. 

## Usage
After you have the app running visit `localhost:8000/admin`. Log in with the credentials mentioned above. Click `Contents`, then the `Add Content` at the top right. 

You can now navigate to `localhost:8000` to have a loop of your added content.

If you are pointing a different machine to this address make sure to replace `localhost` with the machine's IP address.