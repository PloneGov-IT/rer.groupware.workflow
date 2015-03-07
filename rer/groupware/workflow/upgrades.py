# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from rer.groupware.workflow import logger

default_profile = 'profile-rer.groupware.workflow:default'


def to_1100(context):
    """
    """
    logger.info('Upgrading rer.groupware.workflow to version 2.1.1')
    context.runImportStepFromProfile(default_profile, 'workflow')
    logger.info('Updated workflows')
    wf_tool = getToolByName(context, 'portal_workflow')
    logger.info('Starting update security settings')
    wf_tool.updateRoleMappings()
    logger.info('Update security settings finish.')


def to_1200(context):
    """
    """
    logger.info('Upgrading rer.groupware.workflow to version 2.2.0')
    context.runImportStepFromProfile(default_profile, 'workflow')
    logger.info('Updated workflows')
    wf_tool = getToolByName(context, 'portal_workflow')
    logger.info('Starting update security settings')
    wf_tool.updateRoleMappings()
    logger.info('Update security settings finish.')
