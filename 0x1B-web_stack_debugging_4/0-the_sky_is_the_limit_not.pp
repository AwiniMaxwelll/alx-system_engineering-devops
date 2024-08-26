# Increases the amount of traffic on nginx server`.

# increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# restart nginx server
exec { 'restart-nginx-server':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}
