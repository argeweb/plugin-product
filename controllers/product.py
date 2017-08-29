#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
from argeweb.components.csrf import CSRF, csrf_protect
from ..models.config_model import ConfigModel


class Product(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)

    class Scaffold:
        hidden_in_form = []
        display_in_list = ['image', 'title', 'product_no', 'price', 'is_enable', 'category']
        excluded_in_form = ['category_1', 'category_2', 'category_3', 'category_4', 'category_5', 'category_6']

    @route_menu(list_name=u'welcome', text=u'產品管理', sort=1101)
    @route_menu(list_name=u'backend', group=u'產品管理', text=u'產品', sort=1101)
    def admin_list(self):
        config = self.get_config('product_config')
        self.check_field_config(config, self.scaffold)
        self.fire('change_product_filed_config', config=config)
        return scaffold.list(self)

    @csrf_protect
    def admin_add(self):
        config = self.get_config('product_config')
        self.check_field_config(config, self.scaffold)
        self.fire('change_product_filed_config', config=config)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        config = self.get_config('product_config')
        self.check_field_config(config, self.scaffold)
        self.fire('change_product_filed_config', config=config)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.edit(self, key)

    @staticmethod
    def get_config(config_name):
        return ConfigModel.get_or_create_by_name(config_name)

    @staticmethod
    def check_field_config(config, scaffold, *args, **kwargs):
        scaffold.change_field_visibility('sku_link', False)
        scaffold.change_field_visibility('supplier', False)
        scaffold.change_field_visibility('name', config.custom_product_name, True)
        scaffold.change_field_visibility('is_new', config.display_new_field)
        scaffold.change_field_visibility('is_hot', config.display_hot_field)
        scaffold.change_field_visibility('brand', config.display_brand_field)
        scaffold.change_field_visibility('lock_brand', config.display_brand_field)
        scaffold.change_field_visibility('is_recommend', config.display_recommend_field)
        scaffold.change_field_visibility('is_on_sell', config.display_on_sell_field)
        scaffold.change_field_visibility('is_sell_well', config.display_sell_well_field)
        scaffold.change_field_visibility('is_limit_quantity', config.display_limit_quantity_field)
        scaffold.change_field_visibility('is_limit_datetime', config.display_limit_time_field)
        scaffold.change_field_visibility('limit_end_datetime', config.display_limit_time_field)

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
            if item.lock_brand is False and get_category.brand is not None and brand is None:
                brand = get_category.brand
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
