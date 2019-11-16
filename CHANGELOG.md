CHANGELOG
=========

v0.1.0
------------
Creation of the Ansible chrony role.

Functionalities:
- Ensure to stop any active systemd ntpd service.
- Ensure required packages for **chrony** are installed using the yum module.
- Ensure the `chrony.conf` file is created from a template file and set in place using a variable (dictionary) to build it's configuration content.
- Ensure the given timezone is set.

Todo's (possibly):
- Ensure the management of the SELinux context for all configuration files.
- Ensure to manage the chrony key's file for added security.
- Ensure to manage the chrony log file.
