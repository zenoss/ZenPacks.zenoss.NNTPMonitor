###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.zenoss.NNTPMonitor.interfaces import INNTPMonitorDataSourceInfo


class NNTPMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(INNTPMonitorDataSourceInfo)
    cycletime = ProxyProperty('cycletime')
    timeout = ProxyProperty('timeout')
    nntpServer = ProxyProperty('nntpServer')
    useSSL = ProxyProperty('useSSL')
    port = ProxyProperty('port')
    
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
    


