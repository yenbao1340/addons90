"project.project"# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp.osv import fields, osv
from openerp.exceptions import Warning
class task(osv.osv):   
    _inherit = "project.task"

    def _issue_count(self, cr, uid, ids, field_name, arg, context=None):
        Issue = self.pool['project.issue']
        return {
            task_id: Issue.search_count(cr,uid, [('task_id', '=', task_id), '|', ('stage_id.fold', '=', False), ('stage_id', '=', False)], context=context)
            for task_id in ids
        }

    _columns = {        
        'user_id': fields.many2one('res.users', 'Assigned to', select=True, track_visibility='onchange',required=True),       
        'priority': fields.selection([('0','low'), ('1','Normal'),('2','High'), ('3','critical')], 'Priority', select=True),
        'issue_id':fields.one2many('project.issue','task_id','Issue'),
        'issue_count': fields.function(_issue_count, type='integer', string="Issues",),
        } 
    _defaults = {
        'priority': '1',
    }
    def unlink(self, cr, uid, ids, context=None):
        raise Warning("Delete functionality has been disabled")
        return 
    
class project_issue(osv.Model):
    _inherit = "project.issue" 
    _columns = {        
        'priority': fields.selection([('0','low'), ('1','Normal'),('2','High'), ('3','critical')], 'Priority', select=True),
        'description': fields.html('Private Note'),
        
        } 
    def unlink(self, cr, uid, ids, context=None):
        raise Warning("Delete functionality has been disabled")
        return 