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
    class Scaffold:
        display_in_list = ['name', 'title', 'is_enable', 'category']
        hidden_in_form = ['update_timestamp', 'update_cursor']
        actions_in_list = [{
            'name': 'category_list',
            'title': u'產品列表',
            'uri': 'admin:product:product:list',
            'button': u'產品列表',
            'query': [{
                'name': 'category',
                'value': ':key'
            }]
        }]
        navigation = [{
            'uri': 'admin:product:product_category:reset_cache',
            'title': u'產生分類快取檔案',
            'use_json': True,
        }]

    @route_menu(list_name=u'backend', group=u'產品管理', text=u'產品分類', sort=1102)
    def admin_list(self):
        page_view = self.params.get_header('page_view')
        config = ConfigModel.get_config()
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        self.scaffold.change_field_visibility('name', config.custom_category_name)
        if page_view == u'sort':
            self.meta.pagination_limit = 1000
            self.meta.view.template_name = '/product_category/admin_sort.html'
            self.context['change_view_to_edit_function'] = 'reload'
            self.context['change_view_to_view_function'] = 'reload'
            self.context['change_view_to_delete_function'] = 'reload'
        else:
            self.context['change_view_to_sort_function'] = 'reload'
        return scaffold.list(self)

    def admin_add(self):
        config = ConfigModel.get_config()
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        self.scaffold.change_field_visibility('icon', config.use_category_icon)
        self.scaffold.change_field_visibility('name', config.custom_category_name)
        return scaffold.add(self)

    @csrf_protect
    def admin_edit(self, key):
        def scaffold_before_save(controller, container, item):
            if item.category is not None:
                if item.category == item.key:
                    item.category = None

        config = ConfigModel.get_config()
        self.context['config'] = config
        self.scaffold.change_field_visibility('brand', config.display_brand_field)
        self.scaffold.change_field_visibility('use_content', config.display_brand_field)
        self.scaffold.change_field_visibility('icon', config.use_category_icon)
        self.scaffold.change_field_visibility('name', config.custom_category_name)
        self.events.scaffold_before_save += scaffold_before_save
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
    def cron_update_product(self):
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
            n = category.get()
            if n is not None:
                category = n.category
            else:
                category = None
        c = category_list
        for i in xrange(len(category_list), 6):
            category_list.append(None)

        from ..models.product_model import ProductModel
        query = ProductModel.query(ProductModel.category == record.key)
        data, next_cursor, more = query.fetch_page(50, start_cursor=cursor)

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
            'len': len(data),
            'update': record.name
        }

    @route
    def admin_reset_cache(self):
        import urllib2
        import hashlib
        host = self.host_information.host
        if host.find(u'@') > 0:
            host = self.host_information.host.split(u'@')[0] + u':8080'
        url = 'http://%s/data/product_category/items' % host
        try:
            result = urllib2.urlopen(url)
            # self.response.write(result.read())
            code = 'window[\'category\'] = ' + result.read() + ';'
            m2 = hashlib.md5()
            m2.update(code)
            last_md5 = m2.hexdigest()

            from plugins.code.controllers.code import Code
            a = Code.process_file('themes/%s/js/menu_data.js' % self.host_information.theme, code, last_md5)
            if 'info' not in a or a['info'] != 'done':
                self.failure_message(u'快取檔案產生失敗 %s' % a['error'])
        except urllib2.URLError:
            self.logging.exception('Caught exception fetching url')
            return self.json_success_message(u'取得產品分類資料時發生錯誤')
        self.success_message(u'已重新產生快取檔案')

    def before_scaffold(self):
        super(ProductCategory, self).before_scaffold()
        config = ConfigModel.get_config()
        self.scaffold.change_field_visibility('image', config.use_category_image)
        self.scaffold.change_field_visibility('icon', config.use_category_icon)
        self.scaffold.change_field_visibility('description', config.use_category_description)
        self.scaffold.change_field_visibility('keywords', config.use_category_keywords)
        self.scaffold.change_field_visibility('content', config.use_category_content)
        self.scaffold.change_field_visibility('brand', config.display_brand_field)

