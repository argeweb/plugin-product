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
    class Scaffold:
        display_in_list = ('name', 'title_lang_zhtw', 'description_lang_zhtw')
        hidden_in_form = ('must_update_product', 'update_timestamp', 'update_cursor', 'is_enable')
        excluded_in_form = ()

    @route_menu(list_name=u'backend', text=u'產品品牌', sort=1331, group=u'產品銷售', need_hr=True)
    def admin_list(self):
        return scaffold.list(self)
