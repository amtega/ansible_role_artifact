# Amtega artifact role

This is an [Ansible](http://www.ansible.com) role to download several kinds or artifacts. Currently http/https, maven and gitlab/github artifacts are supported.

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

To enable jenkins artefact type testing you need to pass the following extra vars, or define them for the group `docker_sandbox_containers` in the inventory:

- `artifact_tests_jenkins_host`: jenkins host
- `artifact_tests_jenkins_jenkins_path`: URL path where jenkins resides. Default is `/`
- `artifact_tests_jenkins_job_name`: jenkins job name
- `artifact_tests_jenkins_path`: jenkins artifact path within workspace. Default is `/`
- `artifact_tests_jenkins_file`: jenkins artifact file name
- `artifact_tests_jenkins_username`: jenkins username (optional)
- `artifact_tests_jenkins_password`: jenkins password (optional)

## License

Copyright (C) 2019 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
