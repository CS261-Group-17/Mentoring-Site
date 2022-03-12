# Installing the system


## 1. Development environment

In order to facilitate further development and maintanence of the product, we
provide instructions on how to run a development environment for the system,
with additional features including all the required tooling for testing, which
are not retained in the production environment.

This environment is split up into two sections, the backend and the frontend,
which can be developed individually to parallelise the development workflow.

### Backend development environment

The backend source code is stored at `mentorprise/backend_dev`. To run the this environment, follow these steps:

1. First, we create a virtual environment with all the required dependencies installed:
    2. `python3 -m venv env`
    3. `env/bin/pip install -r requirements.txt`

2. Then, we can enter the virtual environment: `source env/bin/activate`

3. You will also need to set up postgresql on your system. If you are running Ubuntu, follow this tutorial [https://help.ubuntu.com/community/PostgreSQL](https://help.ubuntu.com/community/PostgreSQL), otherwise find a relevant one for your distro:
    1. `sudo apt-get install postgresql postgresql-contrib`
    2. `sudo -u postgres createuser --superuser mentorprise`
    3. `sudo -u postgres psql`
        1. postgres=# `ALTER USER mentorprise WITH PASSWORD '12345';` - for development purposes only, in production a securely generated password should be used
        2. postgres=# `CREATE DATABASE mentorprise;`

4. Next, we need to build and run the Django backend using the management file stored at `mentorprise/backend_dev/mentorprise` as follows:
    1. `python3 manage.py makemigrations app`
    2. `python3 manage.py migrate`
    3. `python3 manage.py runserver`

5. Finally, the test suite can be run as follows:
    1. `python3 manage.py test`

### Frontend development environment

The frontend source code is stored at `mentorprise/frontend_dev`. To run the this environment, follow these steps:

1. First, we install all the required node modules with `npm install`
1. Then, we run the development server with `npm run serve`

### Running the development environment

The whole system (both backend and frontend) can be tested together as follows:

1. In one terminal, run the backend environment with `python3 manage.py runserver`
2. In another termincal, run the frontend environment with npm `run serve`

Then, navigating to `http://localhost:8000` will yield the development site



## 2. Production environment

The production release is stored at at `mentorprise/docker`. To run the this environment, follow these steps:

1. Install [Docker](https://www.docker.com/)
2. Run the command `docker-compose -f docker-compose-dev.yml up --build`

This will run a production server, which can be accessed using via the url reported by the docker command.
