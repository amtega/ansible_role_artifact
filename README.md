# Amtega artifact role

This is an [Ansible](http://www.ansible.com) role to download several kinds or artifacts. Currently http/https, maven and gitlab/github artifacts are supported.

## Requirements

[Ansible 2.7+](http://docs.ansible.com/ansible/latest/intro_installation.html)

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

The role setups a fact named `artifact_result` with the following dict structure:

```yaml
artfiact_result:
  <artifact1_id>:
    download_path: <path to the downloaded artifact>
    changed: <true if artifact changed, false in other case>
  <artifact1_id>: ...
  <artifactN_id>: ...  
```

## Dependencies

- [amtega.check_platform](https://galaxy.ansible.com/amtega/check_platform)
- [amtega.packages](https://galaxy.ansible.com/amtega/packages) if you are using Gitlab/Github artifacts.
- [amtega.proxy_client](https://galaxy.ansible.com/amtega/proxy_client). If you need a proxy for internet access fill this role variables.
- - [amtega.select_hostvars](https://galaxy.ansible.com/amtega/select_hostvars)

## Example Playbook

This is an example playbook:

``` yaml
---
- name: artifact role sample
  hosts: localhost
  roles:  
    - amtega.artifact
  vars:
    artifact:
      id: artifact1
      type: github
      host: https://github.com
      project: ansible/ansible
      branch: master
      file: README.rst
      dest: /tmp
      validate_certs: false
```

## Testing

Tests are based on docker containers. You can setup docker engine quickly using the playbook `files/setup.yml` available in the role [amtega.docker_engine](https://galaxy.ansible.com/amtega/docker_engine).

Once you have docker, you can run the tests with the following commands:

```shell
$ cd amtega.artifact/tests
$ ansible-playbook main.yml
```

## License

Copyright (C) 2018 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
