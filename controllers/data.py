#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from argeweb import Controller, scaffold, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.csrf import CSRF, csrf_protect
from argeweb.components.search import Search
from ..models.product_category_model import ProductCategoryModel


class Data(Controller):
    class Meta:
        default_view = 'json'
        Model = ProductCategoryModel

    @route
    @route_with('/data/product_category/items', name='data:product:category_items')
    def category_items(self):
        self.meta.change_view('json')
        data_target = []
        data, cursor, more = self.meta.Model.all_enable().fetch_page(1000)
        self.insert_data(data, data_target)
        while more:
            data, cursor, more = self.meta.Model.all_enable().fetch_page(1000, start_cursor=cursor)
            self.insert_data(data, data_target)
        self.context["data"] = data_target

    def insert_data(self, data, data_target):
        for item in data:
            parent = ""
            if item.category is not None:
                parent = self.util.encode_key(item.category)
            data_target.append({
                "key": self.util.encode_key(item),
                "sort": item.sort,
                "title": item.title,
                "name": item.name,
                "icon": item.icon,
                "parent": parent
            })
        return data_target
