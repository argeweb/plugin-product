#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
import time
import random


class ProductCategory(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 1000

    class Scaffold:
        display_properties_in_list = ("name", "title", "is_enable", "category")

    @route_menu(list_name=u"backend", text=u"產品分類", sort=102, group=u"產品")
    def admin_list(self):
        return scaffold.list(self)

    @route
    @route_menu(list_name=u"backend", text=u"產品分類排列", sort=103, group=u"產品")
    def admin_manage(self):
        from ..models.product_config_model import ProductConfigModel
        self.context["config"] = ProductConfigModel.find_by_name(self.namespace)
        return scaffold.list(self)

    @route
    def admin_change_parent(self):
        parent = self.params.get_ndb_record("parent")
        target = self.params.get_ndb_record("target")
        if parent is not None:
            if parent.key != target.key:
                target.category = parent.key
        else:
            target.category = None
        target.must_update_product = True
        target.must_update_timestamp = time.time()
        target.put()

        self.meta.change_view("json")
        self.context["data"] = {
            "move": "done"
        }

    @route
    def admin_change_sort(self):
        sort = self.params.get_ndb_record("sort")
        sort_before = self.params.get_ndb_record("sort_before")
        target = self.params.get_ndb_record("target")
        s = [target.sort]
        if sort is not None:
            s.append(sort.sort)
        else:
            s = [time.time()]
        if sort_before is not None:
            s.append(sort_before.sort)
        s = sorted(s, reverse=True)
        if len(s) == 1:
            target.sort = s[0]
            target.put_async()
        if len(s) == 2:
            if sort is not None:
                sort.sort = s[0]
                sort.put_async()
                target.sort = s[1]
                target.put_async()
            else:
                target.sort = s[0]
                target.put_async()
                sort_before.sort = s[1]
                sort_before.put_async()
        if len(s) == 3:
            sort.sort = s[0]
            sort.put_async()
            target.sort = s[1]
            target.put_async()
            sort_before.sort = s[2]
            sort_before.put_async()

        self.meta.change_view("json")
        self.context["data"] = {
            "sort": "done"
        }
