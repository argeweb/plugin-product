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
    class Meta:
        label_name = {
            "name": u"網址名稱",
            "title": u"後台識別名稱",
            "title_lang_zhtw": u"繁體分類標題",
            "title_lang_zhcn": u"簡體分類標題",
            "title_lang_enus": u"英文分類標題",
            "category": u"父類別",
            "is_enable": u"啟用",
        }
    name = Fields.StringProperty()
    title = Fields.StringProperty()
    title_lang_zhtw = Fields.StringProperty()
    title_lang_zhcn = Fields.StringProperty()
    title_lang_enus = Fields.StringProperty()
    category = Fields.CategoryProperty(kind=Category)
    is_enable = Fields.BooleanProperty(default=True)

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