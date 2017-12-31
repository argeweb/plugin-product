#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicConfigModel
from argeweb import Fields


class ConfigModel(BasicConfigModel):
    title = Fields.HiddenProperty(verbose_name=u'設定名稱', default=u'產品相關設定')

    category_depth = Fields.StringProperty(verbose_name=u'分類深度', choices=(u'1', u'2', u'3', u'4', u'5', u'6'))
    use_sku = Fields.BooleanProperty(verbose_name=u'使用產品庫存模組', default=False)
    use_supplier = Fields.BooleanProperty(verbose_name=u'使用供應商模組', default=True)
    use_category_image = Fields.BooleanProperty(verbose_name=u'分類圖片', default=False)
    use_category_icon = Fields.BooleanProperty(verbose_name=u'使用分類 icon', default=False)
    use_category_description = Fields.BooleanProperty(verbose_name=u'分類描述', default=False)
    use_category_keywords = Fields.BooleanProperty(verbose_name=u'SEO 關鍵字', default=False)
    use_category_content = Fields.BooleanProperty(verbose_name=u'詳細介紹', default=False)
    display_can_order = Fields.BooleanProperty(verbose_name=u'顯示 可以進行訂購 勾選欄位', default=False)
    display_can_pre_order = Fields.BooleanProperty(verbose_name=u'顯示 可以進行預購 勾選欄位', default=False)
    display_cost = Fields.BooleanProperty(verbose_name=u'顯示 成本 欄位', default=False)
    display_tags = Fields.BooleanProperty(verbose_name=u'顯示 產品標籤 欄位', default=False)
    display_content_2 = Fields.BooleanProperty(verbose_name=u'顯示 購物說明 欄位', default=False)
    use_auto_spec_with_product_no = Fields.BooleanProperty(verbose_name=u'以型號自動產生規格', default=False)
    display_spec_info = Fields.BooleanProperty(verbose_name=u'顯示 規格說明 欄位', default=False)
    display_spec_3 = Fields.BooleanProperty(verbose_name=u'顯示 規格 3 欄位', default=False)
    display_spec_4 = Fields.BooleanProperty(verbose_name=u'顯示 規格 4 欄位', default=False)
    display_spec_5 = Fields.BooleanProperty(verbose_name=u'顯示 規格 5 欄位', default=False)
    custom_category_name = Fields.BooleanProperty(verbose_name=u'自定義分類網址名稱', default=True)
    custom_product_name = Fields.BooleanProperty(verbose_name=u'自定義產品網址名稱', default=True)
    display_recommend_field = Fields.BooleanProperty(verbose_name=u'顯示 推薦商品 勾選欄位', default=True)
    display_brand_field = Fields.BooleanProperty(verbose_name=u'顯示 產品品牌 相關欄位', default=True)
    display_new_field = Fields.BooleanProperty(verbose_name=u'顯示 最新商品 勾選欄位', default=True)
    display_hot_field = Fields.BooleanProperty(verbose_name=u'顯示 熱門商品 勾選欄位', default=True)
    display_on_sell_field = Fields.BooleanProperty(verbose_name=u'顯示 特價商品 勾選欄位', default=True)
    display_sell_well_field = Fields.BooleanProperty(verbose_name=u'顯示 熱銷商品 勾選欄位', default=True)
    display_helper_filed = Fields.BooleanProperty(verbose_name=u'顯示 說明(顯示用) 欄位', default=False)
    auto_count_hot_time = Fields.IntegerProperty(verbose_name=u'熱門商品計算時間(分)', default=4320)
    display_limit_time_field = Fields.BooleanProperty(verbose_name=u'顯示 限時商品 勾選欄位', default=True)
    display_limit_quantity_field = Fields.BooleanProperty(verbose_name=u'顯示 限量商品 勾選欄位', default=True)
    stock_recover = Fields.BooleanProperty(verbose_name=u'使用庫存量回收機制', default=False)
    stock_recover_time = Fields.IntegerProperty(verbose_name=u'庫存量回收時間(分)', default=4320)
    pagination_limit = Fields.IntegerProperty(verbose_name=u'後台列表頁顯示數量', default=25)


