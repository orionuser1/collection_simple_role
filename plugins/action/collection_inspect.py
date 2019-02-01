from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

from ansible.module_utils.collection_inspect import get_dunders


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        result['dunders'] = get_dunders(globals())
        result['msg'] = "foo"
        return result
