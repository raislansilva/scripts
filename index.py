
send email odoo

model 
 @api.multi
    def action_send_email(self):
        template_id = self.env.ref('coupons.email_template_coupon').id
        template = self.env['mail.template'].browse(template_id)
        #mail_template.write({'email_to': self.email}
        if template:
            template.send_mail(self.id, force_send=True, raise_exception=True)
            
data > xml
<odoo>
    <data noupdate="1">
        <!--Email template -->
        <record id="email_template_coupon" model="mail.template">
            <field name="name">Email Template</field>
            <field name="model_id" ref="coupons.model_coupons_ticket"/>
            <field name="email_from">${(object.company_id.email |safe}</field>
            <field name="email_to">${object.partner_id.email}</field>
            <field name="subject">Ref ${object.name or 'n/a' }</field>
            <field name="auto_delete" eval="True"/>
            <field name="lang">${object.partner_id.lang}</field>
            <field name="body_html"><![CDATA[
            <p>Dear Raislan,<br/><br/>
            Good job, you've just created your first e-mail template!<br/></p>
              Regards,<br/>
              ${(object.company_id.name)} ]]>
            </field>
        </record>
    </data>
</odoo>
    
manifest, data
                                        
   depends': ['mail','contacts','base'],                                     
                                        
