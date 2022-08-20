
IPADDR=18.118.186.235 #TEST
#IPADDR=3.141.65.150 #PROD
LOCAL_PROJECT_PATH=~/dev/nobgyn

#New server setup
ssh bitnami@${IPADDR} "sudo mkdir -p /opt/bitnami/projects/northlandobgyn/"
ssh bitnami@${IPADDR} "sudo chown -R bitnami /opt/bitnami/projects/"

#startupconfig
scp $LOCAL_PROJECT_PATH/startup.sh bitnami@${IPADDR}:~
ssh bitnami@${IPADDR} "sudo chmod +x ~/startup.sh"

#apache config
scp $LOCAL_PROJECT_PATH/*.conf_ bitnami@${IPADDR}:/opt/bitnami/apache2/conf/vhosts/
ssh bitnami@${IPADDR} "mv /opt/bitnami/apache2/conf/vhosts/nobgyn-vhost-ssl.conf_ /opt/bitnami/apache2/conf/vhosts/nobgyn-vhost-ssl.conf"
ssh bitnami@${IPADDR} "mv /opt/bitnami/apache2/conf/vhosts/nobgyn-vhost.conf_ /opt/bitnami/apache2/conf/vhosts/nobgyn-vhost.conf"


PASS=$(ssh bitnami@${IPADDR} "cat ~/bitnami_application_password")
DJANGO_PROD="%2t!z5vw11(t@fxbln&zvmfvv*pptk*p2mv5^*va&%k9n&we8"
#add django config to aws lightspeed profile
ssh bitnami@${IPADDR} "test -e ~/.profile_ORIG"
if [ $? -eq 1 ]; then
  # file does not exist
  ssh bitnami@${IPADDR} "cp ~/.profile ~/.profile_ORIG"
  ssh bitnami@${IPADDR} "echo 'export DJANGO_PROD=\"$DJANGO_PROD\"' >> ~/.profile"
  ssh bitnami@${IPADDR} "echo -n 'export MYSQL_PASSWORD=\"' >> ~/.profile"
  ssh bitnami@${IPADDR} "echo -n $PASS >> ~/.profile"
  ssh bitnami@${IPADDR} "echo '\"' >> ~/.profile"
  echo ".profile updated"
fi

#add django config to aws lightspeed profile
ssh bitnami@${IPADDR} "test -e ~/.bashrc_ORIG"
if [ $? -eq 1 ]; then
  # file does not exist
  ssh bitnami@${IPADDR} "cp ~/.bashrc ~/.bashrc_ORIG"
  ssh bitnami@${IPADDR} "echo 'export DJANGO_PROD=\"$DJANGO_PROD\"' >> ~/.bashrc"
  ssh bitnami@${IPADDR} "echo -n 'export MYSQL_PASSWORD=\"' >> ~/.bashrc"
  ssh bitnami@${IPADDR} "echo -n $PASS >> ~/.bashrc"
  ssh bitnami@${IPADDR} "echo '\"' >> ~/.bashrc"
  echo ".bashrc updated"
fi

#mysql setup
# mysql login -u root -p ###
# CREATE DATABASE nobgyn;
# CREATE USER 'NOBGYN'@'localhost' IDENTIFIED BY 'password';
# GRANT ALL ON nobgyn.* TO 'NOBGYN'@'localhost';
# FLUSH PRIVILEGES;
PASS=na
