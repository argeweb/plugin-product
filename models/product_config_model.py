#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class ProductConfigModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u"識別名稱")
    category_depth = Fields.StringProperty(verbose_name=u"分類深度", choices=(u"1", u"2", u"3", u"4", u"5", u"6"))
