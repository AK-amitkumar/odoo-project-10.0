odoo.define('base_import_export', function (require) {
    var core = require('web.core');
    var Model = require('web.Model');
    var ListView = require('web.ListView');
    var Sidebar = require('web.Sidebar');
    var _t = core._t;

    ListView.include({
        load_list: function () {
            var model = new Model('res.users'),
                result = this._super.apply(this, arguments);
            model.call('has_group', ['base_import_export.group_import']).then(function (can_import) {
                if (!can_import) {
                    $(".o_control_panel .o_cp_left .o_cp_buttons .o_list_buttons .o_button_import").hide()
                } else {
                    $(".o_control_panel .o_cp_left .o_cp_buttons .o_list_buttons .o_button_import").show()
                }

            });
            return result;
        }
    });

    Sidebar.include({

        add_items: function (section_code, items) {
            var self = this,
                _sup = _.bind(this._super, this),
                model = new Model('res.users'),
                args = ['base_import_export.group_export'];
            model.call('has_group', args).then(function (can_export) {
                if (can_export) {
                    _sup.call(self, section_code, items);
                } else {
                    var export_label = _t("Export"),
                        new_items = items;
                    if (section_code == 'other') {
                        new_items = [];
                        for (var i = 0; i < items.length; i++) {
                            if (items[i]['label'] != export_label) {
                                new_items.push(items[i]);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    _sup.call(self, section_code, new_items);
                }
            });
        }

    })

});


