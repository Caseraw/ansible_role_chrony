# 1. Chrony

Managing network time using **chrony**.

<!-- TOC -->

- [1. Chrony](#1-chrony)
  - [1.1. Requirements](#11-requirements)
  - [1.2. Role Variables](#12-role-variables)
  - [1.3. Dependencies](#13-dependencies)
  - [1.4. Example Playbook](#14-example-playbook)
  - [1.5. Additional sources](#15-additional-sources)
  - [1.6. Usefull shell commands](#16-usefull-shell-commands)
  - [1.7. License](#17-license)
  - [1.8. Author Information](#18-author-information)

<!-- /TOC -->

## 1.1. Requirements

- Ensure a package manager is available and configured with the correct package sources and repositories.
- Ensure privileged permissions are set for the user executing this role to:
  - Install and uninstall.
  - Edit files provided by the package itself.
  - Manage systemd services for `ntpd` and `chronyd`.
- Ensure network traffic over 123/udp (port/protocol) is allowed.
  - Outbound for any servers providing NTP.
  - Inbound for any clients retrieving NTP.

## 1.2. Role Variables

| Variable name | Description |
|---------------|-------------|
| role_chrony_chrony_dot_conf_parameters | A dictionary containing the native configuration of chrony. |
| role_chrony_required_packages | A list of packages that need to be installed for chrony to work properly. |
| role_chrony_time_zone | The timezone to set. |

## 1.3. Dependencies

N/A

## 1.4. Example Playbook

```yaml
---
- name: Manage the installation and configuration of chrony for NTP
  become: True
  gather_facts: False
  roles:
   - role: chrony

...
```

## 1.5. Additional sources

The following links provide more information about **chrony** and it's usage.

- <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-configuring_ntp_using_the_chrony_suite>
- <https://chrony.tuxfamily.org/faq.html>

## 1.6. Usefull shell commands

```shell
chronyc tracking
chronyc sources
chronyc sourcestats
```

## 1.7. License

MIT / BSD

## 1.8. Author Information

Made and maintained by: [Kasra Amirsarvari](https://www.linkedin.com/in/caseraw)
