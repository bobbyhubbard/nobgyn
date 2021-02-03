
#IPADDR=3.22.239.246 #TEST
IPADDR=3.141.65.150 #PROD

scp -ri /Users/hubbardr/.ssh/LightsailDefaultKey-us-east-2.pem ~/dev/django_projects/northlandobgyn/manage.py ~/dev/django_projects/northlandobgyn/faqs ~/dev/django_projects/northlandobgyn/locations ~/dev/django_projects/northlandobgyn/header ~/dev/django_projects/northlandobgyn/footer ~/dev/django_projects/northlandobgyn/manage.py ~/dev/django_projects/northlandobgyn/northlandobgyn ~/dev/django_projects/northlandobgyn/providers ~/dev/django_projects/northlandobgyn/resources ~/dev/django_projects/northlandobgyn/services bitnami@${IPADDR}:/opt/bitnami/projects/northlandobgyn/

#html only
#scp -ri /Users/hubbardr/.ssh/LightsailDefaultKey-us-east-2.pem ~/dev/django_projects/northlandobgyn/northlandobgyn/templates/ bitnami@${IPADDR}:/opt/bitnami/projects/northlandobgyn/northlandobgyn/templates/

#scp -ri /Users/hubbardr/.ssh/LightsailDefaultKey-us-east-2.pem ~/dev/django_projects/northlandobgyn_static/ bitnami@${IPADDR}:/opt/bitnami/projects/

#scp -ri /Users/hubbardr/.ssh/LightsailDefaultKey-us-east-2.pem ~/dev/django_projects/northlandobgyn/startup.sh bitnami@${IPADDR}:~

#scp -ri /Users/hubbardr/.ssh/LightsailDefaultKey-us-east-2.pem ~/dev/django_projects/northlandobgyn/*.conf_ bitnami@${IPADDR}:/opt/bitnami/apache2/conf/vhosts/
