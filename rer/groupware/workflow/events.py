# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_hasattr
from rer.groupware.workflow import logger


class RoomWorkflowPolicy(object):
    """Apply the local workflow policy to new created Rooms"""

    def __init__(self, context, event):
        self.context = context
        self.request = self.context.REQUEST
        self.applyWorkflowPolicy()

    def applyWorkflowPolicy(self):
        """Create the worfklow policy object for the room"""
        context = self.context

        # check wfp existance: if we are copying current room
        # .wf_policy_config it's already there
        if not safe_hasattr(context, '.wf_policy_config'):
            context.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()

        tool = getToolByName(context, 'portal_placeful_workflow')
        config = tool.getWorkflowPolicyConfig(context)
        config.setPolicyIn('groupware_wf', update_security=True)
        config.setPolicyBelow('groupware_wf', update_security=True)
        logger.info('groupware workflow policy applied')
