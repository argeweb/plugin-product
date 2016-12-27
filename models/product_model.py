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
    name = Fields.StringProperty(verbose_name=u'識別名稱(網址)')
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
    content = Fields.RichTextProperty(verbose_name=u'簡介')
    description = Fields.TextProperty(verbose_name=u'描述')
    info = Fields.TextProperty(verbose_name=u'規格說明')
    use_sku = Fields.BooleanProperty(verbose_name=u'使用 SKU')
    price = Fields.FloatProperty(default=0.0, verbose_name=u'價格')
    spec_name_1 = Fields.StringProperty(verbose_name=u'規格1')
    spec_name_2 = Fields.StringProperty(verbose_name=u'規格2')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用')

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True).order(-cls.sort)
