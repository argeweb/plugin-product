#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class ProductConfigModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    category_depth = Fields.StringProperty(verbose_name=u'分類深度', choices=(u'1', u'2', u'3', u'4', u'5', u'6'))
    custom_category_name = Fields.BooleanProperty(default=True, verbose_name=u'自定義分類網址名稱')
    custom_product_name = Fields.BooleanProperty(default=True, verbose_name=u'自定義產品網址名稱')
    display_new_field = Fields.BooleanProperty(default=True, verbose_name=u'顯示最新商品選項')
    display_hot_field = Fields.BooleanProperty(default=True, verbose_name=u'顯示熱門商品選項')
    display_limit_time_field = Fields.BooleanProperty(default=True, verbose_name=u'顯示限時商品選項')
    display_limit_quantity_field = Fields.BooleanProperty(default=True, verbose_name=u'顯示限量商品選項')
