#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu


class ProductBrand(Controller):
    class Scaffold:
        display_in_list = ['name', 'title_lang_zhtw', 'description_lang_zhtw']
        hidden_in_form = ['must_update_product', 'update_timestamp', 'update_cursor', 'is_enable']

    @route_menu(list_name=u'backend', group=u'產品管理', need_hr=True, text=u'產品品牌', sort=1331)
    def admin_list(self):
        return scaffold.list(self)
