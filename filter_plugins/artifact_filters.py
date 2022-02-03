# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.core import combine


def artifact_hide_sensitive_info(artifact):
    """Hide sensitive info in artifact config

    Args:
        artifact (dict): artifact config

    Returns:
        dict: the artifact config with sensitive info hidden
    """

    sensitive_fields = ["username", "password"]
    sensitive_field_replacement = "******"
    result = artifact.copy()

    for f in sensitive_fields:
        if f in artifact.keys():
            result[f] = sensitive_field_replacement

    return result


def artifact_reverse_combine(a, b):
    """Apply ansible combine in a reverse way

    Args:
        a (dict): the dict with the values to merge
        b (dict): the dict to merge in

    Returns:
        dict: dict b with the values of dict a merged
    """
    return combine(b, a, recursive=True)


class FilterModule(object):
    """Ansible filters."""

    def filters(self):
        return {
            "artifact_hide_sensitive_info": artifact_hide_sensitive_info,
            "artifact_reverse_combine": artifact_reverse_combine
        }
