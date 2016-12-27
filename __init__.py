#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/07/08.

from argeweb import datastore
from models.product_model import ProductModel
from models.product_model import ProductCategoryModel
from models.product_model import ProductBrandModel

datastore.register('product', ProductModel.find_by_properties)
datastore.register('product_list', ProductModel.all_enable)
datastore.register('product_brand', ProductBrandModel.find_by_properties)
datastore.register('product_category', ProductCategoryModel.find_by_properties)
datastore.register('product_category_list', ProductCategoryModel.all_enable)

plugins_helper = {
    'title': u'產品',
    'desc': u'具分類的產品',
    'controllers': {
        'product': {
            'group': u'產品',
            'actions': [
                {'action': 'list', 'name': u'產品管理'},
                {'action': 'add', 'name': u'新增產品'},
                {'action': 'edit', 'name': u'編輯產品'},
                {'action': 'view', 'name': u'檢視產品'},
                {'action': 'delete', 'name': u'刪除產品'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        },
        'product_category': {
            'group': u'產品分類',
            'actions': [
                {'action': 'list', 'name': u'產品分類管理'},
                {'action': 'add', 'name': u'新增產品分類'},
                {'action': 'edit', 'name': u'編輯產品分類'},
                {'action': 'view', 'name': u'檢視產品分類'},
                {'action': 'delete', 'name': u'刪除產品分類'},
                {'action': 'manage', 'name': u'產品分類排列'},
            ]
        },
        'product_brand': {
            'group': u'品牌管理',
            'actions': [
                {'action': 'list', 'name': u'品牌管理'},
                {'action': 'add', 'name': u'新增品牌'},
                {'action': 'edit', 'name': u'編輯品牌'},
                {'action': 'view', 'name': u'檢視品牌'},
                {'action': 'delete', 'name': u'刪除品牌'},
                {'action': 'manage', 'name': u'品牌排列'},
            ]
        },
        'product_config': {
            'group': u'產品設定',
            'actions': [
                {'action': 'config', 'name': u'產品相關設定'},
            ]
        },
    }
}
