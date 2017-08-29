#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, route


class Config(Controller):
    class Scaffold:
        display_in_list = ['title', 'is_enable', 'category']

    @staticmethod
    def change_config(controller, item, *args, **kwargs):
        if item.display_brand_field is True:
            controller.fire('enable_role_action', action_uri='plugins.product.controllers.product_brand.list')
        else:
            controller.fire('disable_role_action', action_uri='plugins.product.controllers.product_brand.list')

    @route
    @route_menu(list_name=u'super_user', text=u'產品相關設定', sort=9930, group=u'系統設定', need_hr=True)
    def admin_config(self):
        config_record = self.meta.Model.get_or_create_by_name('product_config')
        self.events.scaffold_after_save += self.change_config
        return scaffold.edit(self, config_record.key)

    @route
    def taskqueue_after_install(self):
        config_record = self.meta.Model.get_or_create_by_name('product_config')
        return 'done'
