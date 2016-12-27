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
            'title_lang_zhtw': u'標題',
            'content_lang_zhtw': u'分類說明',
            'image_lang_zhtw': u'形象圖片',
            'description_lang_zhtw': u'網頁描述',
            'keywords_lang_zhtw': u'關鍵字',
        }
    name = Fields.StringProperty(verbose_name=u'識別名稱(網址)')
    title_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體分類標題')
    title_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體分類標題')
    title_lang_enus = Fields.StringProperty(verbose_name=u'英文分類標題')

    category = Fields.CategoryProperty(kind=Category, verbose_name=u'父類別')
    brand = Fields.CategoryProperty(kind=Brand, verbose_name=u'品牌')

    description_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體中文網頁描述')
    description_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體中文網頁描述')
    description_lang_enus = Fields.StringProperty(verbose_name=u'英文網頁描述')

    keywords_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體中文關鍵字')
    keywords_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體中文關鍵字')
    keywords_lang_enus = Fields.StringProperty(verbose_name=u'英文關鍵字')

    image_lang_zhtw = Fields.ImageProperty(verbose_name=u'繁體形象圖片')
    image_lang_zhcn = Fields.ImageProperty(verbose_name=u'簡體形象圖片')
    image_lang_enus = Fields.ImageProperty(verbose_name=u'英文形象圖片')

    must_update_product = Fields.BooleanProperty(default=False, verbose_name=u'必須更新產品')
    update_timestamp = Fields.FloatProperty(default=0.0, verbose_name=u'產品更新時間')
    update_cursor = Fields.StringProperty(default=u'', verbose_name=u'產品更新指針')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用')

    use_content = Fields.BooleanProperty(default=False, verbose_name=u'顯示品牌詳細介紹banner')

    content_lang_zhtw = Fields.RichTextProperty(verbose_name=u'繁體詳細介紹')
    content_lang_zhcn = Fields.RichTextProperty(verbose_name=u'簡體詳細介紹')
    content_lang_enus = Fields.RichTextProperty(verbose_name=u'英文詳細介紹')

    @property
    def title(self):
        return self.title_lang_zhtw

    @property
    def content(self):
        return self.content_lang_zhtw

    @property
    def description(self):
        return self.description_lang_zhtw

    @property
    def keyword(self):
        return self.keywords_lang_zhtw

    @property
    def image(self):
        return self.image_lang_zhtw

    @classmethod
    def find_by_properties(cls, *args, **kwargs):
        return cls.find_all_by_properties(**kwargs).get()

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