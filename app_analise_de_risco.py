#______________________________________________________________________________________________________________________

## IMPORTA BIBLIOTECAS PARA O PYTHON ##

import pandas as pd
import streamlit as st
import re
import os

#______________________________________________________________________________________________________________________

## INPUTS DA PÁGINA DO STREAMLIT ##

st.set_page_config(
     page_title="PMI - Empresas Alvará de Funcionamento",
     page_icon=('./dados/favicon.png'),
 )

#______________________________________________________________________________________________________________________

## EXTRAI INFORMAÇÕES DO APROVA ##

# Input box do aprova
logo_image = ('./dados/logo.png')
st.sidebar.image(logo_image, width=200)
st.sidebar.subheader('Verificação do processo:')
texto_aprova = st.sidebar.text_input('CTRL+  V da página do APROVA:','',key="inputbox1")

if texto_aprova != "":
    #Separa o texto do aprova entre os trechos viabilidade e estabelecimento
    texto_aprova_split = re.sub(' +', ' ',texto_aprova).split(' ')
    #itens_analise=['Viabilidade','Estabelecimento','Bairro','Logradouro','Número','Social', 'Nome','PRINT']
    index_aprova1=texto_aprova_split.index('Selecione')
    index_aprova2=texto_aprova_split.index('Horário')
    
    ##Inscrição imobiliária no Aprova Digital
    
    inscricao_aprova = re.findall(r'\d\d\d.\d\d\d.\d\d.\d\d\d\d.\d\d\d\d.\d\d\d', texto_aprova)
    inscricao_aprova = inscricao_aprova[0]

    trecho_aprova = " ".join(texto_aprova_split[index_aprova1:index_aprova2])

    #Separa o texto do aprova em espaços para retornar a razão social
    itens_analise=['Razao','Horário']
    index_aprova3=texto_aprova_split.index('Razao')
    index_aprova4=texto_aprova_split.index('Horário')
    
    trecho_aprova_split2 = texto_aprova_split[index_aprova3:index_aprova4]
    itens_analise=['Social','Nome']
    index_aprova5=trecho_aprova_split2.index('Social')+1
    index_aprova6=trecho_aprova_split2.index('Nome')
    razao_social_aprova = " ".join(trecho_aprova_split2[index_aprova5:index_aprova6])
     

    #Separa o texto do aprova em espaços para retornar o endereço
    itens_analise=['REGIN','Razao']
    index_aprova7=texto_aprova_split.index('REGIN')
    index_aprova8=texto_aprova_split.index('Razao')
    trecho_aprova_split3 = texto_aprova_split[index_aprova7:index_aprova8]
    itens_analise=['Bairro','Logradouro']
    index_aprova9=trecho_aprova_split3.index('Bairro')+1
    index_aprova10=trecho_aprova_split3.index('Logradouro')
    index_aprova11=trecho_aprova_split3.index('Logradouro')+1
    index_aprova12=trecho_aprova_split3.index('Número')
    index_aprova13=trecho_aprova_split3.index('Predial')+1
    index_aprova14=trecho_aprova_split3.index('CEP')
    bairro_aprova = " ".join(trecho_aprova_split3[index_aprova9:index_aprova10])
    logradouro_aprova = " ".join(trecho_aprova_split3[index_aprova11:index_aprova12])
    numero_aprova = " ".join(trecho_aprova_split3[index_aprova13:index_aprova14])

    index_aprova17=trecho_aprova_split3.index('Sala)')
    index_aprova18=trecho_aprova_split3.index('(Sala)')
    index_aprova19=trecho_aprova_split3.index('(Box)')
    index_aprova20=trecho_aprova_split3.index('Telefone')
    complemento1_aprova = " ".join(trecho_aprova_split3[index_aprova17+1:index_aprova18-2])
    complemento2_aprova = " ".join(trecho_aprova_split3[index_aprova18+1:index_aprova19-2])
    complemento3_aprova = " ".join(trecho_aprova_split3[index_aprova19+1:index_aprova20])

    #Extrai as informações do trecho
    cnaes_aprova = re.findall(r'\d\d.\d\d-\d-\d\d', texto_aprova)
    cnaes_aprova=list(set(cnaes_aprova))

    itens_analise=['Razao','Horário']
    index_aprova15=texto_aprova_split.index('Razao')
    index_aprova16=texto_aprova_split.index('Horário')
    trecho_aprova_split4 = texto_aprova_split[index_aprova15:index_aprova16]
    trecho_aprova_cnpj = " ".join(trecho_aprova_split4)
    cnpj_aprova = re.findall(r'\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d', trecho_aprova_cnpj)


