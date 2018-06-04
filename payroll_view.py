from datetime import datetime
from dateutil import relativedelta
from odoo import models, fields, api,_

class payroll_view(models.TransientModel):
	_name = "emp.payroll_view"


	date_from = fields.Date(string='Date From', required=True,
		default=datetime.now().strftime('%Y-%m-01'))
	date_to = fields.Date(string='Date To', required=True,
		default=str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10])
	employee_name = fields.Many2many('hr.employee',string="Employee Name", required=True, )

	# @api.multi
	# def check_repor(self):
	# 	print '111111111111111'
	# 	data={}
	# 	data['form'] = self.read(['employee_name','date_form','date_to'])[0]
	# 	return self._print_report(data)

	# def _print_report(self,data):
	# 	print '22222222222222222'
	# 	data['form'].update(self.read(['employee_name','date_form','date_to'])[0])
	# 	return self.env['report'].get_action(self,'emp_statusbar.report_payslip',data=data)
	
	# def _build_contexts(self, data):
	# 	print 'PPPPPPPPPPPPPPPPP'
	# 	result = {}
	# 	result['employee_name'] = 'employee_name' in data['form'] and data['form']['employee_name'] or False
	# 	result['date_from'] = data['form']['date_from'] or False
	# 	result['date_to'] = data['form']['date_to'] or False
	# 	return result
	# # def _print_report(self, data):
	# # 	raise (_('Error!'), _('Not implemented.'))

	# @api.multi
	# def print_report(self):
	# 	self.ensure_one()
	# 	data = {}
	# 	data['ids'] = self.env.context.get('active_ids', [])
	# 	data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
	# 	data['form'] = self.read(['date_from', 'date_to', 'employee_name'])[0]
	# 	used_context = self._build_contexts(data)
	# 	data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang') or 'en_US')
	# 	return self.env['report'].get_action(self,'emp_statusbar.report_payslip',data=data)


	@api.multi
	def print_report(self):
		self.ensure_one()
		active_ids = self.env.context.get('active_ids', [])
		datas={
		'ids':active_ids,
		'model': 'emp.payroll_view',
		'form': self.read()[0]
		}
		return self.env['report'].get_action(self,'emp_statusbar.report_payslip',data=datas)



# class employee_payslip(models.AbstractModel):
#     _name = 'report.emp_statusbar.report_payslip'
    
#     @api.model
#     def render_html(self, docids, data=None):
#    #  	if not data.get('form'):
# 			# raise UserError(_("Form content is missing, this report cannot be printed."))
# 		print "****************************"
# 		register_ids = self.env.context.get('active_ids', [])
# 		contrib_registers = self.env['hr.payslip.line'].browse(register_ids)

		
# 		date_from1 = data['form'].get('date_from')
# 		print date_from1,'FFFFFFFFFFFFFFFFFFFFFFFFFF'

# 		date_to1 = data['form'].get('date_to')
# 		print date_to1,'TTTTTTTTTTTTTTTTTTTTTTTTTTTT'
		
# 		employee_name1 = data['form'].get('employee_name')
# 		print employee_name1[1],'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'
# 		for names1 in employee_name1:
# 			print names1,'555555555555555555555'
# 		obj1= self.env['hr.payslip.line'].search([('employee_id','=', employee_name1[1])])
# 		records=[]
# 		report_obj = self.env['report']
# 		for rec2 in obj1:
# 			print rec2.slip_id,"slip iddddddddddddddd"
# 		# 'employee_id.name','=','employee_name.name'
# 		# for rec in obj:
# 		# 	if employee_name1[1] == rec.employee_id.name and date_from1 <= rec.date_from and date_to1 >= rec.date_to:
# 		for names1 in employee_name1:
# 			print names1,'555555555555555555555'
# 			emp = self.env['hr.payslip'].search([('employee_id','=', names1),('date_from','>=',date_from1),('date_to','<=',date_to1)])
# 			print emp,"***************************"
# 			# 	if employee_name1[1] == rec.employee_id.name:
# 			for rec in emp:
# 				print "Payslip Iddddddddddddddddddd"
# 				obj= self.env['hr.payslip.line'].search([('slip_id','=',rec.id)])
# 				print obj,"Cardsssssssssssssssssss"
# 				#records['form']=obj.read(['salary_rule_id','employee_id','rate','amount','quantity','salary_category','total','salary_name'])
# 				print records,'RECORDDDDDDDDDDDDD'
# 				for rec3 in obj:
# 					print rec3,'DDDDDDDDDDDDDDDDDDD'
# 					records.append(rec3)
# 				report = report_obj._get_report_from_name('emp_statusbar.report_payslip')
				
# 		lines_data = records
# 		docargs = {
# 		'doc_ids': register_ids,
# 		'doc_model': 'hr.payslip',
# 		'docs': contrib_registers,
# 		'data': records,
# 		'lines_data': lines_data,
# 		}
# 		return self.env['report'].render('emp_statusbar.report_payslip', docargs)

class HrplayslipPrint(models.Model):

	_inherit='hr.payslip.line'

	salary_name=fields.Char(string="Name",compute='_get_fields')
	salary_code=fields.Char(string="Name",compute='_get_fields')
	salary_category=fields.Char(string="Name",compute='_get_fields')
	payslip_from = fields.Char(string="Name",compute='_get_fields_dates')
	wizard_name = fields.Char(string="Name",compute='_get_fields_dates')
	payslip_name = fields.Char(string="employee_payslip", compute='_get_names')

	@api.one
	def _get_names(self):
		obj = self.env['hr.payslip'].search([])
		for rec in obj:
			self.payslip_name = rec.name
	

	@api.one
	def _get_fields_dates(self):

		obj = self.env['emp.payroll_view'].search([])
		for rec in obj:
			self.payslip_from=rec.date_from
			self.payslip_to = rec.date_to
			self.wizard_name = rec.employee_name.name
			#print self.payslip_from,self.payslip_to,'PPPPPPPPPPPPPPPPPPPPPPPPPP'
	@api.one
	def _get_fields(self):

		obj=self.env['hr.salary.rule'].search([])
		for rec in obj:
			if self.salary_rule_id.id==rec.id:
				self.salary_name=rec.name
				self.salary_category=rec.category_id.name
				self.salary_code=rec.code
				#print self.salary_category, self.employee_id.name,self.salary_name ,"&&&&&&&&&&&&&&&&&&&"