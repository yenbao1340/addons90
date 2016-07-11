"project.project"# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp.osv import fields, osv
class task(osv.osv):   
    _inherit = "project.task"

    _columns = {        
        'user_id': fields.many2one('res.users', 'Assigned to', select=True, track_visibility='onchange',required=True),       
        'priority': fields.selection([('0','low'), ('1','Normal'),('2','High'), ('3','critical')], 'Priority', select=True),
        'issue_id':fields.one2many('project.issue','task_id','Issue'),
        } 
    _defaults = {
        'priority': '1',
    }
    
    
class project_issue(osv.Model):
    _inherit = "project.issue" 

    