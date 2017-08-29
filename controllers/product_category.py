#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor
from argeweb.components.csrf import CSRF, csrf_protect
from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
from ..models.config_model import ConfigModel
import time


class ProductCategory(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search, CSRF)

    class Scaffold:
        display_in_list = ['name', 'title', 'is_enable', 'category']
        hidden_in_form = ['must_update_product', 'update_timestamp', 'update_cursor']

    @route_menu(list_name=u'backend', group=u'產品管理', text=u'產品分類', sort=1102)
    def admin_list(self):
        page_view = self.params.get_header('page_view')
        config = ConfigModel.get_by_name('product_config')
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        if page_view == u'sort':
            self.meta.view.template_name = '/product_category/admin_sort.html'
            self.context['change_view_to_edit_function'] = 'reload'
            self.context['change_view_to_view_function'] = 'reload'
            self.context['change_view_to_delete_function'] = 'reload'
        else:
            self.context['change_view_to_sort_function'] = 'reload'
        return scaffold.list(self)

    def admin_add(self):
        config = ConfigModel.get_by_name('product_config')
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        config = ConfigModel.get_by_name('product_config')
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        self.events.scaffold_after_save += self.set_must_update_product_true
        return scaffold.edit(self, key)

    @staticmethod
    def set_must_update_product_true(*args, **kwargs):
        item = kwargs['item']
        item.must_update_product = True
        item.must_update_timestamp = time.time()
        item.put()

    @route
    def admin_change_parent(self):
        parent = self.params.get_ndb_record('parent')
        target = self.params.get_ndb_record('target')
        if parent is not None:
            if parent.key != target.key:
                target.category = parent.key
        else:
            target.category = None
        target.must_update_product = True
        target.must_update_timestamp = time.time()
        target.put()

        self.meta.change_view('json')
        self.context['data'] = {
            'move': 'done'
        }

    @route
    def admin_change_sort(self):
        sort = self.params.get_ndb_record('sort')
        sort_before = self.params.get_ndb_record('sort_before')
        target = self.params.get_ndb_record('target')
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

        self.meta.change_view('json')
        self.context['data'] = {
            'sort': 'done'
        }

    @route
    def taskqueue_update_product(self):
        self.meta.change_view('json')
        self.context['data'] = {
            'update': 'start'
        }
        record = self.meta.Model.need_update_record()
        if record is None:
            self.context['data'] = {
                'update': 'done'
            }
            return
        cursor = Cursor(urlsafe=record.update_cursor)
        self.logging.info(record.update_cursor)
        category = record.category
        category_list = [record.key]
        while category is not None:
            category_list.insert(0, category)
            category = category.get().category
        c = category_list
        for i in xrange(len(category_list), 6):
            category_list.append(None)

        from ..models.product_model import ProductModel
        query = ProductModel.query(ProductModel.category == record.key)
        data, next_cursor, more = query.fetch_page(500, start_cursor=cursor)

        for item in data:
            item.category_1 = category_list[0]
            item.category_2 = category_list[1]
            item.category_3 = category_list[2]
            item.category_4 = category_list[3]
            item.category_5 = category_list[4]
            item.category_6 = category_list[5]
            if item.lock_brand is False:
                item.brand = record.brand
        record.update_cursor = next_cursor.urlsafe() if more else None
        record.must_update_product = more
        record.put_async()
        ndb.put_multi_async(data)
        self.context['data'] = {
            'update': record.name
        }
