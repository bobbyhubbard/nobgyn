
IPADDR=3.22.239.246 #TEST static IP
#IPADDR=3.141.65.150 #PROD static IP

PROJECT_PATH=~/dev/nobgyn

#ssh bitnami@${IPADDR} "sudo mkdir -p /opt/bitnami/projects/northlandobgyn/"
#ssh bitnami@${IPADDR} "sudo chown -R bitnami /opt/bitnami/projects/"
#scp -r $PROJECT_PATH/manage.py $PROJECT_PATH/faqs $PROJECT_PATH/locations $PROJECT_PATH/header $PROJECT_PATH/footer $PROJECT_PATH/manage.py $PROJECT_PATH/northlandobgyn $PROJECT_PATH/providers $PROJECT_PATH/resources $PROJECT_PATH/services bitnami@${IPADDR}:/opt/bitnami/projects/northlandobgyn/

#settings only
#scp $PROJECT_PATH/northlandobgyn/settings.py bitnami@${IPADDR}:/opt/bitnami/projects/northlandobgyn/northlandobgyn/settings.py

#html only
scp -r $PROJECT_PATH/services bitnami@${IPADDR}:/opt/bitnami/projects/northlandobgyn/

#scp $PROJECT_PATH_static/ bitnami@${IPADDR}:/opt/bitnami/projects/