else:
    cnpj_aprova =""
#______________________________________________________________________________________________________________________

## EXTRAI INFORMAÇÕES DO REGIN ##

# Input box do REGIN
texto_regin = st.sidebar.text_input('CTRL + V do REGIN:','',key="inputbox2")

if texto_regin != "":
    #Extrai informações do REGIN

    texto_regin_split = re.sub(' +', ' ',texto_regin).split(' ')

    itens_analise=['Código','NOMES', 'SMU', 'SANITÁRIA']
    index1=texto_regin_split.index('Código')
    index2=texto_regin_split.index('NOMES')

    trecho_regin_cnaes = " ".join(texto_regin_split[index1:index2])
    cnaes_regin = re.findall(r'\d\d\d\d\d\d\d', trecho_regin_cnaes)

    cnaes_formatados_regin=[]
    count=0
    for cnae in cnaes_regin:
    
        format_cnae = cnae[:2]+'.'+cnae[2:4]+'-'+cnae[4:5]+'-'+cnae[5:]
        cnaes_formatados_regin.append(format_cnae)
        count+=1

    index3=texto_regin_split.index('LOCALIZAÇÃO')+1
    index4=texto_regin_split.index('ITAJAI')
    endereco_regin = " ".join(texto_regin_split[index3:index4])
    
    index5=texto_regin_split.index('SMU')+1
    index6=texto_regin_split.index('SANITÁRIA')-11
    despacho_regin = " ".join(texto_regin_split[index5:index6])
    
       

#______________________________________________________________________________________________________________________

## EXTRAI INFORMAÇÕES DO CNPJ ##

# Input box do CNPJ
texto_cnpj = st.sidebar.text_input('CTRL + V do CNPJ:','',key="inputbox3")

if texto_cnpj != "":
    cnaes_cnpj = re.findall(r'\d\d.\d\d-\d-\d\d', texto_cnpj)
    cnae_principal_cnpj=cnaes_cnpj[0]
    numero_cnpj = re.findall(r'\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d', texto_cnpj)
    texto_cnpj_split = re.sub(' +', ' ',texto_cnpj).split(' ')

    #Separa o cartão cnpj em elementos separado por espaços para extração de textos específicos
    itens_analise=['EMPRESARIAL','TÍTULO', 'LOGRADOURO','NÚMERO']
    index_cnpj1=texto_cnpj_split.index('EMPRESARIAL')+1
    index_cnpj2=texto_cnpj_split.index('TÍTULO')
    razao_social_cnpj = " ".join(texto_cnpj_split[index_cnpj1:index_cnpj2])

    #Separa o primeiro split para puxar o endereço
    index_cnpj3=texto_cnpj_split.index('NATUREZA')+1
    index_cnpj4=texto_cnpj_split.index('ESPECIAL')
    texto_cnpj_split2 = texto_cnpj_split[index_cnpj3:index_cnpj4] #função que separa o primeiro split
    
    index_cnpj5=texto_cnpj_split2.index('LOGRADOURO')+1
    index_cnpj6=texto_cnpj_split2.index('NÚMERO')
    logradouro_cnpj = " ".join(texto_cnpj_split2[index_cnpj5:index_cnpj6])
    
    index_cnpj7=texto_cnpj_split2.index('NÚMERO')+1
    index_cnpj8=texto_cnpj_split2.index('COMPLEMENTO')
    numeropredial_cnpj = " ".join(texto_cnpj_split2[index_cnpj7:index_cnpj8])
    
    index_cnpj9=texto_cnpj_split2.index('COMPLEMENTO')+1
    index_cnpj10=texto_cnpj_split2.index('CEP')
    complemento_cnpj = " ".join(texto_cnpj_split2[index_cnpj9:index_cnpj10])
    
    index_cnpj11=texto_cnpj_split2.index('BAIRRO/DISTRITO')+1
    index_cnpj12=texto_cnpj_split2.index('MUNICÍPIO')
    bairro_cnpj = " ".join(texto_cnpj_split2[index_cnpj11:index_cnpj12])


#_____________________________________________________________________________________________________________________

## VERIFICA SOMENTE O CNPJ ##

st.sidebar.subheader('Verificação somente do CNPJ:')

# Input box do CNPJ
somente_cnpj = st.sidebar.text_input('CTRL + V do CNPJ: ','',key="inputbox4")

