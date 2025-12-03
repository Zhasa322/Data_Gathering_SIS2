# Data_Gathering_SIS2

I dont know if i can actually install it, because airflow crashed my pc 2 times already, i'll be honest i have no idea why

Navigate to windows features and enable "Windows subsystems for linux"

Download UBUNTU https://apps.microsoft.com/detail/9nblggh4msv6?hl=ru-RU&gl=RU

To run airflow you first have to intsall UV, run this in your powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Then create a virtual environment
