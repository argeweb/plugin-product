#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
from argeweb.components.csrf import CSRF, csrf_protect
from ..models.product_config_model import ProductConfigModel


class Product(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)
        pagination_limit = 50

    class Scaffold:
        hidden_in_form = []
        display_in_list = ['name', 'title', 'is_enable', 'category']
        excluded_in_form = ['category_1', 'category_2', 'category_3', 'category_4', 'category_5',
                                       'category_6']

    @route_menu(list_name=u'backend', text=u'產品', sort=1101, group=u'產品維護')
    def admin_list(self):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        return scaffold.list(self)

    @staticmethod
    def get_config(namespace):
        return ProductConfigModel.find_by_name(namespace)

    @staticmethod
    def change_field_config(scaffold, field_name, field_value, show_in_list=False):
        if field_value is False:
            if field_name in scaffold.display_in_list:
                scaffold.display_in_list.remove(field_name)
            if field_name not in scaffold.hidden_in_form:
                scaffold.hidden_in_form.append(field_name)
        if field_value is True:
            if field_name in scaffold.hidden_in_form:
                scaffold.hidden_in_form.remove(field_name)
            if show_in_list and field_name not in scaffold.display_in_list:
                scaffold.display_in_list.append(field_name)

    @staticmethod
    def check_field_config(config, scaffold, *args, **kwargs):
        Product.change_field_config(scaffold, 'name', config.custom_product_name, True)
        Product.change_field_config(scaffold, 'is_new', config.display_new_field)
        Product.change_field_config(scaffold, 'is_hot', config.display_hot_field)
        Product.change_field_config(scaffold, 'is_recommend', config.display_recommend_field)
        Product.change_field_config(scaffold, 'is_on_sell', config.display_hot_field)
        Product.change_field_config(scaffold, 'is_sell_well', config.display_recommend_field)
        Product.change_field_config(scaffold, 'is_limit_quantity', config.display_limit_quantity_field)
        Product.change_field_config(scaffold, 'is_limit_datetime', config.display_limit_time_field)
        Product.change_field_config(scaffold, 'limit_end_datetime', config.display_limit_time_field)

    @staticmethod
    def change_parent_category(*args, **kwargs):
        item = kwargs['item']
        category = item.category
        category_list = []
        brand = None
        while category is not None:
            category_list.insert(0, category)
            get_category = category.get()
            category = get_category.category
            if get_category.brand is not None and brand is None:
                brand = get_category.brand
        c = category_list
        for i in xrange(len(category_list), 6):
            category_list.append(None)
        item.category_1 = category_list[0]
        item.category_2 = category_list[1]
        item.category_3 = category_list[2]
        item.category_4 = category_list[3]
        item.category_5 = category_list[4]
        item.category_6 = category_list[5]
        if item.brand is None or item.brand == u'':
            item.brand = brand
        item.put()

    @csrf_protect
    def admin_add(self):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.edit(self, key)