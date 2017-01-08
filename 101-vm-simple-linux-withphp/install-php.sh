sudo apt-get -y update
sudo apt-get -y install apache2
sudo apache2ctl configtest
apt-get install -y php
sudo apt install php libapache2-mod-php
apt-get install -y curl php-cli git
apt-get install -y wget

curl -sS https://getcomposer.org/installer | php

cd /var/www/html
wget https://raw.githubusercontent.com/irwinwilliams/azure-quickstart-templates/101-vm-simple-linux-withphp/master/index.php
rm /var/www/html/index.html

apachectl restart
