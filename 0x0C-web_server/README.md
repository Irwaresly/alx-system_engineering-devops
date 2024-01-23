# Web Server Configuration Project

## Overview

This project focuses on configuring a web server using various tools and techniques. Below are the tasks accomplished in this project:

1. **Transfer a File to Your Server:**
   - Implemented a Bash script (`0-transfer_file`) to transfer a file from the client to a server using `scp`.
   - Accepted parameters for the file path, server IP, username, and SSH private key.
   - Provided usage instructions if insufficient parameters are passed.

2. **Install Nginx Web Server:**
   - Created a Bash script (`1-install_nginx_web_server`) to install and configure Nginx on the server.
   - Ensured Nginx is listening on port 80.
   - Verified proper installation by checking if a GET request to the root returns "Hello World!"

3. **Setup a Domain Name:**
   - Obtained a free .tech domain from .TECH Domains.
   - Configured DNS records with an A entry to point the root domain to the web server's IP address.
   - Entered the domain in the Project website URL field and verified DNS propagation.

4. **Redirection:**
   - Configured Nginx to perform a permanent redirect (301) from /redirect_me to another page.
   - Created a Bash script (`3-redirection`) for automated configuration on a new Ubuntu machine.

5. **Not Found Page 404:**
   - Configured Nginx to have a custom 404 page containing the string "Ceci n'est pas une page."
   - Created a Bash script (`4-not_found_page_404`) for automated configuration on a new Ubuntu machine.

6. **Install Nginx Web Server (w/ Puppet):**
   - Used Puppet to install and configure Nginx on the server.
   - Ensured Nginx is listening on port 80 and returns "Hello World!" on a GET request to the root.
   - Implemented a 301 redirect when querying /redirect_me.

## Usage

### 0. Transfer a File to Your Server

```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

Example:

```bash
./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
```

### 1. Install Nginx Web Server

```bash
./1-install_nginx_web_server
```

Verify:

```bash
curl localhost
```

### 2. Setup a Domain Name

Provide the obtained domain name (e.g., `myschool.tech`).

### 3. Redirection

```bash
./3-redirection
```

Verify:

```bash
curl -sI SERVER_IP/redirect_me/
```

### 4. Not Found Page 404

```bash
./4-not_found_page_404
```

Verify:

```bash
curl -sI SERVER_IP/xyz
curl SERVER_IP/xyzfoo
```

### 5. Install Nginx Web Server (w/ Puppet)

```bash
sudo puppet apply 7-puppet_install_nginx_web_server.pp
```

Verify:

```bash
curl localhost
curl -sI SERVER_IP/redirect_me/
```

## Additional Notes

- DNS propagation may take some time (~1-2 hours). Verify using `dig` or online tools.
- Check Nginx logs in `/var/log/` if any issues arise during configuration.
- Ensure proper permissions and execution rights for Bash scripts.

## Author

Your Name

## Acknowledgments

Special thanks to .TECH Domains for providing a free domain for this project.
