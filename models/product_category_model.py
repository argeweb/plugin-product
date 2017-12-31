#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from product_category_self_referential_model import ProductCategoryModel as Category
from product_brand_model import ProductBrandModel as Brand


class ProductCategoryModel(BasicModel):
    class Meta:
        label_name = {
            'title': u'分類名稱',
            'title_lang_zhtw': u'分類名稱',
            'content_lang_zhtw': u'分類說明',
            'image_lang_zhtw': u'形象圖片',
            'description_lang_zhtw': u'網頁描述',
            'keywords_lang_zhtw': u'關鍵字',
        }
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'分類名稱')

    category = Fields.CategoryProperty(kind=Category, verbose_name=u'上層分類')
    category_name = Fields.SearchingHelperProperty(verbose_name=u'上層分類', target='category', target_field_name='name')
    brand = Fields.CategoryProperty(kind=Brand, verbose_name=u'品牌')
    image = Fields.ImageProperty(verbose_name=u'分類圖片', default='')
    icon = Fields.StringProperty(verbose_name=u'ICON', default='')

    description = Fields.StringProperty(verbose_name=u'分類描述')
    keywords = Fields.StringProperty(verbose_name=u'SEO 關鍵字')
    content = Fields.RichTextProperty(verbose_name=u'詳細介紹')

    must_update_product = Fields.BooleanProperty(verbose_name=u'必須更新產品', default=False)
    update_timestamp = Fields.FloatProperty(verbose_name=u'產品更新時間', default=0.0)
    update_cursor = Fields.StringProperty(verbose_name=u'產品更新指針', default=u'')
    is_enable = Fields.BooleanProperty(verbose_name=u'啟用', default=True)

    use_content = Fields.BooleanProperty(verbose_name=u'顯示品牌詳細介紹banner', default=False)

    @classmethod
    def all_enable(cls, *args, **kwargs):
        if hasattr(cls, 'is_enable') is False:
            return None
        if hasattr(cls, 'category') and 'category' in kwargs:
            if kwargs['category'] is None:
                return cls.query(cls.category == None, cls.is_enable == True).order(-cls.sort)
            cat = cls.find_by_properties(name=kwargs['category'])
            if cat is not None:
                return cls.query(cls.category == cat.key, cls.is_enable == True).order(-cls.sort)

        if 'keep_empty' in kwargs:
            if kwargs['keep_empty'] is True:
                return None
        return cls.query(cls.is_enable == True).order(-cls.sort)

    @property
    def children(self):
        return ProductCategoryModel().all().filter(ProductCategoryModel.category == self.key)

    @classmethod
    def need_update_record(cls, *args, **kwargs):
        return cls.query(cls.must_update_product == True).order(cls.update_timestamp).get()

