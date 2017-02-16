#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from product_category_model import ProductCategoryModel
from product_brand_model import ProductBrandModel


class ProductModel(BasicModel):
    class Meta:
        tab_pages = [u'產品資料', u'規格管理', u'狀態管理', u'產品圖片']
        helper_html = {'tab_page_1': u''}

    name = Fields.StringProperty(verbose_name=u'系統編號')
    title = Fields.StringProperty(verbose_name=u'產品名稱')
    category = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'分類')
    category_1 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 1')
    category_2 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 2')
    category_3 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 3')
    category_4 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 4')
    category_5 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 5')
    category_6 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 6')
    brand = Fields.CategoryProperty(kind=ProductBrandModel, verbose_name=u'品牌')
    lock_brand = Fields.BooleanProperty(default=False, verbose_name=u'鎖定品牌(不受分類影響)')
    description = Fields.TextProperty(verbose_name=u'描述')
    image = Fields.ImageProperty(verbose_name=u'圖片 1', tab_page=3)
    image_2 = Fields.ImageProperty(verbose_name=u'圖片 2', tab_page=3)
    image_3 = Fields.ImageProperty(verbose_name=u'圖片 3', tab_page=3)
    image_4 = Fields.ImageProperty(verbose_name=u'圖片 4', tab_page=3)
    image_5 = Fields.ImageProperty(verbose_name=u'圖片 5', tab_page=3)
    content = Fields.RichTextProperty(verbose_name=u'簡介')

    sku_link = Fields.SidePanelProperty(verbose_name=u'庫存管理', text=u'點擊此處開啟 庫存管理', tab_page=1,
                                        uri='admin:product_stock:stock:list_for_side_panel')
    info = Fields.TextProperty(verbose_name=u'規格說明', tab_page=1)
    # price = Fields.FloatProperty(default=0.0, verbose_name=u'價格', tab_page=1)
    sku_prev_name = Fields.StringProperty(verbose_name=u'sku 前置編號', tab_page=1)
    spec_1 = Fields.StringProperty(verbose_name=u'規格 1', tab_page=1)
    spec_2 = Fields.StringProperty(verbose_name=u'規格 2', tab_page=1)
    spec_3 = Fields.StringProperty(verbose_name=u'規格 3', tab_page=1)
    spec_4 = Fields.StringProperty(verbose_name=u'規格 4', tab_page=1)
    spec_5 = Fields.StringProperty(verbose_name=u'規格 5', tab_page=1)

    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用', tab_page=2)
    is_recommend = Fields.BooleanProperty(default=False, verbose_name=u'顯示為推薦商品', tab_page=2)
    is_new = Fields.BooleanProperty(default=False, verbose_name=u'顯示為最新產品', tab_page=2)
    is_hot = Fields.BooleanProperty(default=False, verbose_name=u'顯示為熱門產品', tab_page=2)
    is_limit_quantity = Fields.BooleanProperty(default=False, verbose_name=u'顯示為限量產品', tab_page=2)
    is_limit_datetime = Fields.BooleanProperty(default=False, verbose_name=u'顯示為限時產品', tab_page=2)
    limit_end_datetime = Fields.DateTimeProperty(auto_now=True, verbose_name=u'最後期限', tab_page=2)

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True).order(-cls.sort)

    @classmethod
    def all_new(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_new==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True, cls.is_new==True).order(-cls.sort)

    @classmethod
    def all_hot(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_hot==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True, cls.is_hot==True).order(-cls.sort)

    @classmethod
    def all_recommend(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_recommend==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True, cls.is_recommend==True).order(-cls.sort)
