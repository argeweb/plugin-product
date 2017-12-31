#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
from argeweb.components.csrf import CSRF, csrf_protect
from ..models.config_model import ConfigModel


class Product(Controller):
    class Scaffold:
        hidden_in_form = []
        display_in_list = ['image', 'title', 'product_no', 'price', 'is_enable', 'category']
        excluded_in_form = ['category_1', 'category_2', 'category_3', 'category_4', 'category_5', 'category_6']

    @route_menu(list_name=u'welcome', text=u'產品管理', sort=1101)
    @route_menu(list_name=u'backend', group=u'產品管理', text=u'產品', sort=1101)
    def admin_list(self):
        return scaffold.list(self)

    @csrf_protect
    def admin_add(self):
        self.events.scaffold_after_save += self.change_spec
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        self.events.scaffold_after_save += self.change_spec
        return scaffold.edit(self, key)

    def before_scaffold(self):
        super(Product, self).before_scaffold()
        config = ConfigModel.get_config()
        self.scaffold.change_field_visibility('sku_link', False)
        self.scaffold.change_field_visibility('supplier', False)
        self.scaffold.change_field_visibility('name', config.custom_product_name, True)
        self.scaffold.change_field_visibility('is_new', config.display_new_field)
        self.scaffold.change_field_visibility('is_hot', config.display_hot_field)
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('lock_brand', config.display_brand_field)
        self.scaffold.change_field_visibility('is_recommend', config.display_recommend_field)
        self.scaffold.change_field_visibility('is_on_sell', config.display_on_sell_field)
        self.scaffold.change_field_visibility('is_sell_well', config.display_sell_well_field)
        self.scaffold.change_field_visibility('is_limit_quantity', config.display_limit_quantity_field)
        self.scaffold.change_field_visibility('is_limit_datetime', config.display_limit_time_field)
        self.scaffold.change_field_visibility('limit_end_datetime', config.display_limit_time_field)
        self.scaffold.change_field_visibility('cost', config.display_cost)
        self.scaffold.change_field_visibility('tags', config.display_tags)
        self.scaffold.change_field_visibility('content_2', config.display_content_2)
        self.scaffold.change_field_visibility('spec_info', config.display_spec_info)
        self.scaffold.change_field_visibility('spec_link', not config.use_auto_spec_with_product_no)
        self.scaffold.change_field_visibility('spec_1', not config.use_auto_spec_with_product_no)
        self.scaffold.change_field_visibility('spec_2', not config.use_auto_spec_with_product_no)
        self.scaffold.change_field_visibility('spec_3', config.display_spec_3)
        self.scaffold.change_field_visibility('spec_4', config.display_spec_4)
        self.scaffold.change_field_visibility('spec_5', config.display_spec_5)
        self.scaffold.change_field_visibility('spec_1_name', not config.use_auto_spec_with_product_no)
        self.scaffold.change_field_visibility('spec_2_name', not config.use_auto_spec_with_product_no)
        self.scaffold.change_field_visibility('spec_3_name', config.display_spec_3)
        self.scaffold.change_field_visibility('spec_4_name', config.display_spec_4)
        self.scaffold.change_field_visibility('spec_5_name', config.display_spec_5)
        self.scaffold.change_field_visibility('can_order', config.display_can_order)
        self.scaffold.change_field_visibility('can_pre_order', config.display_can_pre_order)
        self.scaffold.change_field_visibility('helper_1', config.display_helper_filed)
        self.scaffold.change_field_visibility('helper_2', config.display_helper_filed)
        self.scaffold.change_field_visibility('helper_3', config.display_helper_filed)
        self.scaffold.change_field_visibility('helper_4', config.display_helper_filed)
        self.scaffold.change_field_visibility('helper_5', config.display_helper_filed)
        self.scaffold.change_field_visibility('helper_6', config.display_helper_filed)
        self.scaffold.change_field_visibility('supplier', False)
        self.scaffold.change_field_visibility('sku_link', False)
        self.use_auto_spec_with_product_no = config.use_auto_spec_with_product_no
        self.fire('after_product_field_config_change', config=config)
        self.meta.pagination_limit = config.pagination_limit

    @staticmethod
    def change_spec(*args, **kwargs):
        controller = kwargs['controller']
        item = kwargs['item']
        if controller.use_auto_spec_with_product_no:
            if item.product_no is u'':
                item.product_no = u'---'
            from ..models.product_specification_model import ProductSpecificationModel
            specs = ProductSpecificationModel.all_with_product(item)
            item.spec_1_name = u'型號'
            item.spec_1 = item.product_no
            full_name = u'%s:%s' % (item.spec_1_name, item.spec_1)
            is_not_find = True
            for spec in specs:
                if spec.full_name == full_name:
                    is_not_find = False
            if is_not_find:
                for spec in specs:
                    spec.key.delete()
                spec = ProductSpecificationModel()
                spec.full_name = full_name
                spec.product_object = item.key
                spec.put()
        category = item.category
        category_list = []
        brand = None
        while category is not None:
            get_category = category.get()
            if get_category is not None:
                category_list.insert(0, category)
                category = get_category.category
                if item.lock_brand is False and get_category.brand is not None and brand is None:
                    brand = get_category.brand
            else:
                category = None
                category_list.insert(0, category)
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

    @route
    def spec(self):
        product = self.params.get_ndb_record('key')
        return self.json(product.specs)

    @route
    def taskqueue_after_install(self):
        from ..models.config_model import ConfigModel
        ConfigModel.get_or_create_by_name('product_config')
        return 'done'

    @route
    def product_insert(self):
        self.meta.change_view('json')
        self.response.headers.setdefault('Access-Control-Allow-Origin', '*')
        category_name = self.params.get_string("category_name")
        from ..models.product_category_model import ProductCategoryModel
        category = ProductCategoryModel.get_by_name(category_name).key
        if category is None:
            self.context['data'] = {
                "category": "error"
            }
            return
        product_name = self.params.get_string("name")
        n = self.meta.Model().get_by_name(product_name)
        if n is None:
            n = self.meta.Model()
            category_list = []
            brand = None
            while category is not None:
                get_category = category.get()
                if get_category is not None:
                    category_list.insert(0, category)
                    category = get_category.category
                    if n.lock_brand is False and get_category.brand is not None and brand is None:
                        brand = get_category.brand
                else:
                    category = None
                    category_list.insert(0, category)
            for i in xrange(len(category_list), 6):
                category_list.append(None)
            n.category_1 = category_list[0]
            n.category_2 = category_list[1]
            n.category_3 = category_list[2]
            n.category_4 = category_list[3]
            n.category_5 = category_list[4]
            n.category_6 = category_list[5]
        n.category = category
        n.title = self.params.get_string("title")
        n.product_no = self.params.get_string("product_no")
        n.old_price = self.params.get_string("price_1")
        n.price = self.params.get_float("price_2")
        n.content = self.params.get_string("content")
        n.image = self.params.get_string('image')
        n.image_2 = self.params.get_string('image_2')
        n.image_3 = self.params.get_string('image_3')
        n.image_4 = self.params.get_string('image_4')
        n.image_5 = self.params.get_string('image_5')
        n.spec_1_name = u'型號'
        n.spec_1 = self.params.get_string("product_no")
        n.put()
        self.context['data'] = {
            "info": "done"
        }
