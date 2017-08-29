#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class ConfigModel(BasicModel):
    title = Fields.StringProperty(verbose_name=u'設定名稱', default=u'產品相關設定')

    category_depth = Fields.StringProperty(verbose_name=u'分類深度', choices=(u'1', u'2', u'3', u'4', u'5', u'6'))
    use_sku = Fields.BooleanProperty(verbose_name=u'使用產品庫存模組', default=True)
    use_supplier = Fields.BooleanProperty(verbose_name=u'使用供應商模組', default=True)
    custom_category_name = Fields.BooleanProperty(verbose_name=u'自定義分類網址名稱', default=True)
    custom_product_name = Fields.BooleanProperty(verbose_name=u'自定義產品網址名稱', default=True)
    display_recommend_field = Fields.BooleanProperty(verbose_name=u'顯示 推薦商品 勾選欄位', default=True)
    display_brand_field = Fields.BooleanProperty(verbose_name=u'顯示 產品品牌 相關欄位', default=True)
    display_new_field = Fields.BooleanProperty(verbose_name=u'顯示 最新商品 勾選欄位', default=True)
    display_hot_field = Fields.BooleanProperty(verbose_name=u'顯示 熱門商品 勾選欄位', default=True)
    display_on_sell_field = Fields.BooleanProperty(verbose_name=u'顯示 特價商品 勾選欄位', default=True)
    display_sell_well_field = Fields.BooleanProperty(verbose_name=u'顯示 熱銷商品 勾選欄位', default=True)
    auto_count_hot_time = Fields.IntegerProperty(verbose_name=u'熱門商品計算時間(分)', default=4320)
    display_limit_time_field = Fields.BooleanProperty(verbose_name=u'顯示 限時商品 勾選欄位', default=True)
    display_limit_quantity_field = Fields.BooleanProperty(verbose_name=u'顯示 限量商品 勾選欄位', default=True)
    stock_recover = Fields.BooleanProperty(verbose_name=u'使用庫存量回收機制', default=False)
    stock_recover_time = Fields.IntegerProperty(verbose_name=u'庫存量回收時間(分)', default=4320)


