#!/usr/bin/env bash
# Sets up the web server for the deployment of the web_static

sudo apt-get update
sudo apt install -y nginx
# mkdir -p /data/
# mkdir -p /data/web_static/
# mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
echo "<html>
        <head>
	</head>
	<body>
	  Holberton School
        </body>
 </html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \        location \/hbnb_static {\n\     alias \/data\/web_static\/current\/;\n\ index index.html;\n\    }' /etc/nginx/sites-enabled/default
sudo nginx -t
sudo service nginx start
