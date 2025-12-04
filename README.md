# Data_Gathering_SIS2

**Website description**
  IMDB - is the world's largest movie database. They have films, shows, news, events and many other pieces of media.


**How to run scrapper**
  1. To run scraping we used playwright to open the browser and access the website
  2. After waiting for the entire page to load (it is dynamic) we start gathering movie list
  3. We extract links from every title and transform them into url
  4. By moving from movie to movie we scrap info based on html markup
  5. After which all movies get put into a single list and added to a JSON




**How to run airflow**

  **Navigate to windows features and enable "Windows subsystems for linux"**
  
  **Download UBUNTU** https://apps.microsoft.com/detail/9nblggh4msv6?hl=ru-RU&gl=RU
  
  **Install ubuntu and create an account**
  
  **run the following commands to install python**
  sudo apt-get install software-properties-common
  sudo apt-add-repository universe
  sudo apt-get update
  sudo apt-get install python-pip
  
  **install dependencies**
  sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
  pip install werkzeug==0.15.4
  
  **install virtual environment for python**
  apt install python3.8-venv
  
  **create a venv**
  python3 -m venv airflow_venv
  
  **enter the venv**
  source airflow_venv/bin/activate
  
  **install wheel because not all dependencies have been installed**
  pip install wheel
  pip install google-re2
  
  **then install apache**
  pip install apache-airflow
  
  **change directory for airflow**
  export AIRFLOW_HOME=~/airflow
  
  **initialize database**
  airflow initdb
  
  **start the webserver**
  airflow webserver -p 8080
  
  **start scheduler**
  airflow scheduler
  
  **visit localhost:8080 in the browser and enable the dag **



**Expected output**
 
  From scrapper
  {"imdb_id": "tt0111161", "title": "The Shawshank Redemption", "rating": "IMDb RATING9.3", "year": "1994"}
  
  From cleaner
  {"id": 111161, "title": "The Shawshank Redemption", "rating": 93.0, "year": 1994}
  
  From loader
  '111161', 'The Shawshank Redemption', 1994, 93







I dont know if i can actually install it, because airflow crashed my pc 2 times already, i'll be honest i have no idea why
I have finally done it, i havent slept all night but i finally launched that airflow
