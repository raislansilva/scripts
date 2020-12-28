method saude report

<page string="EPS" attrs="{'invisible':['|', ('paciente_id','=',False), ('eps','=',False)]}">
                            <field name="requisicoes_ids" widget="one2many_list">
                                <tree>
                                    <field name="id_documento"/>
                                    <field name="paciente_id"/>
                                    <field name="grupo_id"/>
                                </tree>
                                <form>
                                    <group>
                                        <field name="id_documento"/>
                                        <field name="paciente_id"/>
                                        <field name="grupo_id"/>
                                    </group>
                                    <group col="1">
                                        <field name="check_eps"/>
                                        <field name="descricao"/>
                                    </group>
                                </form>
                            </field>
                        </page>

class Consulta(models.Model):
    _inherit = 'saude_atendimento.consulta'     
    
    paciente_report = fields.Many2one('saude_report.paciente', string="Paciente Report")
    requisicoes_ids = fields.One2many(related="paciente_report.documento_ids",string="Requisições EPS")
    
    # @api.onchange('paciente_id')
    # def _onchange_paciente_id(self):
    #     paciente = self.env['saude_report.paciente'].search([('cpf','=',self.paciente_id.cpf)])
    #     self.paciente_report = paciente.id

    @api.model
    def create(self,vals):
        paciente = self.env['saude.paciente'].search([('id','=',vals['paciente_id'])])
        paciente_report = self.env['saude_report.paciente'].search([('cpf','=',paciente.cpf)])
        vals['paciente_report'] = paciente_report.id
        return super(Consulta, self).create(vals) 
    
    @api.multi
    def write(self,vals):
        #paciente = self.env['saude.paciente'].search([('id','=',vals['paciente_id'])])
        paciente_report = self.env['saude_report.paciente'].search([('cpf','=',self.paciente_id.cpf)])
        vals['paciente_report'] = paciente_report.id
        return super(Consulta, self).write(vals) 


send email odoo
@api.one
    def action_submit_email(self):
        self.email_from = 'arleidebraz2010@outlook.com'
        self.email_to = 'arleidebraz2010@gmail.com'
        self.email_subject = 'Teste via python a partir do login do suario '
        print "Testando ========= " + self.email_from +" ================"
        print "Testando ========= " + self.email_to +" ================"
        print "Testando ========= " + self.email_subject +" ================"
        template_id = self.env.ref('saude_atendimento.email_template_eps').id
        template =  self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        

<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">


        <record id="email_template_eps" model="mail.template">
            <field name="name">Portal: new user</field>
            <field name="model_id" ref="saude_atendimento.model_saude_atendimento_consulta"/>
            <field name="email_to">${object.email_to}</field>
            <field name="subject">${object.email_subject} </field>
            <field name="email_from"><![CDATA["${object.email_from|safe}"]]></field>
            <field name="auto_delete" eval="True"/>
            <field name="user_signature" eval="True"/>
            <field name="body_html"><![CDATA[

                <hr/>

<p>
    Tribunal de Justiça do Estado do Piauí
</p>
<hr/>
<br/>

<p>
    A SUGESQ, por meio desta mensagem, convidá-o para realização do
     Exame de Periódico de Saúde - EPS. O servidor ou magistrado deverá 
     comparecer a SUGESQ munidos dos exames médicos descritos abaixo.
</p>
<p>
    De acordo com a portaria 1502/2019 publicado no diário da 
    justiça Nº 8664A 10/05/2019.
</p>

<br/>

<p>
   
I - dos magistrados e servidores com idade até 45 anos:

a) consulta clínico-cardiológica;

b) hemograma completo;

c) glicemia em jejum;

d) colesterol total e frações LDL e HDL;

e) triglicerídeos;

f) elementos anormais e sedimento - EAS;

g) gama glutamil transferase - GAMA GT;

h) dosagem de creatinina sérica;

i) sorologia para Chagas;

j) para as mulheres, consulta ginecológica e exame colpocitológico (opcionalmente);

II - dos magistrados e servidores com idade igual ou superior a 46 anos, além dos exames previstos no inciso I:

a) consulta clínica;

b) eletrocardiograma;

c) endoscopia digestiva alta (EDA) (opcional);

d) pesquisa de sangue oculto nas fezes (ambos os sexos);

e) exame TSH;

f) para as mulheres, mamografia;

g) para os homens, antígeno prostático específico total e livre (PSA) e ecografia prostática (via abdominal), uma única vez.
</p>

<br/>
<br/>
<br/>
<br/>

<p>
<strong>
    Poder Judiciário do Estado do Piauí
 Contato 
</strong>
</p>

2020 Todos os deireitos reservados

]]></field>
        </record>
    </data>
</odoo>        

    
manifest, data
                                        
   depends': ['mail','contacts','base'],                                     
                                        
