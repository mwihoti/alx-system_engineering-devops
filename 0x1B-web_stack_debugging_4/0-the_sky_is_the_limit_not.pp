# fix failed request in server

exec { 'set_ulimit_to 3000':
  command => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 3000\"/" /etc/default/nginx'

} -> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
