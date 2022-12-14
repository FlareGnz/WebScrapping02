# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTeste3:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_teste3(self):
        # Test name: teste3
        # Step # | name | target | value
        # 1 | open | https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx |
        self.driver.get("https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx")
        # 2 | setWindowSize | 1265x1011 |
        self.driver.set_window_size(1265, 1011)
        # 3 | click | id=ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento").click()
        # 4 | select | id=ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento | label=Inscrição Imobiliária
        dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento")
        dropdown.find_element(By.XPATH, "//option[. = 'Inscrição Imobiliária']").click()
        # 5 | click | id=ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa").click()
        # 6 | click | css=td:nth-child(5) |
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(5)").click()
        # 7 | click | id=ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa").click()
        # 8 | type | id=ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa | 645197
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa").send_keys("645197")
        # 9 | click | id=ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao").click()
        # 10 | type | id=ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao | 7
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao").send_keys("7")
        # 11 | click | name=ctl00$ContentPlaceHolderPrincipal$CaptchaControl1 |
        self.driver.find_element(By.NAME, "ctl00$ContentPlaceHolderPrincipal$CaptchaControl1").click()
        # 12 | type | name=ctl00$ContentPlaceHolderPrincipal$CaptchaControl1 | yjpuv
        self.driver.find_element(By.NAME, "ctl00$ContentPlaceHolderPrincipal$CaptchaControl1").send_keys("yjpuv")
        # 13 | click | id=ctl00_ContentPlaceHolderPrincipal_btnConsultar |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_btnConsultar").click()
        # 14 | click | id=ctl00_ContentPlaceHolderPrincipal_grdTransmissoes_ctl02_rbTransacao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_grdTransmissoes_ctl02_rbTransacao").click()
        # 15 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbTextoCertidao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbTextoCertidao").click()
        # 16 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoConstrucao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoConstrucao").click()
        # 17 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoTerreno |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoTerreno").click()
        # 18 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbdsAbrangencia |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbdsAbrangencia").click()
        # 19 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbVVA |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbVVA").click()
        # 20 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlDeclarado |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlDeclarado").click()
        # 21 | click | css=.tabela:nth-child(6) |
        self.driver.find_element(By.CSS_SELECTOR, ".tabela:nth-child(6)").click()
        # 22 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlLancadoITIV |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlLancadoITIV").click()
        # 23 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbsqTransmissao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbsqTransmissao").click()
        # 24 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCdInscricaoImob |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCdInscricaoImob").click()
        # 25 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_btnVoltar |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_btnVoltar").click()
        # 26 | click | id=ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento").click()
        # 27 | select | id=ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento | label=Inscrição Imobiliária
        dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_ddlTipoDocumento")
        dropdown.find_element(By.XPATH, "//option[. = 'Inscrição Imobiliária']").click()
        # 28 | click | id=ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa").click()
        # 29 | type | id=ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa | 645197
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDocumentoPesquisa").send_keys("645197")
        # 30 | click | id=ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao").click()
        # 31 | type | id=ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao | 7
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtnuDigitoInscricao").send_keys("7")
        # 32 | click | name=ctl00$ContentPlaceHolderPrincipal$CaptchaControl1 |
        self.driver.find_element(By.NAME, "ctl00$ContentPlaceHolderPrincipal$CaptchaControl1").click()
        # 33 | type | name=ctl00$ContentPlaceHolderPrincipal$CaptchaControl1 | 32qxy
        self.driver.find_element(By.NAME, "ctl00$ContentPlaceHolderPrincipal$CaptchaControl1").send_keys("32qxy")
        # 34 | click | id=ctl00_ContentPlaceHolderPrincipal_btnConsultar |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_btnConsultar").click()
        # 35 | click | id=ctl00_ContentPlaceHolderPrincipal_grdTransmissoes_ctl03_rbTransacao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_grdTransmissoes_ctl03_rbTransacao").click()
        # 36 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCdInscricaoImob |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCdInscricaoImob").click()
        # 37 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbsqTransmissao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbsqTransmissao").click()
        # 38 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlLancadoITIV |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlLancadoITIV").click()
        # 39 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlDeclarado |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlDeclarado").click()
        # 40 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbVVA |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbVVA").click()
        # 41 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoTerreno |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoTerreno").click()
        # 42 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoConstrucao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbvlFracaoConstrucao").click()
        # 43 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCpfCnpjAdquirente |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCpfCnpjAdquirente").click()
        # 44 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCpfCnpjAdquirente |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbCpfCnpjAdquirente").click()
        # 45 | click | css=.tabela:nth-child(13) td |
        self.driver.find_element(By.CSS_SELECTOR, ".tabela:nth-child(13) td").click()
        # 46 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbTextoCertidao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_LbTextoCertidao").click()
        # 47 | click | id=ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_btnVoltar |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCDeclaracao_btnVoltar").click()


