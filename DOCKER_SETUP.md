# Setting up Docker

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>

Setting up containerised stuff is painful - I have Googled it and this is what you need to do.

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

     - project_name - `mentorprise`
     - project_slug - `mentorprise`
     - domain - `domain.invalid`
     - description - `The implementation of group 17's software engineering project for the Warwick CS261 course`
     - author - `CS261 2022 Group 17`
     - email - `null@domain.invalid`
     - api - `1` (REST)
     - backups - `n`
     - use_sentry - `n`
     - use_mailhog - `n`
     - analytics - `3` (None)

3. This will make a folder called `mentorprise`, which is where we will do all the development. We can then run the following script to clean up after the installation:

   ```
   mv mentorprise
   rm .gitignore
   autopep8 -r --in-place --aggressive --aggressive backend
   cd frontend && npm i && npm run lint --fix
   ```

4. Some of the python dependencies will be broken, so you will need to change the `mentorprise/backend/requirements.txt` file as follows:

   1. Line 6 - `decorator==5.1.1` (was 4.0.7)
   2. Line 17 - `idna==2.10` (was 3.1)
   
5. To start up the system, run the command (you may need to disable particularly aggressive firewalls):

   ```bash
   docker-compose up --build
   ```

   This will take some time when first run (many node modules to install), but should take tens of seconds every time after.

6. Whilst the docker containers are running, the site can be accessed by the URL (http *not* https): [http://localhost:8000](http://localhost:8000)

7. To kill the containers, interrupt with `Ctrl+c`, and run (optionally?) run `docker compose down` after.

8. Sometimes, problems come from cached images. To delete these, use `docker container prune` - and see if that fixes your problems

9. For production, we need to generate a `.env` file and use the `docker-compose-prod.yml` file. This can be done with:

   ```bash
   docker-compose -f docker-compose-prod.yml up --build -d
   ```



(One of the tutorials also notes: "If all works well, you should be able to create an admin account with `docker-compose run backend python manage.py createsuperuser`". I am not too sure what this does, but it might be helpful somewhere)
