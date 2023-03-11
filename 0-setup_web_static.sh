#!/usr/bin/bash
#setup web static

apt update
apt install nginx
ufw allow 'Nginx HTTP'
sudo service nginx start

mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 
chown ubuntu /data/
chgrp ubuntu /data/

echo "
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;


	location / {
		try_files \$uri \$uri/ =404;
		 }
	if (\$request_filename ~ redirect_me) {
		return 301 https://www.istockphoto.com/photos/horror\$request_uri;
	}
	error_page 400 404 /error404.html;
	location = /error404.html{
		internal;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}" > /etc/nginx/sites-available/default
service nginx restart
