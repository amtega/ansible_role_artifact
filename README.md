# Amtega artifact role

This is an [Ansible](http://www.ansible.com) role to download several kinds or artifacts. Currently http/https, maven and gitlab/github artifacts are supported.

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

The role setups a fact named `artifact_result` with the following dict structure:

```yaml
artifact_result:
  <artifact1_id>:
    download_path: <path to the downloaded artifact>
    unarchived_files: <list of files unarchived>
    changed: <true if artifact changed, false in other case>
  <artifact1_id>: ...
  <artifactN_id>: ...  
```

## Example Playbook

This is an example playbook:

``` yaml
---
- name: Artifact role sample
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
      validate_certs: no
```

## Testing

Tests are based on [molecule with docker containers](https://molecule.readthedocs.io/en/latest/installation.html).

```shell
cd amtega.artifact

molecule test --all
```

To enable jenkins artefact type testing you need to pass the following extra environment variables to molecule:

- `ARTIFACT_TESTS_JENKINS_HOST`: jenkins host
- `ARTIFACT_TESTS_JENKINS_JENKINS_PATH`: URL path where jenkins resides. Default is `/`
- `ARTIFACT_TESTS_JENKINS_JOB_NAME`: jenkins job name
- `ARTIFACT_TESTS_JENKINS_PATH`: jenkins artifact path within workspace. Default is `/`
- `ARTIFACT_TESTS_JENKINS_FILE`: jenkins artifact file name
- `ARTIFACT_TESTS_JENKINS_USERNAME`: jenkins username (optional)
- `ARTIFACT_TESTS_JENKINS_PASSWORD`: jenkins password (optional)

## License

Copyright (C) 2022 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
