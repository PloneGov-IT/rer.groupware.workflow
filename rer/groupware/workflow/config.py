# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import setDefaultRoles
from AccessControl import ModuleSecurityInfo

security = ModuleSecurityInfo("rer.groupware.workflow")

PROJECTNAME = 'rer.groupware.workflow'

#permission to unlock locked objects
security.declarePublic("CanRetractObjects")
CanRetractObjects = "Rer Groupware: Can retract objects"
setDefaultRoles(CanRetractObjects, ('Manager','Owner'))