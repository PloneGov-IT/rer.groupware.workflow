# -*- coding: utf-8 -*-
import config

from zope.i18nmessageid import MessageFactory

groupwareworkflowMessageFactory = MessageFactory('rer.groupware.workflow')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
