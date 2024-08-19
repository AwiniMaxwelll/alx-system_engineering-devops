# A puppet script that correct an error in a server

$file_path = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
