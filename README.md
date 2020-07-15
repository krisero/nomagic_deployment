## Before You Begin
Before you begin we recommend you read about the basic building blocks that assemble this solution:
* Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. Start by going through [Ansible docs](https://docs.ansible.com/ansible/latest/index.html).
* Molecule project is designed to aid in the development and testing of Ansible roles. Go through [Molecule docs](https://molecule.readthedocs.io/en/latest/).
* Docker helps developers bring their ideas to life by conquering the complexity of app development. Study [Docker docs](https://docs.docker.com/).
* Vagrant enables users to create and configure lightweight, reproducible, and portable development environments. Learn here [Vagrant docs](https://www.vagrantup.com/docs).
* VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. Read [VirtualBox docs](https://www.virtualbox.org/wiki/Documentation).
* NGINX accelerates content and application delivery, improves security, facilitates availability and scalability for the busiest web sites on the Internet. Start here [Nginx docs](https://docs.nginx.com/).


## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
* Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
* Docker - [Download & Install Docker](https://docs.docker.com/get-docker/)
* Vagrant - [Download & Install Vagrant](https://www.vagrantup.com/downloads.html)
* VirtualBox - [Download & Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Molecule - [Download & Install Molecule](https://molecule.readthedocs.io/en/latest/installation.html)
* Ansible - [Download & Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html)




### Cloning The GitHub Repository

```bash
$ git clone https://github.com/krisero/nomagic_deployment.git nomagic_deployment
```

This will clone the latest version of the nomagic_deployment repository to a **nomagic_deployment** folder.


## Running it locally:
#### Local vagrant environment:

```bash
$ cd local_env; vagrant up
```

#### Setup environment before deployment:

```bash
$ ansible-playbook -i hosts setup.yml --ask-vault-pass
```

#### Deploy website:

```bash
$ ansible-playbook -i hosts deployment.yml --ask-vault-pass
```

#### Try it:

```bash
$ curl -k https://nomagic.local:58443
``` 
or simply go to browser  [https://nomagic.local:58443](https://nomagic.local:58443)




## Tests:

1. For each role in directory ```nomagic_deployment/roles/<ROLE_NAME>/molecule/default/``` create ```vault.pw``` with raw password 

2. For each role run in role directory 
```bash
$ molecule test
```

