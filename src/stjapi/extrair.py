import pandas as pd
import json
import numpy as np

# Function to create DataFrames for each table
def create_dataframes(process_data):
    dataframes = {}

    # Processo Table
    processo_data = {
        'numeroRegistro': process_data.get('numeroRegistro'),
        'numeroRegistroFormatado': process_data.get('numeroRegistroFormatado'),
        'codigoClasse': process_data.get('classe', {}).get('codigo'),
        'numeroProcessoClasse': process_data.get('numeroProcessoClasse'),
        'qtdVolumes': process_data.get('qtdVolumes'),
        'qtdApensos': process_data.get('qtdApensos'),
        'dataRegistroProtocolo': process_data.get('dataRegistroProtocolo'),
        'dataAutuacao': process_data.get('dataAutuacao'),
        'justicaGratuita': process_data.get('justicaGratuita'),
        'originario': process_data.get('originario'),
        'segredoJustica': process_data.get('segredoJustica'),
        'agravoSTF': process_data.get('agravoSTF'),
        'criminal': process_data.get('criminal'),
        'criminalCorte': process_data.get('criminalCorte'),
        'prioridade': process_data.get('prioridade'),
        'codigoCompetencia': process_data.get('codigoCompetencia'),
        'numeroUnico': process_data.get('numeroUnico'),
        'numeroUnicoFormatado': process_data.get('numeroUnicoFormatado'),
        'codigoClasseAnterior': process_data.get('codigoClasseAnterior'),
        'numeroClasseAnterior': process_data.get('numeroClasseAnterior'),
        'numeroRegistroVinculante': process_data.get('numeroRegistroVinculante'),
        'codigoOrigem': process_data.get('origem', {}).get('codigo'),
        'tipo': process_data.get('tipo'),
        'processoFisico': process_data.get('processoFisico'),
        'processoEletronico': process_data.get('processoEletronico'),
        'preferencial': process_data.get('preferencial'),
        'sigiloso': process_data.get('sigiloso'),
        'nivelSigilo': process_data.get('nivelSigilo'),
        'pais': process_data.get('pais'),
        'codigoDestino': process_data.get('destino', {}).get('codigo'),
        'codigoStatus': process_data.get('status', {}).get('codigo'),
        'numerosConexo': process_data.get('numerosConexo'),
        'nomeLocalOrigem': process_data.get('nomeLocalOrigem'),
        'numeroOrigemProtocolo': process_data.get('numeroOrigemProtocolo'),
        'observacaoProcesso': process_data.get('observacaoProcesso'),
        'pedidoLiminar': process_data.get('pedidoLiminar'),
        'recolheuCusta': process_data.get('recolheuCusta'),
        'nome': process_data.get('nome'),
        'nomeCompleto': process_data.get('nomeCompleto'),
        'nomeUf': process_data.get('nomeUf'),
        'uf': process_data.get('uf'),
        'parteAutora': process_data.get('parteAutora'),
        'tipoParteAutora': process_data.get('tipoParteAutora'),
        'parteRe': process_data.get('parteRe'),
        'tipoParteRe': process_data.get('tipoParteRe'),
        'ministro': process_data.get('ministro'),
        'codigoAssuntoCNJ': process_data.get('codigoAssuntoCNJ'),
        'local': process_data.get('local', {}).get('seq') if process_data.get('local') else None,
        'documentos': None,  # Not available in the JSON
        'representativoControversia': process_data.get('representativoControversia'),
        'repetitivo': process_data.get('repetitivo'),
        'valorCausa': process_data.get('valorCausa')
    }
    dataframes['Processo'] = pd.DataFrame([processo_data])

    # Decisao Table
    if process_data.get('decisoes'):
        decisao_data = process_data['decisoes'][0]
        decisao_df = pd.DataFrame([{
            'codigo': decisao_data.get('seq'),
            'numeroPeticao': decisao_data.get('numeroPeticao'),
            'tipoDespacho': None,
            'codigoTipoDocumento': decisao_data.get('tipoDocumento', {}).get('codigo'),
            'ministro': decisao_data.get('ministro'),
            'dataConfirmacaoPublicacao': decisao_data.get('dataConfirmacaoPublicacao'),
            'nome': decisao_data.get('nome'),
            'seqInteiroTeor': decisao_data.get('seqInteiroTeor'),
            'julgamentoEletronico': decisao_data.get('julgamentoEletronico'),
            'indTipoEditor': decisao_data.get('indTipoEditor'),
            'decisao': decisao_data.get('decisao')
        }])
        dataframes['Decisao'] = decisao_df

    # Fases Table
    if process_data.get('fases'):
        fases_data = []
        for fase in process_data['fases']:
            fases_data.append({
                'codigo': fase.get('seq'),
                'numeroRegistro': process_data.get('numeroRegistro'),
                'dataHoraFase': fase.get('dataHoraFase'),
                'textoFase': fase.get('textoFase'),
                'descricaoSimplificada': fase.get('descricaoSimplificada')
            })
        dataframes['Fases'] = pd.DataFrame(fases_data)

    # Partes Table
    if process_data.get('partesAdvogados'):
        partes_data = []
        for parte in process_data['partesAdvogados']:
            partes_data.append({
                'siglaTipoParte': parte.get('siglaTipoParte'),
                'indicadorAutorReu': parte.get('indicadorAutorReu'),
                'codigoTipoParte': parte.get('codigoTipoParte'),
                'codigoOAB': parte.get('codigoOAB'),
                'nome': parte.get('nome'),
                'cpfCnpj': parte.get('cpfCnpj'),
                'codigo': parte.get('seq'),
                'seqParteProcesso': parte.get('seqParteProcesso'),
                'tipo': parte.get('tipo'),
                'codTipoEnte': parte.get('codTipoEnte'),
                'descricaoTipoParte': parte.get('descricaoTipoParte'),
                'numeroOrdemParte': parte.get('numeroOrdemParte'),
                'descricaoTipoParteFem': parte.get('descricaoTipoParteFem'),
                'sexoParte': parte.get('sexoParte')
            })
        dataframes['Partes'] = pd.DataFrame(partes_data)

    # Local Table
    local_data = []
    if process_data.get('local'):
        local_data.append({
            'codigoLocal': process_data['local'].get('seq'),
            'nomeLocal': process_data['local'].get('nomeLocal')
        })
    if process_data.get('deslocamento', {}).get('localEntrada'):
        local_data.append({
            'codigoLocal': process_data['deslocamento']['localEntrada'].get('seq'),
            'nomeLocal': process_data['deslocamento']['localEntrada'].get('nomeLocal')
        })
    if process_data.get('deslocamento', {}).get('localSaida'):
        local_data.append({
            'codigoLocal': process_data['deslocamento']['localSaida'].get('seq'),
            'nomeLocal': process_data['deslocamento']['localSaida'].get('nomeLocal')
        })
    if local_data:
        dataframes['Local'] = pd.DataFrame(local_data).drop_duplicates(subset='codigoLocal')

    # Deslocamento Table
    if process_data.get('deslocamento'):
        deslocamento_data = {
            'codigo': process_data['deslocamento'].get('seq'),
            'numeroRegistro': process_data.get('numeroRegistro'),
            'localEntradaSeq': process_data['deslocamento'].get('localEntrada', {}).get('seq'),
            'localSaidaSeq': process_data['deslocamento'].get('localSaida', {}).get('seq'),
            'dataEntrada': process_data['deslocamento'].get('dataEntrada'),
            'dataSaida': process_data['deslocamento'].get('dataSaida')
        }
        dataframes['Deslocamento'] = pd.DataFrame([deslocamento_data])

    # Origem Table
    if process_data.get('origem'):
        origem_data = {
            'codigo': process_data['origem'].get('codigo'),
            'nome': process_data['origem'].get('nome'),
            'sigla': process_data['origem'].get('sigla')
        }
        dataframes['Origem'] = pd.DataFrame([origem_data])

    # Ministro Relator Table
    if process_data.get('ministroRelator'):
        ministro_data = []
        for ministro in process_data['ministroRelator']:
            ministro_data.append({
                'numMinistro': ministro.get('ministro', {}).get('numMinistro'),
                'nomeMinistro': ministro.get('ministro', {}).get('nomeMinistro'),
                'sexoMinistro': ministro.get('ministro', {}).get('sexoMinistro'),
                'codigoTipoMinistro': ministro.get('codigoTipoMinistro')
            })
        dataframes['MinistroRelator'] = pd.DataFrame(ministro_data)

    # Assunto Table
    if process_data.get('assunto'):
        assunto_data = {
            'codigo': process_data['assunto'].get('seq'),
            'descAssunto': process_data['assunto'].get('descAssunto'),
            'descricao': process_data['assunto'].get('descricao'),
            'descricaoCompleta': process_data['assunto'].get('descricaoCompleta'),
            'codigoAreaEspecializacao': process_data['assunto'].get('areaEspecializacao', {}).get('codigoAreaEspecializacao'),
            'nomeAreaEspecializacao': process_data['assunto'].get('areaEspecializacao', {}).get('nomeAreaEspecializacao'),
            'segredoJustica': process_data['assunto'].get('segredoJustica')
        }
        dataframes['Assunto'] = pd.DataFrame([assunto_data])
    

    # Classe Table
    if process_data.get('classe'):
        classe_data = {
            'codigo': process_data['classe'].get('codigo'),
            'sigla': process_data['classe'].get('sigla'),
            'codigoClasseEmbargada': process_data['classe'].get('codigoClasseEmbargada'),
            'nome': process_data['classe'].get('nomeClasse')
        }
        dataframes['Classe'] = pd.DataFrame([classe_data])

    # Status Table
    if process_data.get('status'):
        status_data = {
            'codigo': process_data['status'].get('codigo'),
            'descricao': process_data['status'].get('descricao'),
            'tramitando': process_data['status'].get('tramitando')
        }
        dataframes['Status'] = pd.DataFrame([status_data])

    # Destino Table
    if process_data.get('destino'):
        destino_data = {
            'codigo': process_data['destino'].get('codigo'),
            'descricao': process_data['destino'].get('descricao')
        }
        dataframes['Destino'] = pd.DataFrame([destino_data])

    # Números de Origem
    if process_data.get('numerosOrigem'):
        numeros_origem_data = []
        for numero in process_data['numerosOrigem']:
            numeros_origem_data.append({
                'numeroRegistro': process_data.get('numeroRegistro'),
                'numerosOrigem': numero.get('numeroProcessoOrigem')
            })
        dataframes['NumerosOrigemProcesso'] = pd.DataFrame(numeros_origem_data)

    # Órgão Julgador
    if process_data.get('orgaoJulgador'):
        orgao_julgador_data = {
            'codigo': process_data['orgaoJulgador'].get('codigo'),
            'nome': process_data['orgaoJulgador'].get('nome')
        }
        dataframes['OrgaoJulgador'] = pd.DataFrame([orgao_julgador_data])

    # Órgão Processante
    if process_data.get('orgaoProcessante'):
        orgao_processante_data = {
            'codigo': process_data['orgaoProcessante'].get('codigo'),
            'nome': process_data['orgaoProcessante'].get('nome')
        }
        dataframes['OrgaoProcessante'] = pd.DataFrame([orgao_processante_data])

    # Forma de Distribuição
    if process_data.get('formaDistribuicao'):
        forma_distribuicao_data = {
            'codigo': process_data['formaDistribuicao'].get('codigo'),
            'descricao': process_data['formaDistribuicao'].get('descricao')
        }
        dataframes['formaDistribuicao'] = pd.DataFrame([forma_distribuicao_data])

    # Tipo de Distribuição
    if process_data.get('tipoDistribuicao'):
        tipo_distribuicao_data = {
            'codigo': process_data['tipoDistribuicao'].get('codigo'),
            'descricao': process_data['tipoDistribuicao'].get('descricao')
        }
        dataframes['tipoDistribuicao'] = pd.DataFrame([tipo_distribuicao_data])

    # Tipo de Documento de Decisão
    if process_data.get('decisoes') and process_data['decisoes'][0].get('tipoDocumento'):
        tipo_documento_decisao_data = {
            'codigo': process_data['decisoes'][0]['tipoDocumento'].get('codigo'),
            'descricao': process_data['decisoes'][0]['tipoDocumento'].get('descricao')
        }
        dataframes['TipoDocumentoDecisao'] = pd.DataFrame([tipo_documento_decisao_data])


    return dataframes