if somente_cnpj != "":
    cnaes_cnpj2 = re.findall(r'\d\d.\d\d-\d-\d\d', somente_cnpj)
    cnae_principal_cnpj2=cnaes_cnpj2[0]
    numero_cnpj2 = re.findall(r'\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d', somente_cnpj)

    texto_cnpj2_split = re.sub(' +', ' ',somente_cnpj).split(' ')

    #Separa o cartão cnpj em elementos separado por espaços para extração de textos específicos
    itens_analise=['EMPRESARIAL','TÍTULO', 'LOGRADOURO','NÚMERO']
    index_cnpj1=texto_cnpj2_split.index('EMPRESARIAL')+1
    index_cnpj2=texto_cnpj2_split.index('TÍTULO')
    razao_social_cnpj2 = " ".join(texto_cnpj2_split[index_cnpj1:index_cnpj2])

    #Separa o primeiro split para puxar o endereço
    index_cnpj3=texto_cnpj2_split.index('NATUREZA')+1
    index_cnpj4=texto_cnpj2_split.index('ESPECIAL')
    texto_cnpj_split2 = texto_cnpj2_split[index_cnpj3:index_cnpj4] #função que separa o primeiro split
    
    index_cnpj5=texto_cnpj_split2.index('LOGRADOURO')+1
    index_cnpj6=texto_cnpj_split2.index('NÚMERO')
    logradouro_cnpj2 = " ".join(texto_cnpj_split2[index_cnpj5:index_cnpj6])
    index_cnpj7=texto_cnpj_split2.index('NÚMERO')+1
    index_cnpj8=texto_cnpj_split2.index('COMPLEMENTO')
    numeropredial_cnpj2 = " ".join(texto_cnpj_split2[index_cnpj7:index_cnpj8])
    index_cnpj9=texto_cnpj_split2.index('COMPLEMENTO')+1
    index_cnpj10=texto_cnpj_split2.index('CEP')
    complemento_cnpj2 = " ".join(texto_cnpj_split2[index_cnpj9:index_cnpj10])
    index_cnpj11=texto_cnpj_split2.index('BAIRRO/DISTRITO')+1
    index_cnpj12=texto_cnpj_split2.index('MUNICÍPIO')
    bairro_cnpj2 = " ".join(texto_cnpj_split2[index_cnpj11:index_cnpj12])

else:
   razao_social_cnpj2 = ""
     
#_____________________________________________________________________________________________________________________

## BOTÃO LIMPAR ##

def clear_text():
    st.session_state["inputbox1"] = ""
    st.session_state["inputbox2"] = ""
    st.session_state["inputbox3"] = ""
    st.session_state["inputbox4"] = ""
st.sidebar.button("Limpar", on_click=clear_text)

     
#_____________________________________________________________________________________________________________________

## ESTRUTURA PAGINA VERIFICAÇÃO DE PROCESSOS ##

st.title('PMI - ALVARÁ EMPRESAS')
if (texto_aprova or somente_cnpj) == '':
     st.markdown('<<< Copie e cole as informações na barra lateral esquerda.')
     st.subheader(str('Links úteis'))
     st.markdown('APROVA: '+str('https://itajai.prefeituras.net/login'))
     st.markdown('CNPJ: '+str('https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp'))
     st.markdown('REGIN: '+str('http://regin.jucesc.sc.gov.br/regin.externo/CON_ViabilidadeSelecaoExternoV4.aspx?'))
     st.markdown('GEO: '+str('https://arcgis.itajai.sc.gov.br/geoitajai/plantacadastral/plantacadastral.html'))
     st.markdown('CBMSC: '+str('https://sigat.cbm.sc.gov.br/sigat/modulos/solicitacoes/acessocidadao2.php'))
     st.markdown('CBMSC NOVO: '+str('https://esci.cbm.sc.gov.br/Safe/PublicoExterno/ControllerConferenciaDigital/'))
     st.markdown('PMI ALVARÁ: '+str('https://portaldocidadao.itajai.sc.gov.br/servico_link/7'))
     st.markdown('PMI TERMO ÚNICO: '+str('https://portaldocidadao.itajai.sc.gov.br/servico.php?id=89'))
     st.markdown('ALVARÁ PROVISÓRIO: '+str('https://portaldocidadao.itajai.sc.gov.br/c/88'))
     st.markdown('DRIVE: '+str('https://drive.google.com/drive/folders/1LfDRxkb8Tv6fspqjBGuToB0xAQO-xGDv?usp=sharing'))
     st.markdown('APP CMGDT: '+str('https://arcgis.itajai.sc.gov.br/portal/apps/webappviewer/index.html?id=c7fefa2b76864a969ee922add9e02fd3#'))
     st.markdown('APP SETORES: '+str('https://arcgis.itajai.sc.gov.br/portal/apps/webappviewer/index.html?id=ab4e19d77cc547968dce80dce054d8db'))
     st.markdown('MEI: '+str('https://docs.google.com/spreadsheets/d/1bnRz4OJd5IAaZ5QtXHT0gxf2w3WPnMprbsG1WLdyenc/edit?usp=sharing'))
     st.markdown('ESCRITÓRIOS VIRTUAIS: '+str('https://docs.google.com/spreadsheets/d/1J0gHPYf69kp0F9flnAQBqPf8rQ0ScrUVoHN7vxEij30/edit?usp=sharing'))
     
