#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from product_category_self_referential_model import ProductCategoryModel as Category


class ProductCategoryModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u"網址名稱")
    title = Fields.StringProperty(verbose_name=u"後台識別名稱")
    title_lang_zhtw = Fields.StringProperty(verbose_name=u"繁體分類標題")
    title_lang_zhcn = Fields.StringProperty(verbose_name=u"簡體分類標題")
    title_lang_enus = Fields.StringProperty(verbose_name=u"英文分類標題")
    category = Fields.CategoryProperty(kind=Category, verbose_name=u"父類別")
    must_update_product = Fields.BooleanProperty(default=False, verbose_name=u"必須更新產品")
    must_update_timestamp = Fields.FloatProperty(default=0.0, verbose_name=u"產品更新時間")
    category_1 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 1")
    category_2 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 2")
    category_3 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 3")
    category_4 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 4")
    category_5 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 5")
    category_6 = Fields.CategoryProperty(kind=Category, verbose_name=u"類別 6")
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u"啟用")

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = cls.find_by_name(category)
        if cat is None:
            return cls.query(cls.category == None, cls.is_enable == True).order(-cls.sort)
        else:
            return cls.query(cls.category == cat.key, cls.is_enable == True).order(-cls.sort)

    def before_put(self):
        super(ProductCategoryModel, self).before_put()