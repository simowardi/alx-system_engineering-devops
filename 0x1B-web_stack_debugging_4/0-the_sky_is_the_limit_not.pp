# Increases the amount of traffic an Nginx server can handle.

# Fix PHP configuration if needed
exec { 'replacing_right path':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}

# Increase ULIMIT of the default file for Nginx
exec { 'increase_ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx to apply changes
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  subscribe => Exec['increase_ulimit', 'modify_nginx_config'],
  refreshonly => true,
}
