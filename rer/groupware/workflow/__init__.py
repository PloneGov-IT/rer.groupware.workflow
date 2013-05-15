# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory

import config

logger = logging.getLogger('rer.groupware.workflow')
groupwareworkflowMessageFactory = MessageFactory('rer.groupware.workflow')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
