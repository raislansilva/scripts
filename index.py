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
        
<odoo>
    <data noupdate="1">
        <record id="email_template_eps" model="mail.template">
            <field name="name">Portal: new user</field>
            <field name="model_id" ref="saude_report.model_saude_report_grupo" />
            <field name="email_to">${object.email_to}</field>
            <field name="subject">${object.subject}</field>
            <field name="email_from"><![CDATA["${object.email_from|safe}"]]></field>
            <field name="auto_delete" eval="True" />
            <field name="user_signature" eval="True" />
            <field name="body_html"><![CDATA[
                <div class="o_layout o_default_theme" style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                    <table class="o_mail_wrapper" style="border-spacing:0px;">
                        <tbody>
                        <tr>
                            <td class="o_mail_no_resize">
                            <br>
                            </td>
                            <td class="o_mail_no_resize o_mail_wrapper_td oe_structure bg-beta" style="border-image-width:1;border-image-source:none;border-image-slice:100%;border-image-repeat:stretch;border-image-outset:0;">
                            <div class="o_mail_block_header_logo mb16">
                                <div class="o_mail_snippet_general">
                                <table class="o_mail_table_styles o_mail_h_padding" style="border-spacing:0px;" cellspacing="0" cellpadding="0" border="0" align="center">
                                    <tbody>
                                    <tr>
                                        <td width="20%">
                                        <br>
                                        </td>
                                        <td class="o_mail_logo_container text-center o_mail_v_padding" width="60%" valign="center">
                                        <a href="http://www.tjpi.jus.br"> <img src="http://odoo.tjpi.jus.br/web/image/28548/tjpi_logo.png" style="border-image-width:1;border-image-source:none;border-image-slice:100%;border-image-repeat:stretch;border-image-outset:0;border-left-style:none;border-left-color:currentcolor;border-bottom-style:none;border-bottom-color:currentcolor;border-right-style:none;border-right-color:currentcolor;border-top-style:none;border-top-color:currentcolor;max-width:400px;" alt="Seu Logo" data-original-title="" title="" class="" border="0"> </a>
                                        </td>
                                        <td style="text-align:right" width="20%">
                                        <br>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                            <div class="o_mail_block_paragraph bg-gray-lighter" style="color:gray;">
                                <div class="o_mail_snippet_general">
                                <table class="o_mail_table_styles" style="background-color:rgb(246, 247, 248);border-spacing:15px;width:100%" cellspacing="0" cellpadding="0" border="0" align="center">
                                    <tbody>
                                    <tr>
                                        <td class="o_mail_h_padding o_mail_v_padding bg-gray-lighter" style="color:rgb(255, 255, 255);" width="100%">
                                        <p class="" style="font-family:-apple-system;, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;" align="center">
                                            &nbsp;
                                            <span class="LineBreakBlob BlobObject DragDrop SCXW190332866 BCX2" style="font-size: 11pt; line-height: 19.425px; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif;color:grey"><span class="BCX2 SCXW190332866">Tribunal de Justiça do Estado do Piauí</span></span>
                                        </p>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                            <div class="o_mail_block_title_text">
                                <div class="o_mail_snippet_general">
                                <table class="o_mail_table_styles" style="border-spacing:0px;" cellspacing="0" cellpadding="0" border="0" align="center">
                                    <tbody>
                                    <tr>
                                        <td class="o_mail_h_padding o_mail_v_padding" width="100%">
                                        <div class="OutlineElement Ltr SCXW190332866 BCX2" style="direction: ltr;">
                                            <p class="Paragraph SCXW190332866 BCX2" role="heading" aria-level="5" style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;font-weight: normal; font-style: normal; vertical-align: baseline; background-color: transparent; color: rgb(47, 84, 150); text-align: left; margin-left: 0px; margin-right: 0px; padding-left: 0px; padding-right: 0px; text-indent: 0px;" lang="PT-BR">
                                            <br>
                                            <span style="color: rgb(47, 84, 150); font-size: 11pt; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif; line-height: 19.425px;" data-contrast="none" class="TextRun SCXW190332866 BCX2" lang="PT-BR"><span class="BCX2 NormalTextRun SCXW190332866" style="background-color: inherit;"><span style="color: rgb(47, 84, 150); font-size: 11pt; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif; line-height: 19.425px;" data-contrast="none" class="BCX2 SCXW190332866 TextRun" lang="PT-BR"><span class="BCX2 NormalTextRun SCXW190332866" style="background-color: inherit;">A SUGESQ, por meio desta mensagem, convidá-o para realização do </span></span>Exame de Periódico de Saúde - EPS. O servidor ou magistrado deverá comparecer a SUGESQ munidos </span></span>
                                            <span style="color: rgb(47, 84, 150); font-size: 11pt; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif; line-height: 19.425px;" data-contrast="none" class="TextRun SCXW190332866 BCX2" lang="PT-BR"><span class="NormalTextRun SCXW190332866 BCX2" style="background-color: inherit;">dos exames médicos descritos</span></span>
                                            <span style="color: rgb(47, 84, 150); font-size: 11pt; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif; line-height: 19.425px;" data-contrast="none" class="TextRun SCXW190332866 BCX2" lang="PT-BR"><span class="NormalTextRun SCXW190332866 BCX2" style="background-color: inherit;"> abaixo.</span></span>
                                            <span class="EOP SCXW190332866 BCX2" style="font-size: 11pt; line-height: 19.425px; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif;" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559738&quot;:40,&quot;335559739&quot;:0,&quot;335559740&quot;:259}"> </span>
                                            <br>
                                            <br>
                                            <span class="EOP SCXW190332866 BCX2" style="font-size: 11pt; line-height: 19.425px; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif;" data-ccp-props="{&quot;201341983&quot;:0,&quot;335559738&quot;:40,&quot;335559739&quot;:0,&quot;335559740&quot;:259}"><i><span style="color: rgb(47, 84, 150); font-size: 11pt; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif; line-height: 19.425px;" data-contrast="none" class="TextRun SCXW190332866 BCX2" lang="PT-BR"><span class="BCX2 NormalTextRun SCXW190332866" style="background-color: inherit;">De acordo com a portaria <b>1502/2019</b> publicado no diário da justiça Nº 8664A 10/05/2019.</span></span></i><span class="LineBreakBlob BlobObject DragDrop SCXW190332866 BCX2" style="font-size: 11pt; line-height: 19.425px; font-family: Calibri Light, Calibri Light_MSFontService, sans-serif;"><span class="BCX2 SCXW190332866"><br></span></span></span>
                                            </p>
                                        </div>
                                        <span class="text-justify"><h5 style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;"></h5><p style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;"><br><span class="text-justify"><span class="text-justify"></span></span></p><p style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;"><span class="text-justify"><span class="text-justify"></span></span></p></span>
                                        <h5 style="font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                        </h5>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            I - dos magistrados e servidores com idade até 45 anos:
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            a) consulta clínico-cardiológica;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            b) hemograma completo;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            c) glicemia em jejum;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            d) colesterol total e frações LDL e HDL;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            e) triglicerídeos;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            f) elementos anormais e sedimento - EAS;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            g) gama glutamil transferase - GAMA GT;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            h) dosagem de creatinina sérica;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            i) sorologia para Chagas;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            j) para as mulheres, consulta ginecológica e exame colpocitológico (opcionalmente);
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            II - dos magistrados e servidores com idade igual ou superior a 46 anos, além dos exames previstos no inciso I:
                                        </p>
                                        <p style="color:grey;color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            a) consulta clínica;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            b) eletrocardiograma;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            c) endoscopia digestiva alta (EDA) (opcional);
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            d) pesquisa de sangue oculto nas fezes (ambos os sexos);
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            e) exame TSH;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            f) para as mulheres, mamografia;
                                        </p>
                                        <p style="color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            g) para os homens, antígeno prostático específico total e livre (PSA) e ecografia prostática (via abdominal), uma única vez.
                                        </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="o_mail_h_padding o_mail_v_padding" width="100%">
                                        <br>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                            <div class="o_mail_block_footer_social" style="display:flex; margin-top:6%;padding-top:10px;border-top:solid 2px rgb(237, 240, 243)">
                                <div class="o_mail_snippet_general">
                                <table class="o_mail_table_styles o_mail_full_width_padding" style="border-spacing:0px;" cellspacing="0" cellpadding="0" align="center">
                                    <tbody>
                                    <tr>
                                        <td class="o_mail_footer_description">
                                        <p class="o_mail_no_margin" style="font-size:1em;color:grey;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            <strong class="o_default_snippet_text">Poder Judiciário do Estado do Piauí</strong>
                                        </p>
                                        <div class="o_mail_footer_links">
                                            &nbsp;
                                            <a href="http://odoo.tjpi.jus.br/page/contactus" class="btn btn-link o_default_snippet_text" style="font-size:1em;-moz-;border-image-width:1;border-image-source:none;border-image-slice:100%;border-image-repeat:stretch;border-image-outset:0;text-decoration: none; color: rgb(56, 52, 61); font-weight: bold;">Contato </a>
                                        </div>
                                        <div>
                                            <p class="o_mail_footer_copy" style="color:grey;font-size:0.8em;font-family:-apple-system, &quot;HelveticaNeue&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;">
                                            <span class="fa fa-copyright"></span>
                                            &copy;2019 Todos os deireitos reservados
                                            <br>
                                            </p>
                                        </div>
                                        </td>
                                        <td class="o_mail_footer_social">
                                        <br>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                            </td>
                            <td class="o_mail_no_resize">
                            <br>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                ]]>
            </field>
        </record>
    </data>
</odoo>       

    
manifest, data
                                        
   depends': ['mail','contacts','base'],                                     
                                        
