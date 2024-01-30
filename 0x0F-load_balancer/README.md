Certainly! Here's a simple README file for your load balancer project:

---

# Load Balancer Project

This repository contains scripts and configuration files for setting up a load balancer with Nginx and HAproxy on Ubuntu machines. The goal is to distribute incoming HTTP requests among multiple web servers and include a custom HTTP header in the response.

## Contents

1. [**Configure Custom HTTP Response Header**](0x0F-load_balancer/0-custom_http_response_header):
    - Bash script (`0-custom_http_response_header`) to configure Nginx on web-01 and web-02.
    - Adds a custom HTTP header (`X-Served-By`) to the HTTP response with the server's hostname.

    Example usage:
    ```bash
    $ curl -sI [web-01-IP] | grep X-Served-By
    X-Served-By: [STUDENT_ID]-web-01

    $ curl -sI [web-02-IP] | grep X-Served-By
    X-Served-By: [STUDENT_ID]-web-02
    ```

2. [**Install Load Balancer (HAproxy)**](0x0F-load_balancer/1-install_load_balancer):
    - Bash script (`1-install_load_balancer`) to install and configure HAproxy on lb-01.
    - Configures HAproxy to send traffic to web-01 and web-02 using a round-robin algorithm.

    Example usage:
    ```bash
    $ curl -Is [lb-01-IP]
    X-Served-By: [STUDENT_ID]-web-01

    $ curl -Is [lb-01-IP]
    X-Served-By: [STUDENT_ID]-web-02
    ```

3. [**Add Custom HTTP Header with Puppet**](0x0F-load_balancer/2-puppet_custom_http_response_header.pp) (Advanced):
    - Puppet manifest (`2-puppet_custom_http_response_header.pp`) to automate the configuration of a new Ubuntu machine.
    - Adds a custom HTTP header (`X-Served-By`) to the HTTP response with the server's hostname.

## How to Use

1. Clone the repository:
    ```bash
    $ git clone [repository-url]
    $ cd alx-system_engineering-devops/0x0F-load_balancer
    ```

2. Execute the scripts:
    - Follow the instructions provided in each subdirectory to run the scripts and configure the load balancer.

---


