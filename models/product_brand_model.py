#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class ProductBrandModel(BasicModel):
    class Meta:
        label_name = {
            'title_lang_zhtw': u'品牌名稱',
            'content_lang_zhtw': u'品牌說明',
            'image_lang_zhtw': u'形象圖片',
            'description_lang_zhtw': u'網頁描述',
            'keywords_lang_zhtw': u'關鍵字',
        }
    name = Fields.StringProperty(verbose_name=u'系統編號')
    title_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體品牌名稱')
    title_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體品牌名稱')
    title_lang_enus = Fields.StringProperty(verbose_name=u'英文品牌名稱')

    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用')

    description_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體中文網頁描述')
    description_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體中文網頁描述')
    description_lang_enus = Fields.StringProperty(verbose_name=u'英文網頁描述')

    keywords_lang_zhtw = Fields.StringProperty(verbose_name=u'繁體中文關鍵字')
    keywords_lang_zhcn = Fields.StringProperty(verbose_name=u'簡體中文關鍵字')
    keywords_lang_enus = Fields.StringProperty(verbose_name=u'英文關鍵字')

    image_lang_zhtw = Fields.ImageProperty(verbose_name=u'繁體形象圖片')
    image_lang_zhcn = Fields.ImageProperty(verbose_name=u'簡體形象圖片')
    image_lang_enus = Fields.ImageProperty(verbose_name=u'英文形象圖片')

    content_lang_zhtw = Fields.RichTextProperty(verbose_name=u'繁體品牌說明')
    content_lang_zhcn = Fields.RichTextProperty(verbose_name=u'簡體品牌說明')
    content_lang_enus = Fields.RichTextProperty(verbose_name=u'英文品牌說明')

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