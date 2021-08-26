#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
rm -rf /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    <h1>Hello</h1>
  </body>
</html>
" >> /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
rm -rf /etc/nginx/sites-available/default
echo "
server {
	listen 80 default_server;
    listen [::]:80 default_server;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
" >> /etc/nginx/sites-available/default
sudo service nginx restart
