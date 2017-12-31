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
        tab_pages = [u'產品資料', u'規格', u'狀態', u'圖片', u'說明(顯示用)']
        stop_update = True

    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'產品名稱')
    product_no = Fields.StringProperty(verbose_name=u'產品型號')
    category = Fields.CategoryProperty(kind=ProductCategoryModel, verbose_name=u'分類', dropdown=False)
    category_1 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 1')
    category_2 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 2')
    category_3 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 3')
    category_4 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 4')
    category_5 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 5')
    category_6 = Fields.KeyProperty(kind=ProductCategoryModel, verbose_name=u'類別 6')
    brand = Fields.CategoryProperty(kind=ProductBrandModel, verbose_name=u'品牌')
    lock_brand = Fields.BooleanProperty(verbose_name=u'鎖定品牌(不受分類影響)', default=False)

    try:
        from plugins.supplier.models.supplier_model import SupplierModel
    except ImportError:
        class SupplierModel(BasicModel):
            pass
    supplier = Fields.CategoryProperty(kind=SupplierModel, verbose_name=u'供應商')

    tags = Fields.TextProperty(verbose_name=u'產品標籤', default=u'')
    description = Fields.TextProperty(verbose_name=u'描述')
    content = Fields.RichTextProperty(verbose_name=u'產品介紹')
    content_2 = Fields.RichTextProperty(verbose_name=u'注意事項')

    spec_info = Fields.TextProperty(verbose_name=u'規格說明',  tab_page=1)
    price = Fields.FloatProperty(verbose_name=u'銷售價格', default=0, tab_page=1)
    cost = Fields.FloatProperty(verbose_name=u'成本', default=0.0, tab_page=1)
    spec_1_name = Fields.StringProperty(verbose_name=u'規格 1 名稱', tab_page=1, default=u'規格')
    spec_1 = Fields.TextProperty(verbose_name=u'規格 1 (每行1個)', tab_page=1)
    spec_2_name = Fields.StringProperty(verbose_name=u'規格 2 名稱', tab_page=1, default=u'尺寸')
    spec_2 = Fields.TextProperty(verbose_name=u'規格 2 (每行1個)', tab_page=1)
    spec_3_name = Fields.StringProperty(verbose_name=u'規格 3 名稱', tab_page=1, default=u'顏色')
    spec_3 = Fields.TextProperty(verbose_name=u'規格 3 (每行1個)', tab_page=1)
    spec_4_name = Fields.StringProperty(verbose_name=u'規格 4 名稱', tab_page=1, default=u'材質')
    spec_4 = Fields.TextProperty(verbose_name=u'規格 4 (每行1個)', tab_page=1)
    spec_5_name = Fields.StringProperty(verbose_name=u'規格 5 名稱', tab_page=1, default=u'重量')
    spec_5 = Fields.TextProperty(verbose_name=u'規格 5 (每行1個)', tab_page=1)
    spec_link = Fields.SidePanelProperty(
        verbose_name=u'產品規格', text=u'點擊此處開啟 產品規格管理', tab_page=1,
        auto_open=True, uri='admin:product:product_specification:side_panel_for_product')
    sku_link = Fields.SidePanelProperty(
        verbose_name=u'庫存管理', text=u'點擊此處開啟 庫存管理', tab_page=1,
        auto_open=True, uri='admin:product_stock:stock:side_panel_for_product')

    size_1 = Fields.FloatProperty(verbose_name=u'長度(公分)', default=10.0, tab_page=1)
    size_2 = Fields.FloatProperty(verbose_name=u'寬度(公分)', default=10.0, tab_page=1)
    size_3 = Fields.FloatProperty(verbose_name=u'高度(公分)', default=10.0, tab_page=1)
    weight = Fields.FloatProperty(verbose_name=u'重量(公斤)', default=1.0, tab_page=1)

    is_enable = Fields.BooleanProperty(verbose_name=u'顯示於前台', tab_page=2, default=True)
    can_order = Fields.BooleanProperty(verbose_name=u'可以進行訂購', tab_page=2, default=True)
    can_pre_order = Fields.BooleanProperty(verbose_name=u'可以進行預購', tab_page=2, default=False)
    is_recommend = Fields.BooleanProperty(verbose_name=u'顯示為推薦商品', tab_page=2, default=False)
    is_new = Fields.BooleanProperty(verbose_name=u'顯示為最新產品', tab_page=2, default=False)
    is_hot = Fields.BooleanProperty(verbose_name=u'顯示為熱門產品', tab_page=2, default=False)
    is_on_sell = Fields.BooleanProperty(verbose_name=u'顯示為特價產品', tab_page=2, default=False)
    is_sell_well = Fields.BooleanProperty(verbose_name=u'顯示為熱銷產品', tab_page=2, default=False)
    is_limit_quantity = Fields.BooleanProperty(verbose_name=u'顯示為限量產品', tab_page=2, default=False)
    is_limit_datetime = Fields.BooleanProperty(verbose_name=u'顯示為限時產品', tab_page=2, default=False)
    limit_end_datetime = Fields.DateTimeProperty(verbose_name=u'最後期限', auto_now_add=True, tab_page=2)

    image = Fields.ImageProperty(verbose_name=u'圖片', default=u'', tab_page=3)
    image_2 = Fields.ImageProperty(verbose_name=u'圖片 2', default=u'', tab_page=3)
    image_3 = Fields.ImageProperty(verbose_name=u'圖片 3', default=u'', tab_page=3)
    image_4 = Fields.ImageProperty(verbose_name=u'圖片 4', default=u'', tab_page=3)
    image_5 = Fields.ImageProperty(verbose_name=u'圖片 5', default=u'', tab_page=3)

    old_price = Fields.StringProperty(verbose_name=u'原價', tab_page=4, default=u'')
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
        super(ProductModel, self).after_put(key)
        # from google.appengine.api import taskqueue
        # task = taskqueue.add(
        #     url='/taskqueue/product_stock/stock/update_sku_information',
        #     params={'product': key})

    @property
    def images(self):
        l = []
        for name in ['image', 'image_2', 'image_3', 'image_4', 'image_5']:
            if getattr(self, name) is not u'':
                l.append(getattr(self, name))
        return l

    @property
    def spec_full_list(self):
        spec_lists, total = self.get_spec_lists(self.spec_list)
        return spec_lists

    @property
    def spec_list(self):
        if not hasattr(self, '_spec_list'):
            self._spec_list = [
                self.process_spec(self.spec_1_name, self.spec_1),
                self.process_spec(self.spec_2_name, self.spec_2),
                self.process_spec(self.spec_3_name, self.spec_3),
                self.process_spec(self.spec_4_name, self.spec_4),
                self.process_spec(self.spec_5_name, self.spec_5)
            ]
        return self._spec_list

    @property
    def spec_name_list(self):
        if not hasattr(self, '_spec_name_list'):
            self._spec_name_list = []
            for n in self.spec_list:
                if (len(n) > 1):
                    self._spec_name_list.append(n[0])
        return self._spec_name_list

    @property
    def tags_list(self):
        return self.tags.split('\n')

    def process_spec(self, spec_name, spec_data):
        """ 格式化產品規格資料、去除空白
        :param spec_data: '尺寸:S, L'
        :return:
            ['尺寸', 'S', 'L']
        """
        if spec_data is u'' or spec_data is None:
            return [spec_name]
        return_data = [x.strip() for x in spec_data.split('\r\n')]
        return_data.insert(0, spec_name)
        return return_data

    def gen_spec_item(self, list_exist, list_need_to_append):
        """ 將 list_need_to_append 陣列合併至，list_exist 成一維的陣列
        :param list_exist: ['尺寸:s,大小:5', '尺寸:s,大小:6']
        :param list_need_to_append: ['顏色', '紅', '綠']
        :return:
            ['尺寸:s,大小:5,顏色:紅', '尺寸:s,大小:6,顏色:紅', '尺寸:s,大小:5,顏色:綠', '尺寸:s,大小:6,顏色:綠']
        """
        return_list_exist = []
        for exist_item in list_exist:
            for loop_index in range(1, len(list_need_to_append)):
                new_item = exist_item + u',' + list_need_to_append[0] + u':' + list_need_to_append[loop_index]
                if new_item not in return_list_exist:
                    return_list_exist.append(new_item)
        return return_list_exist

    def get_spec_lists(self, original_specs):
        """ 合併各規格陣列，成一維的陣列
        :param original_specs: an array like [['尺寸', 's', 'm', 'l'], ['大小', '5', '6']]
        :return:
            ['尺寸:s,大小:5','尺寸:m,大小:5','尺寸:l,大小:5','尺寸:s,大小:6','尺寸:m,大小:6','尺寸:l,大小:6']
        """
        total = 0
        spec_lists = []
        for loop_item_spec_list in original_specs:
            loop_item_len = len(loop_item_spec_list) - 1
            if total == 0 and loop_item_len > 0:
                for loop_index in range(1, loop_item_len + 1):
                    if loop_item_spec_list[loop_index] != u'':
                        total += 1
                        new_item = loop_item_spec_list[0] + u':' + loop_item_spec_list[loop_index]
                        spec_lists.append(new_item)
            elif loop_item_len > 0:
                total *= loop_item_len
                spec_lists = self.gen_spec_item(spec_lists, loop_item_spec_list)
        return spec_lists, total

    def get_need_update_spec_item_list(self, new_spec_list, old_spec_records):
        """ 比較應有的規格與現有規格，然後回傳需要新增的規格資料
        :param new_spec_list: ['尺寸:s,大小:5','尺寸:m,大小:5']
        :param old_spec_records: ndb records
        :return:
            ['尺寸:m,大小:5']
        """
        need_to_insert_spec_items = []
        if old_spec_records is not None:
            for spec_item in new_spec_list:
                is_find = False
                for spec_record in old_spec_records:
                    if spec_record.full_name == spec_item:
                        is_find = True
                if is_find is False:
                    need_to_insert_spec_items.append(spec_item)
        return need_to_insert_spec_items
