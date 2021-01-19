stopServices='false'
startServices='false'
resetLogs='false'
help='false'
install='false'

while getopts ':strih' 'OPTKEY'
do
  case ${OPTKEY} in
    't') stopServices='true';;
    's') startServices='true';;
    'r') resetLogs='true';;
    'h') help='true';;
    'i') install='true';;
    '?') echo "?" ;;
    ':') echo ":";;
    *)  echo "*";;
  esac
done

cd /opt/bitnami/projects/northlandobgyn

if $install; then
  echo "Install required components"
  sudo pip install django-import-export
fi

if $help; then
  echo "Usage: ./startup.sh
          -s [start services]
          -t [terminate/stop running services]
          -r [clear previous logs]
          -i [install required components]
          -h [help]

          "
fi

if $stopServices; then
  echo "Stopping services"
  pkill python
  sudo /opt/bitnami/ctlscript.sh stop apache

  wait

  if $resetLogs; then
    echo "Clearing logs"
    sudo rm -f /opt/bitnami/apache2/logs/error_log
    sudo rm -f /opt/bitnami/apache2/logs/access_log
  fi
fi

if $startServices; then
  HOSTNAME=$(hostname -I | awk '{print $1}')
  echo "Starting services"
  export DJANGO_PROD="%2t!z5vw11(t@fxbln&zvmfvv*pptk*p2mv5^*va&%k9n&we8g"; python3 manage.py runserver $HOSTNAME:8000 &
  sudo /opt/bitnami/ctlscript.sh restart apache
fi