#_____________________________________________________________________________________________________________________
 
## PÁGINA - SOMENTE CNPJ ##  

try:
     if somente_cnpj != "":
          st.subheader(str('Dados do cartão CNPJ'))
          #st.text('CNPJ: '+numero_cnpj2)
          st.markdown('RAZÃO SOCIAL: '+razao_social_cnpj2)
          #st.markdown('CNPJ: '+numero_cnpj2)
          st.markdown('ENDEREÇO: '+logradouro_cnpj2+', '+numeropredial_cnpj2+', '+bairro_cnpj2+' '+complemento_cnpj2)
          st.subheader('Verificação das atividades e documentação específica')
          
          tabela_cnaes = pd.read_csv('./dados/grau_risco_maio_2021.xlsx - Página2.csv', sep=',')
          
          
          cnaes_cnpj2 = pd.DataFrame(cnaes_cnpj2)
        
          nova_tabela=tabela_cnaes.merge(cnaes_cnpj2,left_on='codigo', right_on=0)
          nova_tabela.drop([0], axis=1, inplace=True)
          nova_tabela
        
          #Verificação armas de fogo
        
          cnae1 = '47.89-0-09'
          if cnae1 in cnaes_cnpj2:
               st.text('*** APRESENTA CNAE para comércio de ARMAS DE FOGO, solicitar documentação extra.')
          if cnae1 not in cnaes_cnpj2:
               st.text('*** NÃO apresenta CNAE para comércio de armas de fogo.')     
            
          #Verificação SPE
        
          cnae2 = '41.10-7-00'      
          cnae3 = '41.20-4-00'
        
          if (cnae2 or cnae3) in cnaes_cnpj2:
             st.text('*** APRESENTA CNAE para construção ou incorporação, verificar se é uma SPE.')
          if (cnae2 or cnae3) not in cnaes_cnpj2:
             st.text('*** NÃO apresenta CNAE para incorporação imobiliária ou construção (SPE).')

          #Verificação transporte escolar
        
          cnae4 = '49.24-8-00'
          if cnae4 in cnaes_cnpj2:
              st.text('*** APRESENTA CNAE para TRANSPORTE ESCOLAR, solicitar documentação extra.')
          if cnae4 not in cnaes_cnpj2:
              st.text('*** NÃO apresenta CNAE para transporte escolar.')
            
          #Verificação transporte por cabotagem
          cnae5 = '50.11-4-02'
          if cnae5 in cnaes_cnpj2:
              st.text('*** APRESENTA CNAE para transporte por CABOTAGEM, solicitar autorização da ANTAC.')
          if cnae5 not in cnaes_cnpj2:
              st.text('*** NÃO apresenta CNAE para transporte de cabotagem.')
          
          st.subheader('Verificação do grau de risco')
          tabela_risco = pd.read_csv('./dados/Decreto 11.985 - Grau de risco.csv', sep=',')
          
          cnaes_cnpj2 = pd.DataFrame(cnaes_cnpj2)        
          nova_tabela2=tabela_risco.merge(cnaes_cnpj2,left_on='CÓDIGO', right_on=0)
          nova_tabela2.drop([0], axis=1, inplace=True)
          nova_tabela2
          
except:
  pass



#_____________________________________________________________________________________________________________________

## PÁGINA - CONFERÊNCIA DO PROCESSO ##

