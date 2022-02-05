# Mentoring-Site

The implementation of group 17's software engineering project for the Warwick CS261 course.

## Setup

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>

For frontend people, it is probably sufficient to just run the Vue.js cli on your machine and spoof the JSON api - then we can handle integration later :grimacing: .

A template for setting up a docker container of the correct tech stack was used. This was published under the BSD-3 License by Daniel Greenfeld, and can be found [here](https://github.com/vchaptsev/cookiecutter-django-vue). To get docker running on your machine, perform the following steps (derived on top of the template):

1. Ensure you have Docker installed.
   - Windows users should install [WSL2](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10) (I recommend using the Ubuntu distro), then install [docker desktop](https://www.docker.com/products/docker-desktop), and set it up [as shown](https://imgur.com/a/xcgPMLA)
   - Linux (and Mac?) users can either install [docker desktop](https://www.docker.com/products/docker-desktop), or install it [directly to their machine](https://docs.docker.com/engine/install/)

2. Run the cookie cutter to create the docker container with the correct stack.

   - First, install it with:

     ```bash
     pip install cookiecutter
     ```

   - Then, run it with:

     ```bash
     cookiecutter gh:vchaptsev/cookiecutter-django-vue
     ```

   - Enter the following values on the setup screen:

     - project_name: mentorprise
     - project_slug:
     - ...
     - api: REST (1)
     - backups: n
     - use_sentry: n
     - use_mailhog: n
     - analytics: None (3)

3. To start up the system, run the command:

    ```bash
    docker-compose up --build
    ```

   This will take some time when first run (many node modules to install), but should take tens of seconds every time after.

4. Whilst the docker containers are running, the site can be accessed by the URL (http *not* https): [http://localhost:8000](http://localhost:8000)

5. To kill the containers, interrupt with `Ctrl+c`, and run (optionally?) run `docker compose down` after.

6. Sometimes, problems come from cached images. To delete these, use `docker container prune` - and see if that fixes your problems

7. For production, we need to generate a `.env` file and use the `docker-compose-prod.yml` file. This can be done with:

   ```bash
   docker-compose -f docker-compose-prod.yml up --build -d
   ```



(If all works well, you should be able to create an admin account with `docker-compose run backend python manage.py createsuperuser` (not sure if this does anything?) )

## License

This project is published under the MIT license by Group 17 ("Mentorprise") of the 2022 Warwick CS261 module. The team members include: Ben Lewis, Dan Risk, Edmund Goodman, Jay Re Ng, John-Loong Gao, Rahul Vanmali, and Tomás Chapmann Fromm.
