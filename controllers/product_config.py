#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class ProductConfig(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)

    class Scaffold:
        display_in_list = ('title', 'is_enable', 'category')
        hidden_in_form = ('name',)

    @route
    @route_menu(list_name=u'backend', text=u'產品相關設定', sort=9930, group=u'系統設定', need_hr=True)
    def admin_config(self):
        record = self.meta.Model.find_by_name(self.namespace)
        if record is None:
            record = self.meta.Model()
            record.name = self.namespace
            record.put()
        return scaffold.edit(self, record.key)

