#!/usr/bin/env bash
# Sets up the web server for the deployment of the web_static

sudo apt-get update
sudo apt install -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h1> Testing nginx configurations </h1>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
domain="wahujos.tech"
nginx_config="/etc/nginx/sites-available/default"
temp_config="/tmp/nginx_temp_config"
echo "server {
	listen 80;
	server_name $domain;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}" > "$temp_config"
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default_backup
sudo mv "$temp_config" "$nginx_config"
sudo nginx -t
sudo service nginx start