class TestTestee2(InscricaoImobiliaria7d):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_testee2(self):
        # Test name: testee2
        # Step # | name | target | value
        # 1 | open | /WebsiteV2/Sistemas/CertidaoDadosCadastrais/Modulos/Principal/CertidaoDadosCadastraisFrm.aspx |
        self.driver.get(
            "https://servicosweb.sefaz.salvador.ba.gov.br/WebsiteV2/Sistemas/CertidaoDadosCadastrais/Modulos/Principal/CertidaoDadosCadastraisFrm.aspx")
        # 2 | setWindowSize | 900x600 |
        self.driver.set_window_size(900, 600)
        # 3 | click | id=ctl00_ContentPlaceHolderPrincipal_txtCdInscricao |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtCdInscricao").click()
        # 4 | type | id=ctl00_ContentPlaceHolderPrincipal_txtCdInscricao | 6451977
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtCdInscricao").send_keys(
            InscricaoImobiliaria7d)
        # 5 | click | id=ctl00_ContentPlaceHolderPrincipal_BtConsultar |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_BtConsultar").click()
        # 6 | click | id=ctl00_ContentPlaceHolderPrincipal_BtConsultar |
        self.vars["window_handles"] = self.driver.window_handles
        # 7 | selectWindow | handle=${win162} |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_BtConsultar").click()
        # 8 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbCdInscricaoImob |
        self.vars["win162"] = self.wait_for_window(2000)
        # 9 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnmContribuinte |
        self.driver.switch_to.window(self.vars["win162"])
        # 10 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuCnpjCpf |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbCdInscricaoImob").click()
        # 11 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLogradouro |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnmContribuinte").click()
        # 12 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuMetrico |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuCnpjCpf").click()
        # 13 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuPorta |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLogradouro").click()
        # 14 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsQuadra |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuMetrico").click()
        # 15 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLote |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuPorta").click()
        # 16 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsEdificio |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsQuadra").click()
        # 17 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuBloco |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLote").click()
        # 18 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsBairro |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsEdificio").click()
        # 19 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuCEP |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuBloco").click()
        # 20 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuSubUnidade |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsBairro").click()
        # 21 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSubunidade |
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuCEP").click()
        # 22 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaTerreno |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnuSubUnidade").click()
        # 23 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlFracaoIdeal |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSubunidade").click()
        # 24 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaConstruida |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaTerreno").click()
        # 25 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaTotal |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlFracaoIdeal").click()
        # 26 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlVenalIPTU |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaConstruida").click()
        # 27 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsUtilizacao |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlAreaTotal").click()
        # 28 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsPadraoConstrutivo |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbvlVenalIPTU").click()
        # 29 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLogradouroTrib |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsUtilizacao").click()
        # 30 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbDtVigenciaLanc |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsPadraoConstrutivo").click()
        # 31 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSituacaoCadastral |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsLogradouroTrib").click()
        # 32 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSituacaoFiscalIPTU |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbDtVigenciaLanc").click()
        # 33 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdtEmissao |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSituacaoCadastral").click()
        # 34 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbTextoCertidao |
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdsSituacaoFiscalIPTU").click()
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbdtEmissao").click()
        self.driver.find_element(By.ID,
                                 "ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbTextoCertidao").click()
