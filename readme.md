<div id="top"></div>
<br />
<div align="">
  <h1 align="">FHIR server</h1>
  <p align="">
    

  </p>
</div>
 <br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#vscode">VScode extensions</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

 <br />
 
## About The Project
This is a FHIR server built with python Django and works with hapi-FHIR API for now.
The Database is Postgresql
<p align="right">(<a href="#top">back to top</a>)</p>

## Built With

* [Python](https://www.python.org/)
* [Anaconda](https://www.anaconda.com/)
* [Django](https://docs.djangoproject.com)
* [PostgreSQL](https://www.postgresql.org/)
* [Ubuntu WSL](https://ubuntu.com/wsl)

<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

1. Clone the repo to your local system.
2. This project is built with python 3.8. Obtain a copy of python 3X from python.org or     anaconda and install it in your local system
3. Obtain a copy of .env from project owner and place in the root folder of the project.
4. Obtain a copy of postman export

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

1. Install Python 3x from the above listed sources
2. Install redis from above listed source.(If you are using windows, use Ubuntu WSL and install redis inside WSL)
    
3. Install Postgres and use pgadmin to connect to the database
5. Navigate to the project folder FHIR using terminal/commandprompt
6. In terminal type the below command, This will create a virtual environment
      ```sh
      pipenv shell
      ```
7. install dependencies from pipfile
    ```sh
    pipenv install
    ```
    this will install all the dependencies from the pipfile. 
8. navigate to app folder
    ```sh
    cd fhir_app
    ```
9. apply migrations. 
    ```sh
    python manage.py migrate
    ```
10. Run the Django application.
    ```sh
    python manage.py runserver
    ```

## VScode
if you are using vscode, please install the below extensions.

* [Gitlens](https://gitlens.amod.io/)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact
NA
<p align="right">(<a href="#top">back to top</a>)</p>
