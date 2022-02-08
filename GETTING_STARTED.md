# Setting the development environment
Setting up containerised stuff is painful - I have Googled it and this is what you need to do.

## Frontend
For frontend people, it is probably sufficient to just run the Vue.js cli on your machine and spoof the JSON api - then we can handle integration later :grimacing: .

To run basic dev server:
1. cd into frontend_dev
2. npm run serve
This will run a dev server for the website on localhost.

Still need to set up JSON spoof.
**All this may seem confusing, but please watch the Vue crash course video in the frontend discord that will literally explain everything.**

## Backend

### Getting Docker running

1. Ensure you have Docker installed.
   - Windows users should install [WSL2](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10) (I recommend using the Ubuntu distro), then install [docker desktop](https://www.docker.com/products/docker-desktop), and set it up [as shown](https://imgur.com/a/xcgPMLA)
   - Linux (and Mac?) users can either install [docker desktop](https://www.docker.com/products/docker-desktop), or install it [directly to their machine](https://docs.docker.com/engine/install/)

5. Copy the `.env` file in the private `#links` channel in the discord to `<repo>/mentorship/.env`

3. To start up the system, run the command (you may need to disable particularly aggressive firewalls):

   ```bash
   docker-compose up --build
   ```

   This will take some time when first run (many node modules to install), but should take tens of seconds every time after.

4. Whilst the docker containers are running, the site can be accessed by the URL (http *not* https): [http://localhost:8000](http://localhost:8000)

5. To kill the containers, interrupt with `Ctrl+c`, and they will shut down gracefully

### Troubleshooting

1. Problems can come from containers not shutting down correctly. To fix this, run `docker compose down` , then go back to step (3)
2. Problems can also come from cached images. To delete these, use `docker container prune` , then go back to step (3)

### Other notes

For production, we need to generate a `.env` file and use the `docker-compose-prod.yml` file. This can be done with:

```bash
docker-compose -f docker-compose-prod.yml up --build -d
```



One of the tutorials also notes: "If all works well, you should be able to create an admin account with `docker-compose run backend python manage.py createsuperuser`". I am not too sure what this does, but it might be helpful somewhere
