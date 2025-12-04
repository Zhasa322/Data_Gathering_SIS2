# Data_Gathering_SIS2

I dont know if i can actually install it, because airflow crashed my pc 2 times already, i'll be honest i have no idea why

Navigate to windows features and enable "Windows subsystems for linux"

Download UBUNTU https://apps.microsoft.com/detail/9nblggh4msv6?hl=ru-RU&gl=RU

Install ubuntu and create an account

run the following commands to install python
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip

install dependencies
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
pip install werkzeug==0.15.4

install virtual environment for python
apt install python3.8-venv

create a venv for apache
python3 -m venv airflow_venv
source airflow_venv/bin/activate

install wheel because not all dependencies have been installed
pip install wheel
pip install google-re2

then install apache
pip install apache-airflow



To run airflow you first have to intsall UV, run this in your powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Then create a virtual environment
