# Chronyd

Managing network time using **chrony**.

## Requirements

- Ensure a package manager is available and configured with the correct package sources and repositories.
- Ensure privileged permissions are set for the user executing this role to:
  - Install and uninstall.
  - Edit files provided by the package itself.
- Ensure network traffic over 123/udp (port/protocol) is allowed.
  - Outbound for any servers providing NTP.
  - Inbound for any clients retrieving NTP.

## Role Variables

| Variable name | Default value | Type | Options/Contents | Description |
|---------------|------------------------|------|------------------|-------------|
| role_chrony_chrony_dot_conf_parameters| N/A | *Dictionary* | *Default chrony configuration options* | A dictionary containing the native configuration of chorny. |
| role_chrony_required_packages | N/A | *List* | *Package names* | A list of packages that need to be installed for chrony to work properly. |
| role_chrony_time_zone | Europe/Amsterdam | *String* | *All ISO standard timezones* | The timezone to set. |

## Dependencies

N/A

## Example Playbook

```yaml
---
- name: Manage the installation and configuration of chrony for NTP
  become: True
  gather_facts: False
  roles:
   - role: chrony

...
```

## License

MIT / BSD

## Author Information

Made and maintained by: Kasra Amirsarvari (https://www.linkedin.com/in/caseraw)

## Sources

- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-configuring_ntp_using_the_chrony_suite
- https://chrony.tuxfamily.org/faq.html

## Additional chrony documentation

**Chrony shell commands:**

```shell
chronyc tracking
chronyc sources
chronyc sourcestats
```
