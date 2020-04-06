# ncov-web-api

## Description
This is a web api service for retriving conovirus 2019 infection data. Those data are gain from this [repository](https://github.com/BlankerL/DXY-COVID-19-Data)

## Installation
In order to boostrap this api in dev enviornment you should clone the above repository to your local pc too. After that, Doing the following step. 
1. Create a folder named json_data under ncov-web-api folder. 
2. copy following files from DXY-COVID-19-DATA repository to json_data folder.
   1. DXYArea-TimeSeries.json -> DXYArea-TimeSeries.json
   2. DXYArea.json -> DXYArea.json
   3. DXYOverall-TimeSeries.json -> DXYOverall-TimeSeries.json
   4. DXYOverall.json -> DXYOverall.json
3. Setup the python enviornment
   1. install python 
   2. install flask and flask_cors 
   3. then got to cmd and enter flask run 

## Deployment
   If you want to put this api to your cloud server. You can follow below instructions step by step. The target machine is a linux ubuntu. 
   1. Install Python Nginx on your cloud server. Enter these command in cmd
      1. sudo apt-get update 
      2. sudo apt-get install python-pip python-dev nginx
   2. python3 -m venv <your env>
   3. source <your env>/bin/active
   4. pip3 install flask
   5. pip3 install flask_cors
   6. pip3 install gunicorn
   7. Create a file enter the following instruction
      sudo vim /etc/systemd/system/app.service
   8. Paste the following content in app.service(you can refer my sample)
      [Unit]
      \#  specifies metadata and dependencies
      Description=Gunicorn instance to serve myproject
      After=network.target
      \# tells the init system to only start this after the networking target has been reached
      \# We will give our regular user account ownership of the process since it owns all of the relevant files
      [Service]
      \# Service specify the user and group under which our process will run.
      User=Isaac
      \# give group ownership to the www-data group so that Nginx can communicate easily with the Gunicorn processes.
      Group=www-data
      \# We'll then map out the working directory and set the PATH environmental variable so that the init system knows where our the executables for the process are located (within our virtual environment).
      WorkingDirectory=/home/Isaac/ncov-web-api
      Environment="PATH=/home/Isaac/ncov-web-api/venv/bin"
      \# We'll then specify the commanded to start the service
      ExecStart=/home/Isaac/ncov-web-api/venv/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app
      \# This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running:
      [Install]
      WantedBy=multi-user.target
   9. sudo systemctl start app
   10. sudo systemctl enable app
   11. you can see the app.sock file under the current directory now
   12. vim nano /etc/nginx/sites-available/app
   13. paste the following content(you can refer my sample )
      server {
         listen 80;
         server_name server_domain_or_IP;
      }
      location / {
         include proxy_params;
         proxy_pass http://unix:/home/Isaac/ncov-web-api/app.sock;
      }
   14. sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
   15. sudo systemctl restart nginx
   16. sudo ufw allow 'Nginx Full'
   17. done. 
       
      
      
   
