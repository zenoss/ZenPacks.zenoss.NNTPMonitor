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
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class INNTPMonitorDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    timeout = schema.TextLine(title=_t(u'Timeout (seconds)'))
    nntpServer = schema.TextLine(title=_t(u'NNTP Server'), group=_t(u'NNTP'))
    useSSL = schema.Bool(title=_t(u'Use SSL?'), group=_t(u'NNTP'))
    port = schema.Int(title=_t(u'Port'), group=_t(u'NNTP'))
