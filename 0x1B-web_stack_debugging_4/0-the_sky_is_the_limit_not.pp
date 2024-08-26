# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress-errors':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
  path    => '/usr/local/bin:/bin/
}
