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
        pagination_limit = 10

    class Scaffold:
        display_properties_in_list = ['name', 'title', 'is_enable', 'category']
        hidden_properties_in_edit = []
        excluded_properties_in_from = ['category_1', 'category_2', 'category_3', 'category_4', 'category_5',
                                       'category_6']

    @route_menu(list_name=u'backend', text=u'產品', sort=1101, group=u'產品維護')
    def admin_list(self):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        return scaffold.list(self)

    @staticmethod
    def get_config(namespace):
        return ProductConfigModel.find_by_name(namespace)

    @staticmethod
    def check_field_config(config, scaffold, *args, **kwargs):

    # custom_category_name = Fields.BooleanProperty(default=True, verbose_name=u"自定義分類網址名稱")
    # custom_product_name = Fields.BooleanProperty(default=True, verbose_name=u"自定義產品網址名稱")
    # display_new_field = Fields.BooleanProperty(default=True, verbose_name=u"顯示最新商品選項")
    # display_hot_field = Fields.BooleanProperty(default=True, verbose_name=u"顯示熱門商品選項")
    # display_limit_time_field = Fields.BooleanProperty(default=True, verbose_name=u"顯示限時商品選項")
    # display_limit_quantity_field = Fields.BooleanProperty(default=True, verbose_name=u"顯示限量商品選項")

        if config.custom_product_name is False:
            scaffold.display_properties_in_list.remove('name')
            scaffold.hidden_properties_in_edit.append('name')


    @staticmethod
    def change_parent_category(*args, **kwargs):
        item = kwargs['item']
        category = item.category
        category_list = []
        while category is not None:
            category_list.insert(0, category)
            category = category.get().category
        c = category_list
        for i in xrange(len(category_list), 6):
            category_list.append(None)
        item.category_1 = category_list[0]
        item.category_2 = category_list[1]
        item.category_3 = category_list[2]
        item.category_4 = category_list[3]
        item.category_5 = category_list[4]
        item.category_6 = category_list[5]
        item.put()

    @csrf_protect
    def admin_add(self):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        self.context['config'] = ProductConfigModel.find_by_name(self.namespace)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        self.check_field_config(self.get_config(self.namespace), self.Scaffold)
        self.events.scaffold_after_save += self.change_parent_category
        return scaffold.edit(self, key)