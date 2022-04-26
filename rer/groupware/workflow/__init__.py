# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory

from rer.groupware.workflow import config
from rer.groupware.workflow import patches

logger = logging.getLogger('rer.groupware.workflow')
groupwareworkflowMessageFactory = MessageFactory('rer.groupware.workflow')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
