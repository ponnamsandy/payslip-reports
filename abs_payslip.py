import time
from odoo import api, models, _
from odoo.exceptions import UserError


class employee_payslip(models.AbstractModel):
    _name = 'report.emp_statusbar.report_payslip'

    def get_employees(self,employee_name1,date_from1,date_to1):
    	records={}
    	count = 1
    	for names in employee_name1:
    		emp = self.env['hr.payslip'].search([('employee_id','=', names),('date_from','>=',date_from1),('date_to','<=',date_to1)])
    		for rec in emp:
    			obj= self.env['hr.payslip.line'].search([('slip_id','=',rec.id)])
    			records[count] = obj.read(['salary_rule_id','employee_id','rate','amount','quantity','salary_category','total','salary_name'])
    			count = count+1
    			print count,'CCCCCCCCCCCCCCCCCCCCCCCCCCCCC'

    			print records
    			print 'SANDEEEEEEEEEEEEEEEEEEEEP'
    	return records


    
    @api.model
    def render_html(self, docids, data=None):
		print "****************************"
		register_ids = self.env.context.get('active_ids', [])
		lines_data = self.env['hr.payslip.line'].browse(register_ids)
		date_from1 = data['form'].get('date_from')
		print date_from1,'FFFFFFFFFFFFFFFFFFFFFFFFFF'

		date_to1 = data['form'].get('date_to')
		print date_to1,'TTTTTTTTTTTTTTTTTTTTTTTTTTTT'
		
		employee_name1 = data['form'].get('employee_name')


		test = self.get_employees(employee_name1,date_from1,date_to1)

		print test,'99999999999999999999999'
		docargs = {
		'doc_model':'hr.payslip.line',
		'data': data,
		'docs': lines_data,
		#'lines_data':lines_data,
		'employees':test,
		}
		return self.env['report'].render('emp_statusbar.report_payslip', docargs)
		


