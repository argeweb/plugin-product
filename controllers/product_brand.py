#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor
from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
import time
import random


class ProductBrand(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 1000

    class Scaffold:
        display_properties_in_list = ('name', 'title_lang_zhtw', 'description_lang_zhtw')
        hidden_properties_in_edit = ('must_update_product', 'update_timestamp', 'update_cursor', 'is_enable')
        excluded_properties_in_from = ()

    @route_menu(list_name=u'backend', text=u'品牌管理', sort=1103, group=u'產品維護')
    def admin_list(self):
        return scaffold.list(self)
