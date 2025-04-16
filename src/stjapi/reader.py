import pandas as pd
import json
import numpy as np
from time import strftime, gmtime
from typing import Optional

class STJLer:
    
    def __init__(self, filename: str):
        """
        Read data from a JSON file on disk.
        
        Args:
            filename: Name of the file (without path or extension)
            
        Returns:
            str: Dict with all dataframes
        """
        
        #self.read_dir = read_dir,
        self.filename = filename
        
    def safe_get(self, dictionary, *keys, default=None):
        """
        Safely navigate nested dictionaries, returning default if any key is missing
        """
        for key in keys:
            if isinstance(dictionary, dict):
                dictionary = dictionary.get(key, {})
            else:
                return default
        return dictionary if dictionary != {} else default

    # Function to create DataFrames for each table
    def create_dataframes(self):

        filepath = self.filename

        with open(filepath, 'r') as file:
            data = json.load(file)
        
        process_data = data["list"][0]
        
        data_situacao1 = ''.join(x for x in filepath.split('_time_')[1] if x.isnumeric())

        data_situacao = strftime('%Y-%m-%d', gmtime(int(data_situacao1)))
        
        dataframes = {}

        # Tabela processo
        processo_data = {
            'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
            'numeroRegistroFormatado': self.safe_get(process_data, 'numeroRegistroFormatado'),
            'codigoClasse': self.safe_get(process_data, 'classe', 'codigo'),
            'numeroProcessoClasse': self.safe_get(process_data, 'numeroProcessoClasse'),
            'qtdVolumes': self.safe_get(process_data, 'qtdVolumes'),
            'qtdApensos': self.safe_get(process_data, 'qtdApensos'),
            'dataRegistroProtocolo': self.safe_get(process_data, 'dataRegistroProtocolo'),
            'dataAutuacao': self.safe_get(process_data, 'dataAutuacao'),
            'justicaGratuita': self.safe_get(process_data, 'justicaGratuita'),
            'originario': self.safe_get(process_data, 'originario'),
            'segredoJustica': self.safe_get(process_data, 'segredoJustica'),
            'agravoSTF': self.safe_get(process_data, 'agravoSTF'),
            'criminal': self.safe_get(process_data, 'criminal'),
            'criminalCorte': self.safe_get(process_data, 'criminalCorte'),
            'prioridade': self.safe_get(process_data, 'prioridade'),
            'codigoCompetencia': self.safe_get(process_data, 'codigoCompetencia'),
            'numeroUnico': self.safe_get(process_data, 'numeroUnico'),
            'numeroUnicoFormatado': self.safe_get(process_data, 'numeroUnicoFormatado'),
            'codigoClasseAnterior': self.safe_get(process_data, 'codigoClasseAnterior'),
            'numeroClasseAnterior': self.safe_get(process_data, 'numeroClasseAnterior'),
            'numeroRegistroVinculante': self.safe_get(process_data, 'numeroRegistroVinculante'),
            'codigoOrigem': self.safe_get(process_data, 'origem', 'codigo'),
            'tipo': self.safe_get(process_data, 'tipo'),
            'processoFisico': self.safe_get(process_data, 'processoFisico'),
            'processoEletronico': self.safe_get(process_data, 'processoEletronico'),
            'preferencial': self.safe_get(process_data, 'preferencial'),
            'sigiloso': self.safe_get(process_data, 'sigiloso'),
            'nivelSigilo': self.safe_get(process_data, 'nivelSigilo'),
            'pais': self.safe_get(process_data, 'pais'),
            'codigoDestino': self.safe_get(process_data, 'destino', 'codigo'),
            'codigoStatus': self.safe_get(process_data, 'status', 'codigo'),
            'numerosConexo': self.safe_get(process_data, 'numerosConexo'),
            'nomeLocalOrigem': self.safe_get(process_data, 'nomeLocalOrigem'),
            'numeroOrigemProtocolo': self.safe_get(process_data, 'numeroOrigemProtocolo'),
            'observacaoProcesso': self.safe_get(process_data, 'observacaoProcesso'),
            'pedidoLiminar': self.safe_get(process_data, 'pedidoLiminar'),
            'recolheuCusta': self.safe_get(process_data, 'recolheuCusta'),
            'nome': self.safe_get(process_data, 'nome'),
            'nomeCompleto': self.safe_get(process_data, 'nomeCompleto'),
            'nomeUf': self.safe_get(process_data, 'nomeUf'),
            'uf': self.safe_get(process_data, 'uf'),
            'parteAutora': self.safe_get(process_data, 'parteAutora'),
            'tipoParteAutora': self.safe_get(process_data, 'tipoParteAutora'),
            'parteRe': self.safe_get(process_data, 'parteRe'),
            'tipoParteRe': self.safe_get(process_data, 'tipoParteRe'),
            'ministro': self.safe_get(process_data, 'ministro'),
            'codigoAssuntoCNJ': self.safe_get(process_data, 'codigoAssuntoCNJ'),
            'local': self.safe_get(process_data, 'local', 'seq'),
            'documentos': self.safe_get(process_data, 'documentos'),
            'representativoControversia': self.safe_get(process_data, 'representativoControversia'),
            'repetitivo': self.safe_get(process_data, 'repetitivo'),
            'valorCausa': self.safe_get(process_data, 'valorCausa'),
            'dataSituacao': data_situacao
        }
        
        dataframes['Processo'] = pd.DataFrame([processo_data])
        
        # Adding the additional tables from the standalone function
        
        # Decisao Table
        decisoes = self.safe_get(process_data, 'decisoes', default=[])
        if decisoes:
            decisao_data = []
            for decisao in decisoes:
                decisao_entry = {
                    'codigo': self.safe_get(decisao, 'seq'),
                    'numeroPeticao': self.safe_get(decisao, 'numeroPeticao'),
                    'codigoTipoDocumento': self.safe_get(decisao, 'tipoDocumento', 'codigo'),
                    'dataConfirmacaoPublicacao': self.safe_get(decisao, 'dataConfirmacaoPublicacao'),
                    'nome': self.safe_get(decisao, 'nome'),
                    'julgamentoEletronico': self.safe_get(decisao, 'julgamentoEletronico')
                }
                decisao_data.append({k: v for k, v in decisao_entry.items() if v is not None})
            
            if decisao_data:
                dataframes['Decisao'] = pd.DataFrame(decisao_data)

        # Fases Table
        fases = self.safe_get(process_data, 'fases', default=[])
        if fases:
            fases_data = []
            for fase in fases:
                fase_entry = {
                    'codigo': self.safe_get(fase, 'seq'),
                    'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                    'dataHoraFase': self.safe_get(fase, 'dataHoraFase'),
                    'textoFase': self.safe_get(fase, 'textoFase'),
                    'descricaoSimplificada': self.safe_get(fase, 'descricaoSimplificada')
                }
                fases_data.append({k: v for k, v in fase_entry.items() if v is not None})
            
            if fases_data:
                dataframes['Fases'] = pd.DataFrame(fases_data)

        # Partes Table
        partes = self.safe_get(process_data, 'partesAdvogados', default=[])
        if partes:
            partes_data = []
            for parte in partes:
                parte_entry = {
                    'siglaTipoParte': self.safe_get(parte, 'siglaTipoParte'),
                    'indicadorAutorReu': self.safe_get(parte, 'indicadorAutorReu'),
                    'codigoTipoParte': self.safe_get(parte, 'codigoTipoParte'),
                    'codigoOAB': self.safe_get(parte, 'codigoOAB'),
                    'nome': self.safe_get(parte, 'nome'),
                    'cpfCnpj': self.safe_get(parte, 'cpfCnpj'),
                    'codigo': self.safe_get(parte, 'seq'),
                    'seqParteProcesso': self.safe_get(parte, 'seqParteProcesso'),
                    'tipo': self.safe_get(parte, 'tipo'),
                    'descricaoTipoParte': self.safe_get(parte, 'descricaoTipoParte'),
                    'sexoParte': self.safe_get(parte, 'sexoParte')
                }
                partes_data.append({k: v for k, v in parte_entry.items() if v is not None})
            
            if partes_data:
                dataframes['Partes'] = pd.DataFrame(partes_data)

        # Classe Table
        classe = self.safe_get(process_data, 'classe')
        if classe:
            classe_data = {
                'codigo': self.safe_get(classe, 'codigo'),
                'sigla': self.safe_get(classe, 'sigla'),
                'codigoClasseEmbargada': self.safe_get(classe, 'codigoClasseEmbargada', default=0),
                'nome': self.safe_get(classe, 'nomeClasse')
            }
            dataframes['Classe'] = pd.DataFrame([{k: v for k, v in classe_data.items() if v is not None}])

        # Status Table
        status = self.safe_get(process_data, 'status')
        if status:
            status_data = {
                'codigo': self.safe_get(status, 'codigo'),
                'descricao': self.safe_get(status, 'descricao'),
                'tramitando': self.safe_get(status, 'tramitando')
            }
            dataframes['Status'] = pd.DataFrame([{k: v for k, v in status_data.items() if v is not None}])

        # Números de Origem
        numeros_origem = self.safe_get(process_data, 'numerosOrigem', default=[])
        if numeros_origem:
            numeros_origem_data = []
            for numero in numeros_origem:
                origem_entry = {
                    'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                    'numerosOrigem': self.safe_get(numero, 'numeroProcessoOrigem')
                }
                numeros_origem_data.append({k: v for k, v in origem_entry.items() if v is not None})
            
            if numeros_origem_data:
                dataframes['NumerosOrigemProcesso'] = pd.DataFrame(numeros_origem_data)

        return dataframes