try:
    if texto_aprova != "":
        #Printa o resumo do processo
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Resumo do processo')
        st.text('RAZÃO SOCIAL: '+razao_social_aprova+', CNPJ: '+cnpj_aprova[0])
        st.text(logradouro_cnpj+', '+bairro_cnpj+', '+numeropredial_cnpj+', '+complemento_cnpj)
        st.text('INSCRIÇÃO IMOBILIÁRIA: '+str(inscricao_aprova[0:15]))
        endereço_split = re.sub(' +', ' ',logradouro_aprova).split(' ')
        logradouro_google = "+".join(endereço_split)
        st.markdown('MAPS: '+str('https://www.google.com/maps/place/')+logradouro_google+str(',+')+str(numero_aprova)+str('+,+Itaja%C3%AD+-+SC'))
        st.markdown('VIABILIDADE: '+str('https://geoitajai.github.io/geo/consultaalvara.html#')+inscricao_aprova[0:3]+inscricao_aprova[4:7]+inscricao_aprova[11:15])
        
        #Printa a verificação do cnpj
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação do CNPJ')

        if (numero_cnpj[0] == cnpj_aprova[0]):
            st.text('Ok! Número CNPJ inserido corretamente no Aprova.')
        else:
            st.text('VERIFICAR! Número CNPJ NÃO coincide')

        #Printa a verificação da razão social
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação da RAZÃO SOCIAL')
        if (razao_social_cnpj == razao_social_aprova.upper()):
            st.text('Ok! A razão social inserida corretamento no Aprova.')
        else:
            st.text('VERIFICAR! A razão social NÃO coincide com o Aprova.')
                
        #Printa a verificação do endereço
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação do ENDEREÇO')
        st.text('** Verifique manualmente os endereços abaixo:')
        st.text('Endereço no APROVA: '+logradouro_aprova+', '+bairro_aprova+', '+numero_aprova+', '+complemento1_aprova+', '+complemento2_aprova+', '+complemento3_aprova)
        st.text('Endereço no CNPJ: '+logradouro_cnpj+', '+bairro_cnpj+', '+numeropredial_cnpj+', '+complemento_cnpj)
        st.text('Endereço no REGIN: '+endereco_regin)

        #Printa a verificação dos cnaes
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação dos CNAES')

        if (set(cnaes_cnpj) == set(cnaes_formatados_regin)):
             st.text('Conferência dos CNAEs do CNPJ com o REGIN: Ok! CNAES coincidem.')
        else:
            st.text('Conferência dos CNAEs do CNPJ com o REGIN: VERIFICAR! CNAES não coincidem.')

        if (set(cnaes_cnpj) == set(cnaes_aprova)):
             st.text('Conferência dos CNAEs do CNPJ com o APROVA: Ok! CNAES coincidem.')
        else:
            st.text('Conferência dos CNAEs do CNPJ com o APROVA: VERIFICAR! CNAES não coincidem.')
                
        if (set(cnaes_formatados_regin) == set(cnaes_aprova)):
            st.text('Conferência dos CNAEs do APROVA com o REGIN: Ok! CNAES coincidem.')
        else:
            st.text('Conferência dos CNAEs do APROVA com o REGIN: VERIFICAR! CNAES não coincidem.')

        st.text('ATENÇÃO! Verifique manualmente se não houve inserção REPETIDA de CNAES no Aprova Digital. Abaixo o número de atividades por valores únicos (exclui repetidos)')
        nome_contagem = pd.Series(['Aprova Digital', 'Cartão CNPJ', 'REGIN'])      
        n_cnaes=([len(cnaes_aprova),len(cnaes_cnpj),len(cnaes_formatados_regin)])
        st.dataframe({'LOCAL':nome_contagem,'Nº DE CNAES':n_cnaes})

            
        if (set(cnaes_formatados_regin) == set(cnaes_aprova)):
            st.text('TABELA DE CNAES')
            tabela_cnaes = pd.DataFrame({ 'CNAES APROVA': cnaes_aprova, 'CNAES CNPJ': cnaes_cnpj, 'CNAES REGIN': cnaes_formatados_regin })
            st.dataframe(tabela_cnaes)
        else:
            st.text('   ** CNAE principal: '+cnaes_cnpj[0])
            st.text('   ** CNAES não inseridos no APROVA: '+str(set(cnaes_cnpj)-set(cnaes_aprova)))
            verif_cnaes = set(cnaes_aprova)-set(cnaes_cnpj)
            if verif_cnaes == set():
                verif_cnaes = ""
            st.text('   ** CNAES inseridos no APROVA que não estão no CNPJ: '+str(verif_cnaes))
            st.text('CNAES do APROVA')
            st.dataframe(cnaes_aprova)
            st.text('CNAES do CNPJ')
            st.dataframe(cnaes_cnpj)
            st.text('CNAES do REGIN')
            st.dataframe(cnaes_formatados_regin)
            
        #Printa verificação REGIN
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação do REGIN')
        
        st.text('DESPACHO REGIN:')
        st.text(str(despacho_regin))
        
        despacho_regin_split = re.sub(' +', ' ',despacho_regin).split(' ')
        
        EV = 'COMPARTILHADO'
        if EV in despacho_regin_split:
            st.text('*** ESCRITÓRIO VIRTUAL.')
       
        REF = 'REFERÊNCIA'
        if REF in despacho_regin_split:
            st.text('*** REFERÊNCIA FISCAL EM RESIDÊNCIA')
        
        LIC = 'Licenciamento'
        if LIC in despacho_regin_split:
            st.text('*** LICENCIAMENTO AMBIENTAL.')
           
        PAR = 'PARECER'
        if PAR in despacho_regin_split:
            st.text('*** PARECER DA DEFESA CIVIL.')
            
        ESC = 'ESCRITÓRIO'
        if ESC in despacho_regin_split:
            st.text('*** DECLARAÇÃO DE ESCRITÓRIO.')
        
        COM = 'COMED'
        if COM in despacho_regin_split:
            st.text('*** COMED.')
            
        cnove = '9'
        cdez = '10'
        cnovedois = '9-'
        cdezdois = '10-'
        
        if (cnove or cnovedois or cdez or cdezdois) in despacho_regin_split:
            st.text('*** DOCUMENTOS/ SOLICITAÇÕES COMPLEMENTARES. (CAMPOS 9 E 10) ')

        #Printa outras verificações
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação de documentos complementares')
        
        #Tabelas com CNAES
        
        tabela_cnaes = pd.read_csv('./dados/grau_risco_maio_2021.xlsx - Página2.csv', sep=',')       
        cnaes_cnpj = pd.DataFrame(cnaes_cnpj)
        
        nova_tabela=tabela_cnaes.merge(cnaes_cnpj,left_on='codigo', right_on=0)
        nova_tabela.drop([0], axis=1, inplace=True)
        nova_tabela
        
        #Verificação armas de fogo
        
        cnae1 = '47.89-0-09'
        if cnae1 in cnaes_aprova:
            st.text('*** APRESENTA CNAE para comércio de ARMAS DE FOGO, solicitar documentação extra.')
        if cnae1 not in cnaes_aprova:
            st.text('*** NÃO apresenta CNAE para comércio de armas de fogo.')     
            
        #Verificação SPE
        
        cnae2 = '41.10-7-00'      
        cnae3 = '41.20-4-00'
        
        if (cnae2 or cnae3) in cnaes_aprova:
           st.text('*** APRESENTA CNAE para construção ou incorporação, verificar se é uma SPE.')
        if (cnae2 or cnae3) not in cnaes_aprova:
           st.text('*** NÃO apresenta CNAE para incorporação imobiliária ou construção (SPE).')

        #Verificação transporte escolar
        
        cnae4 = '49.24-8-00'
        if cnae4 in cnaes_cnpj:
            st.text('*** APRESENTA CNAE para TRANSPORTE ESCOLAR, solicitar documentação extra.')
        if cnae4 not in cnaes_cnpj:
            st.text('*** NÃO apresenta CNAE para transporte escolar.')
            
        #Verificação transporte por cabotagem
        cnae5 = '50.11-4-02'
        if cnae5 in cnaes_cnpj:
            st.text('*** APRESENTA CNAE para transporte por CABOTAGEM, solicitar autorização da ANTAC.')
        if cnae5 not in cnaes_cnpj:
            st.text('*** NÃO apresenta CNAE para transporte de cabotagem.')
               
        #Printa outras verificações
        st.text('____________________________________________________________________________________________________________')
        st.subheader('Verificação do grau de risco')
     
        tabela_risco = pd.read_csv('./dados/Decreto 11.985 - Grau de risco.csv', sep=',')
          
        cnaes_cnpj = pd.DataFrame(cnaes_cnpj)        
        nova_tabela3=tabela_risco.merge(cnaes_cnpj,left_on='CÓDIGO', right_on=0)
        nova_tabela3.drop([0], axis=1, inplace=True)
        nova_tabela3
     
        
        
except:
  pass

