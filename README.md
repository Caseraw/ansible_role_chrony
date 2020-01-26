# 1. Chrony

Managing network time with **Ansible** using **chrony**.

[![Build Status](https://travis-ci.org/Caseraw/ansible_role_chrony.svg?branch=master)](https://travis-ci.org/Caseraw/ansible_role_chrony) [<img src="https://img.shields.io/ansible/role/44669">](https://galaxy.ansible.com/caseraw/ansible_role_chrony) [<img src="https://img.shields.io/ansible/role/d/44669">](https://galaxy.ansible.com/caseraw/ansible_role_chrony) [<img src="https://img.shields.io/ansible/quality/44669">](https://galaxy.ansible.com/caseraw/ansible_role_chrony)

<!-- TOC -->

- [1. Chrony](#1-chrony)
  - [1.1. License](#11-license)
  - [1.2. Author Information](#12-author-information)
  - [1.3. Requirements](#13-requirements)
  - [1.4. Dependencies](#14-dependencies)
  - [1.5. Compatibility](#15-compatibility)
  - [1.6. Role Variables](#16-role-variables)
  - [1.7. Example Playbook](#17-example-playbook)
  - [1.8. Useful shell commands](#18-useful-shell-commands)
  - [1.9. Additional chrony documentation resources](#19-additional-chrony-documentation-resources)
  - [1.10. Testing with Molecule](#110-testing-with-molecule)
  - [1.11. CI/CD with Travis CI](#111-cicd-with-travis-ci)
  - [1.12. Useful links](#112-useful-links)

<!-- /TOC -->

## 1.1. License

MIT / BSD

## 1.2. Author Information

- Made and maintained by: [Kasra Amirsarvari](https://www.linkedin.com/in/caseraw)
- Ansible Galaxy community author: <https://galaxy.ansible.com/caseraw>
- Dockerhub community user: <https://hub.docker.com/u/caseraw>

## 1.3. Requirements

- Ensure a package manager is available and configured with the correct package sources and repositories.
- Ensure privileged permissions are set for the user executing this role to:
  - Install and uninstall.
  - Edit files provided by the package itself.
  - Manage `systemd` services for `ntpd` and `chronyd`.
- Ensure network traffic over 123/udp (port/protocol) is allowed.
  - Outbound for any servers providing NTP.
  - Inbound for any clients retrieving NTP.

## 1.4. Dependencies

N/A

## 1.5. Compatibility

Compatible with the following list of operating systems:

- CentOS 7
- CentOS 8
- RHEL 7.x
- RHEL 8.x

## 1.6. Role Variables

| Variable name | Description |
|---------------|-------------|
| role_chrony_chrony_dot_conf_parameters | A dictionary containing the chrony configuration. |
| role_chrony_required_packages | A list of packages that need to be installed for chrony to work properly. |
| role_chrony_time_zone | The timezone to set. |

## 1.7. Example Playbook

```yaml
---
- name: Manage the installation and configuration of chrony for NTP
  become: True
  gather_facts: False
  roles:
   - role: chrony

...
```

## 1.8. Useful shell commands

```shell
chronyc tracking
chronyc sources
chronyc sourcestats
```

## 1.9. Additional chrony documentation resources

The following links provide more information about **chrony** and it's usage.

- <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-configuring_ntp_using_the_chrony_suite>
- <https://chrony.tuxfamily.org/faq.html>

## 1.10. Testing with Molecule

This role is locally tested with the use of [Molecule](https://molecule.readthedocs.io/en/stable/), the configuration is located at: [molecule/default](molecule/default).  
The Molecule tests are run (using the [docker driver](https://molecule.readthedocs.io/en/stable/configuration.html#docker)) on [Dockerhub images](https://hub.docker.com/u/caseraw) built for this purpose:

- [CentOS](https://hub.docker.com/r/caseraw/ansible-molecule-centos)
- [Fedora](https://hub.docker.com/r/caseraw/ansible-molecule-fedora)

Some specific configurations might require a full OS instead of a minimal container image. In these use-cases make use of [molecule driver for vagrant](https://molecule.readthedocs.io/en/stable/configuration.html#vagrant) with the [libvirt provider](https://molecule.readthedocs.io/en/stable/configuration.html#molecule-vagrant-module). The Molecule driver and platform configuration part could look something like this:

```yaml
driver:
  name: vagrant
  provider:
    name: libvirt
platforms:
  - name: ansible_role_chrony-ansible-molecule-centos-7
    box: centos/7
    imemory: 1024
    cpus: 1
```

## 1.11. CI/CD with Travis CI

This role uses [Travis CI](https://travis-ci.org/) to run online tests with the use of [Molecule](https://molecule.readthedocs.io/en/stable/) and pushes notifications to import the role into [Ansible Galaxy](https://galaxy.ansible.com/) once the tests are successful. The Travis CI configuration is located at the root of the Ansible role [.travis.yml](.travis.yml)

## 1.12. Useful links

- GitHub repository: <https://github.com/Caseraw/ansible_role_chrony>
- Travis CI build status: <https://travis-ci.org/Caseraw/ansible_role_chrony>
- Ansible Galaxy role: <https://galaxy.ansible.com/caseraw/ansible_role_chrony>
