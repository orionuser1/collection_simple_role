# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# from ansible.module_utils.collection_inspect import get_dunders
from ansible_collections.alikins.collection_inspect.plugins.module_utils.collection_inspect import get_dunders

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


def collection_inspect(text):
    # import pdb; pdb.set_trace()

    try:
        dunders = get_dunders(globals())
    except Exception as e:
        print(e)
        raise

    try:
        aq = [text,
              "collection_inspect filter:\n\t__file__=%s\n" % dunders['__file__'],
              "\t__path__=%s\n" % dunders['__path__'],
              "\t__name__=%s\n" % dunders['__name__'],
              ]
    except Exception as e:
        print(e)
        raise
    return ''.join(aq)


# ---- Ansible filters ----
class FilterModule(object):
    ''' collection inspect and introspection filter '''

    def filters(self):
        return {
            'collection_inspect': collection_inspect
        }
