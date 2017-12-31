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
from product_model import ProductModel


class ProductSpecificationModel(BasicModel):
    class Meta:
        tab_pages = [u'產品規格']
    product_no = Fields.StringProperty(verbose_name=u'產品型號')
    full_name = Fields.StringProperty(verbose_name=u'完整規格名稱')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    use_price = Fields.BooleanProperty(verbose_name=u'使用獨立銷售價格', default=False)
    price = Fields.FloatProperty(verbose_name=u'獨立銷售價格', default=-1)
    use_cost = Fields.BooleanProperty(verbose_name=u'使用成本', default=False)
    cost = Fields.FloatProperty(verbose_name=u'成本', default=0.0)
    is_enable = Fields.BooleanProperty(verbose_name=u'顯示於前台', default=True)
    can_be_purchased = Fields.BooleanProperty(verbose_name=u'可購買', default=True)

    product = Fields.SearchingHelperProperty(verbose_name=u'所屬產品', target='product_object', target_field_name='title')
    product_object = Fields.KeyProperty(verbose_name=u'所屬產品', kind=ProductModel)
    spec_name_1 = Fields.StringProperty(verbose_name=u'規格名稱 1')
    spec_name_2 = Fields.StringProperty(verbose_name=u'規格名稱 2')
    spec_name_3 = Fields.StringProperty(verbose_name=u'規格名稱 3')
    spec_name_4 = Fields.HiddenProperty(verbose_name=u'規格名稱 4')
    spec_name_5 = Fields.HiddenProperty(verbose_name=u'規格名稱 5')
    spec_value_1 = Fields.StringProperty(verbose_name=u'規格值 1')
    spec_value_2 = Fields.StringProperty(verbose_name=u'規格值 2')
    spec_value_3 = Fields.StringProperty(verbose_name=u'規格值 3')
    spec_value_4 = Fields.HiddenProperty(verbose_name=u'規格值 4')
    spec_value_5 = Fields.HiddenProperty(verbose_name=u'規格值 5')

    @classmethod
    def all_with_product(cls, product_record, *args, **kwargs):
        return cls.query(cls.product_object == product_record.key).order(cls.sort)