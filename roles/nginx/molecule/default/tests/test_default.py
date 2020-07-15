def test_ssl_certs_dir(host):
    file_handler = host.file("/etc/nginx/ssl-certs")
    assert file_handler.exists
    assert file_handler.is_directory
    assert file_handler.mode == 0o755


def test_cert_and_key_files_exists(host):
    cert_file = host.file("/etc/nginx/ssl-certs/example.cert")
    key_file = host.file("/etc/nginx/ssl-certs/example.key")
    assert cert_file.exists
    assert cert_file.is_file
    assert key_file.exists
    assert key_file.is_file


def test_nginx_is_installed(host):
    pkg = host.package("nginx")
    assert pkg.is_installed


def test_nginx_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_enabled
