# -*- coding: utf-8 -*-

"""
We need this monkey patch because Ploneboard 3.4 added a new feature that create problems
to us:

See https://github.com/collective/Products.Ploneboard/issues/22
"""

try:
    from Products.Ploneboard.content import PloneboardForum
    from Products.Ploneboard.content import PloneboardComment

    from rer.groupware.workflow import logger

    try:
        PloneboardForum.schema['allowEditComment'].widget.visible = {'edit': 'invisible',
                                                                     'view': 'invisible'}
        logger.warning('Patching Ploneboard: disabling the "Edit own comments" feature')
    except KeyError:
        pass
    PloneboardComment.PloneboardComment.__ac_local_roles_block__ = False
    logger.warning('Patching Ploneboard: disabling __ac_local_roles_block__ for comments')
except ImportError:
    pass
