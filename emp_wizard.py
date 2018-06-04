from odoo import tools, api, fields, models, _


class emp_wizard(models.Model):
	_name = 'emp.wizard'

	name = fields.Char(string='Name')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
	mobile = fields.Char('Mobile')
	description = fields.Text('Description')
	salary = fields.Integer(string="salary")
	gst = fields.Integer(string="GST")
	total = fields.Integer(string="Total")

    # @api.depends(salary,gst)
    # def cals(self):
    #     total=salary+(salary*gst)/100


	# @api.multi
	# def action_my_action(self):
	# 	return True


	#wizard record save the another module
	def _cretate_wizard_new_record(self):

		inv_obj = self.env['wizard_test.wizard_test']
		#self.ensure_one()
		record = inv_obj.create({
			'name_wizard': self.name,
			'gender_wizard': self.gender,
			'mobile_wizard': self.mobile,
			'description_wizard' : self.description,
			})
		print '2222'
		return {'type': 'ir.actions.server_close'}
		


	def wizard_new_record(self):
		self._cretate_wizard_new_record()


	#calling server action to wizard 
	@api.multi
	def some_condition(self):
		return {
     		'type': 'ir.actions.act_window',
            'res_model' : 'emp.wizard',
            'view_type' : 'form',
            'view_mode' : 'form',
            'target'    : 'new'
    }


	# def compute_project_type(self):

	# 	self.env["emp.wizard"].browse(action_emp_wizard).signal_workflow("open")
	# 	print 'hi sandyu'

