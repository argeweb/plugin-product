#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb.core.ndb.model import BasicModel
from argeweb.core import property as Fields
from product_category_model import ProductCategoryModel
from product_brand_model import ProductBrandModel
from google.appengine.ext import ndb


class ProductModel(BasicModel):
    class Meta:
        tab_pages = [u'產品資料', u'規格', u'狀態', u'圖片', u'說明']

    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'產品名稱')
    product_no = Fields.StringProperty(verbose_name=u'產品編號')
    category = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'分類')
    category_1 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 1')
    category_2 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 2')
    category_3 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 3')
    category_4 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 4')
    category_5 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 5')
    category_6 = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'類別 6')
    brand = Fields.CategoryProperty(kind=ProductBrandModel, verbose_name=u'品牌')
    lock_brand = Fields.BooleanProperty(verbose_name=u'鎖定品牌(不受分類影響)', default=False)

    try:
        from plugins.supplier.models.supplier_model import SupplierModel
    except ImportError:
        class SupplierModel(BasicModel):
            pass
    supplier = Fields.CategoryProperty(kind=SupplierModel, verbose_name=u'供應商')

    description = Fields.TextProperty(verbose_name=u'描述')
    content = Fields.RichTextProperty(verbose_name=u'詳細說明')

    info = Fields.TextProperty(verbose_name=u'規格說明', tab_page=1)
    price = Fields.FloatProperty(verbose_name=u'銷售價格', default=0, tab_page=1)
    cost = Fields.FloatProperty(verbose_name=u'成本', default=0.0, tab_page=1)
    spec_1 = Fields.StringProperty(verbose_name=u'規格 1', tab_page=1)
    spec_2 = Fields.StringProperty(verbose_name=u'規格 2', tab_page=1)
    spec_3 = Fields.StringProperty(verbose_name=u'規格 3', tab_page=1)
    spec_4 = Fields.StringProperty(verbose_name=u'規格 4', tab_page=1)
    spec_5 = Fields.StringProperty(verbose_name=u'規格 5', tab_page=1)
    sku_link = Fields.SidePanelProperty(verbose_name=u'庫存管理', text=u'點擊此處開啟 庫存管理', tab_page=1,
                                        auto_open=True, uri='admin:product_stock:stock:side_panel_for_product')

    is_enable = Fields.BooleanProperty(verbose_name=u'顯示於前台', tab_page=2, default=True)
    can_order = Fields.BooleanProperty(verbose_name=u'可以進行訂購', tab_page=2, default=False)
    can_pre_order = Fields.BooleanProperty(verbose_name=u'可以進行預購', tab_page=2, default=False)
    is_recommend = Fields.BooleanProperty(verbose_name=u'顯示為推薦商品', tab_page=2, default=False)
    is_new = Fields.BooleanProperty(verbose_name=u'顯示為最新產品', tab_page=2, default=False)
    is_hot = Fields.BooleanProperty(verbose_name=u'顯示為熱門產品', tab_page=2, default=False)
    is_on_sell = Fields.BooleanProperty(verbose_name=u'顯示為特價產品', tab_page=2, default=False)
    is_sell_well = Fields.BooleanProperty(verbose_name=u'顯示為熱銷產品', tab_page=2, default=False)
    is_limit_quantity = Fields.BooleanProperty(verbose_name=u'顯示為限量產品', tab_page=2, default=False)
    is_limit_datetime = Fields.BooleanProperty(verbose_name=u'顯示為限時產品', tab_page=2, default=False)
    limit_end_datetime = Fields.DateTimeProperty(auto_now=True, verbose_name=u'最後期限', tab_page=2)

    image = Fields.ImageProperty(verbose_name=u'圖片', tab_page=3)
    image_2 = Fields.ImageProperty(verbose_name=u'圖片 2', tab_page=3)
    image_3 = Fields.ImageProperty(verbose_name=u'圖片 3', tab_page=3)
    image_4 = Fields.ImageProperty(verbose_name=u'圖片 4', tab_page=3)
    image_5 = Fields.ImageProperty(verbose_name=u'圖片 5', tab_page=3)

    old_price = Fields.StringProperty(verbose_name=u'原價(僅顯示用)', tab_page=4, default=u'')
    helper_1 = Fields.StringProperty(verbose_name=u'重量', tab_page=4, default=u'')
    helper_2 = Fields.StringProperty(verbose_name=u'尺寸', tab_page=4, default=u'')
    helper_3 = Fields.StringProperty(verbose_name=u'成分/材質', tab_page=4, default=u'')
    helper_4 = Fields.StringProperty(verbose_name=u'顏色', tab_page=4, default=u'')
    helper_5 = Fields.StringProperty(verbose_name=u'製造商', tab_page=4, default=u'')
    helper_6 = Fields.StringProperty(verbose_name=u'其他', tab_page=4, default=u'')

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True)).order(-cls.sort)

    @classmethod
    def all_new(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_new==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_new==True)).order(-cls.sort)

    @classmethod
    def all_hot(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_hot==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_hot==True)).order(-cls.sort)

    @classmethod
    def all_recommend(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_recommend==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_recommend==True)).order(-cls.sort)

    @classmethod
    def all_on_sell(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_on_sell==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_on_sell==True)).order(-cls.sort)

    @classmethod
    def all_sell_well(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_sell_well==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_sell_well==True)).order(-cls.sort)

    @classmethod
    def all_limit_quantity(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = ProductCategoryModel.get_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True, cls.is_limit_quantity==True).order(-cls.sort)
        else:
            return cls.query(ndb.AND(ndb.OR(
                cls.category==cat.key, cls.category_1==cat.key, cls.category_2==cat.key, cls.category_3==cat.key,
                cls.category_4==cat.key, cls.category_5==cat.key, cls.category_6==cat.key),
                cls.is_enable==True, cls.is_limit_quantity==True)).order(-cls.sort)

    @classmethod
    def all_brand_product_list(cls, brand=None, *args, **kwargs):
        if brand:
            brand = ProductBrandModel.get_by_name(brand)
        if brand is None:
            return []
        return cls.query(cls.is_enable==True, cls.brand==brand.key).order(-cls.sort)

    @property
    def sku_list(self):
        try:
            from plugins.product_stock.models.stock_keeping_unit_model import StockKeepingUnitModel
            return StockKeepingUnitModel.find_by_product(self)
        except:
            return []

    def after_put(self, key):
        from google.appengine.api import taskqueue
        task = taskqueue.add(
            url='/taskqueue/product_stock/stock/update_sku_information',
            params={'product': key})
