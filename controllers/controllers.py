# -*- coding: utf-8 -*-
# from odoo import http


# class SatGeolocalization(http.Controller):
#     @http.route('/sat_geolocalization/sat_geolocalization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sat_geolocalization/sat_geolocalization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sat_geolocalization.listing', {
#             'root': '/sat_geolocalization/sat_geolocalization',
#             'objects': http.request.env['sat_geolocalization.sat_geolocalization'].search([]),
#         })

#     @http.route('/sat_geolocalization/sat_geolocalization/objects/<model("sat_geolocalization.sat_geolocalization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sat_geolocalization.object', {
#             'object': obj
#         })
