#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from datetime import datetime
from argeweb import Controller, scaffold, route_menu, route_with, route, settings
from argeweb import auth, add_authorizations
from argeweb.components.pagination import Pagination
from argeweb.components.csrf import CSRF, csrf_protect
from argeweb.components.search import Search
from plugins.mail import Mail
from ..models.product_category_model import ProductCategoryModel


class Data(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)
        default_view = 'json'
        Model = ProductCategoryModel

    @route
    @route_with('/data/product_category/items', name='data:product:category_items')
    def category_items(self):
        self.meta.change_view('json')
        n_data = []
        data = self.meta.Model.all_enable().fetch(1000)
        for item in data:
            parent = ""
            if item.category is not None:
                parent = self.util.encode_key(item.category)
            n_data.append({
                "key": self.util.encode_key(item),
                "sort": item.sort,
                "title": item.title,
                "name": item.name,
                "parent": parent
            })
        self.context["data"] = n_data