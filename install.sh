read -p "This will erase evreything in the HTML and cgi-bin folder are you sure to procede: " input
if [ $input == 'yes' ]
then
   a2enmod cgid
   cp -r cgi-bin/* /usr/lib/cgi-bin/
   cp -r html/* /var/www/html/
   chmod 775 /var/www/html/
   chmod 775 /usr/lib/cgi-bin/
   chmod 777 /usr/lib/cgi-bin/chat.txt
fi
