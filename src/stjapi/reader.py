import pandas as pd
import json
import numpy as np
from datetime import datetime
from typing import Optional
import re

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
    
    def add_fk_table(self, column_name, column, default = None):
        pdf = pd.DataFrame({column_name: column})
        pdf['numeroRegistro'] = self.process_data['numeroRegistro']
        return pdf
    
    def get_branch(self, x):
        
        try:
            return  x.split("-")[0].strip()
        except:
            return None
    
    def is_mp(self, x):
        regex = '(?i)(minist[ée]rio\\s+p[úu]blico|procurador.+justi[çc]a).+s.o\\s+paulo'
        return bool(re.search(regex, x))   
         
    def create_dataframes(self):

        filepath = self.filename

        with open(filepath, 'r') as file:
            data = json.load(file)
        
        process_data = data["list"][0]
        # Store the process_data as an instance attribute so it can be accessed by other methods
        self.process_data = process_data
        
        data_situacao1 = ''.join(x for x in filepath.split('_time_')[1] if x.isnumeric())

        data_situacao = datetime.fromtimestamp(int(data_situacao1)).strftime('%Y-%m-%d')
        
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
            'dataSituacao': data_situacao,
            'codigoRelator': self.safe_get(process_data, 'ministroRelator'  ,'numMinistro'),
            'codigoAssunto': self.safe_get(process_data, 'assunto','seq')
        }
        
        dataframes['Processo'] = pd.DataFrame([processo_data])
                
        # Tabela Decisao
        decisoes = self.safe_get(process_data, 'decisoes', default=[])
        if decisoes:
            decisao_data = []
            for decisao in decisoes:
                decisao_entry = {
                    'numeroRegistro': self.safe_get(process_data,'numeroRegistro'),
                    'codigo': self.safe_get(decisao, 'seq'),
                    'numeroPeticao': self.safe_get(decisao, 'numeroPeticao'),
                    'tipoDespacho': self.safe_get(decisao, 'tipoDespacho'),
                    'codigoTipoDocumento': self.safe_get(decisao, 'tipoDocumento', 'codigo'),
                    'ministro': self.safe_get(decisao, 'ministro'),
                    'dataConfirmacaoPublicacao': self.safe_get(decisao, 'dataConfirmacaoPublicacao'),
                    'nome': self.safe_get(decisao, 'nome'),
                    'seqInteiroTeor': self.safe_get(decisao, 'seqInteiroTeor'),
                    'julgamentoEletronico': self.safe_get(decisao, 'julgamentoEletronico'),
                    'indTipoEditor': self.safe_get(decisao, "indTipoEditor"),
                    'decisao': self.safe_get(decisao, 'decisao')
                }
                decisao_data.append({k: v for k, v in decisao_entry.items() if v is not None})
            
            if decisao_data:
                df = pd.DataFrame(decisao_data)
                df['dataConfirmacaoPublicacao']   = pd.to_datetime(df['dataConfirmacaoPublicacao'])
                dataframes['ProcessoDecisao'] = df

        # Tabela TipoDocumentoDecisao 
        if decisoes:
            tipo_documento_data = []
            
            for tp in decisoes:
                tipo_documento = {
                    'codigo': self.safe_get(tp, 'tipoDocumento','codigo'),
                    'descricao': self.safe_get(tp,'tipoDocumento','descricao')
                }
            
                tipo_documento_data.append({k: v for k, v in tipo_documento.items() if v is not None})

            if tipo_documento_data:
                dataframes['TipoDocumentoDecisao'] = pd.DataFrame(tipo_documento_data)

        # Tabela ProcessoDecisao
       # if decisoes and 'Decisao' in dataframes:
            
        #    dataframes['ProcessoDecisao'] =  self.add_fk_table('codigo', dataframes['Decisao']['codigo'])

        ## Tabela Peticoes
        peticoes = self.safe_get(process_data, 'peticoes', default = [])
        
        if peticoes:
            peticoes_data = []
            for peticao in peticoes:
                peticao_entry  = {
                    'numero': self.safe_get(peticao, 'numero'),
                    'dataProtocolo': self.safe_get(peticao,'dataProtocolo'),
                    'descTipoPeticao': self.safe_get(peticao, 'descTipoPeticao'),
                    'partePeticionante': self.safe_get(peticao, 'partePeticionante'),
                    'status': self.safe_get(peticao, 'status')
                }
                peticoes_data.append({k: v for k, v in peticao_entry.items() if v is not None})     
            if peticoes_data:
                df = pd.DataFrame(peticoes_data)
                df['dataProtocolo']= pd.to_datetime(df['dataProtocolo'])
                dataframes['Peticoes'] = df
        
        # Tabela ProcessoPeticoes
        if peticoes and 'Peticoes' in dataframes:
            dataframes['ProcessoPeticoes'] = self.add_fk_table('numeroPeticao', dataframes['Peticoes']['numero'])

        # Tabela Partes
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
                    'sexoParte': self.safe_get(parte, 'sexoParte'),
                    'mpsp': self.is_mp(self.safe_get(parte, 'nome'))
                }
                partes_data.append({k: v for k, v in parte_entry.items() if v is not None})
            
            if partes_data:
                dataframes['Partes'] = pd.DataFrame(partes_data)

        if partes and 'Partes' in dataframes:
           dataframes['ProcessoPartes'] = self.add_fk_table('codigoParte', dataframes['Partes']['codigo'])
           

            
        # Tabela Fases
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

        # Tabela Local
        local = self.safe_get(process_data, 'local', default = [])
        if local:
            local_data = {
                "codigoLocal": self.safe_get(local,'seq'),
                "nomeLocal": self.safe_get(local, 'nomeLocal')
            }
            dataframes['Local'] = pd.DataFrame([{k: v for k, v in local_data.items() if v is not None}])

        # Tabela LocalProcesso
        if local and 'Local' in dataframes:
           dataframes['LocalProcesso'] = self.add_fk_table('codigoLocal', dataframes['Local']['codigoLocal'])

        # Tabela Deslocamento
        deslocamento = self.safe_get(process_data, "deslocamento", default = [])
        
        if deslocamento:
            deslocamento_data = {
                "codigo": self.safe_get(deslocamento, 'seq'),
                "numeroRegistro": self.safe_get(process_data,'numeroRegistro'),
                "localEntradaSeq": self.safe_get(deslocamento,"localEntrada","seq"),
                "localSaidaSeq": self.safe_get(deslocamento, "localSaida","seq"),
                "dataEntrada": self.safe_get(deslocamento, "dataEntrada"),
                "dataSaida": self.safe_get(deslocamento,"dataSaida")
            }
            
            if deslocamento_data:
                df = pd.DataFrame([{k: v for k, v in deslocamento_data.items() if v is not None}])
                try:
                    df['dataEntrada']= pd.to_datetime(df['dataEntrada'])
                except:
                    pass
                try:
                    df['dataSaida']= pd.to_datetime(df['dataSaida'])
                except:
                    pass
                dataframes['Deslocamento'] = df
        
        
        
        # Tabela ProcessoFavorito
        
        processoFavorito = self.safe_get(process_data, 'processoFavorito')
        
        if processoFavorito: 
            processoFavorito_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'numeroRegistroFavorito': self.safe_get(processoFavorito, 'numeroRegistro', default = None),
                'seqProcessoFavorito': self.safe_get(processoFavorito,'seqProcessoFavorito', default = None)
            }
            dataframes['ProcessoFavorito'] = pd.DataFrame([{k: v for k, v in processoFavorito_data.items() if v is not None}])

         # Tabela MinistroRelator
        ministroRelator = self.safe_get(process_data, 'ministroRelator', default=[])
        
        if ministroRelator:
            ministro_relator_data = []
            for relator in ministroRelator:
                ministro_entry = {
                    'numMinistro': self.safe_get(relator, 'ministro','numMinistro'),
                    'nomeMinistro': self.safe_get(relator,'ministro', 'nomeMinistro'),
                    'sexoMinistro': self.safe_get(relator,"ministro", 'sexoMinistro'),
                    'codigoTipoMinistro': self.safe_get(relator, 'codigoTipoMinistro')
                }
                
                ministro_relator_data.append({k: v for k, v in ministro_entry.items() if v is not None})
            
            if ministro_relator_data:
                dataframes['MinistroRelator'] = pd.DataFrame(ministro_relator_data)

        ## Tabela MinistroRelatorProcesso
        
        if ministroRelator and 'MinistroRelator' in dataframes:
            
           dataframes['MinistroRelatorProcesso'] = self.add_fk_table('numMinistro', dataframes['MinistroRelator']['numMinistro'])


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

        # Tabela NumerosOrigemProcesso
        
        numeros_origem = self.safe_get(process_data, 'numerosOrigem', default=[])
        if numeros_origem:
            numeros_origem_data = []
            for numero in numeros_origem:
                origem_entry = {
                    'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                    'numerosOrigem': self.safe_get(numero, 'numeroProcessoOrigem'),
                    'numOrdem': self.safe_get(numero,'numOrdem')
                }
                numeros_origem_data.append({k: v for k, v in origem_entry.items() if v is not None})
            
            if numeros_origem_data:
                dataframes['NumerosOrigemProcesso'] = pd.DataFrame(numeros_origem_data)
        
        # Tabela Origem   
        origem = self.safe_get(process_data, 'origem')
        
        if origem:
            origem_data = {
                'codigo': self.safe_get(origem, 'codigo'),
                'nome': self.safe_get(origem, 'nome'),
                'sigla': self.safe_get(origem, 'sigla')
            }
            dataframes['Origem'] = pd.DataFrame([{k: v for k, v in origem_data.items() if v is not None}])

        # Tabela Destino
        destino = self.safe_get(process_data, 'destino')
        
        if destino:
            destino_data = {
                'codigo': self.safe_get(destino, 'codigo'),
                'descricao': self.safe_get(destino, 'descricao')
            }
            dataframes['Destino'] = pd.DataFrame([{k: v for k, v in destino_data.items() if v is not None}])


        # Tabela Assunto
        assunto = self.safe_get(process_data, 'assunto')
        
        
        if assunto:
            assunto_data = {
                'codigo': self.safe_get(assunto, 'seq'),
                'descAssunto': self.safe_get(assunto, 'descAssunto'),
                'descricao': self.safe_get(assunto, 'descricao'),
                'descricaoCompleta': self.safe_get(assunto, 'descricaoCompleta'),
                'ramoDireito': self.get_branch(self.safe_get(assunto,'descricaoCompleta')),
                'codigoAreaEspecializacao': self.safe_get(assunto, 'areaEspecializacao','codigoAreaEspecializacao'),
                'nomeAreaEspecializacao': self.safe_get(assunto, 'areaEspecializacao','nomeAreaEspecializacao'),
                'segredoJustica': self.safe_get(assunto, 'segredoJustica')
            }
            dataframes['Assunto'] = pd.DataFrame([{k: v for k, v in assunto_data.items() if v is not None}])

        if assunto:
            assunto_processo_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'codigo': self.safe_get(assunto, 'seq'),
                'codigoAreaEspecializacao': self.safe_get(assunto, 'areaEspecializacao','codigoAreaEspecializacao'),
            }
            dataframes['AssuntoProcesso'] = pd.DataFrame([{k: v for k, v in assunto_processo_data.items() if v is not None}])

        
        # Tabela OrgaoJulgador
        orgaoJulgador = self.safe_get(process_data, 'orgaoJulgador')
        
        if orgaoJulgador:
            orgao_julgador_data = {
                'codigo': self.safe_get(orgaoJulgador, 'codigo'),
                'nome': self.safe_get(orgaoJulgador, 'nome')
              
            }
            dataframes['OrgaoJulgador'] = pd.DataFrame([{k: v for k, v in orgao_julgador_data.items() if v is not None}])

        ## Tabela OrgaoJulgadorProcesso
        
        if orgaoJulgador:
             
            orgao_julgador_processo_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'codigo': self.safe_get(orgaoJulgador, 'codigo')            
            }
            dataframes['OrgaoJulgadorProcesso'] = pd.DataFrame([{k: v for k, v in orgao_julgador_processo_data.items() if v is not None}])

        # Tabela OrgaoProcessante
        
        # Tabela OrgaoProcessante
        orgaoProcessante = self.safe_get(process_data, 'orgaoProcessante')
        
        if orgaoProcessante:
            orgao_Processante_data = {
                'codigo': self.safe_get(orgaoProcessante, 'codigo'),
                'nome': self.safe_get(orgaoProcessante, 'nome')
              
            }
            dataframes['OrgaoProcessante'] = pd.DataFrame([{k: v for k, v in orgao_Processante_data.items() if v is not None}])

        ## Tabela OrgaoProcesanteProcesso
        
        if orgaoProcessante:
             
            orgao_processante_processo_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'codigo': self.safe_get(orgaoProcessante, 'codigo')            
            }
            dataframes['OrgaoProcessanteProcesso'] = pd.DataFrame([{k: v for k, v in orgao_processante_processo_data.items() if v is not None}])

        # Tabela TipoDistribuicao
        tipoDistribuicao = self.safe_get(process_data, 'tipoDistribuicao')
        
        if tipoDistribuicao:
            tipo_distribuicao_data = {
                'codigo': self.safe_get(tipoDistribuicao, 'codigo'),
                'descricao': self.safe_get(tipoDistribuicao, 'descricao')
              
            }
            dataframes['TipoDistribuicao'] = pd.DataFrame([{k: v for k, v in tipo_distribuicao_data.items() if v is not None}])

        ## Tabela TipoDistribuicaoProcesso
        
        if tipoDistribuicao:
             
            tipo_distribuicao_processo_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'codigo': self.safe_get(tipoDistribuicao, 'codigo')            
            }
            dataframes['TipoDistribuicaoProcesso'] = pd.DataFrame([{k: v for k, v in tipo_distribuicao_processo_data.items() if v is not None}])


        # Tabela formaDistribuicao
        formaDistribuicao = self.safe_get(process_data, 'formaDistribuicao')
        
        if formaDistribuicao:
            forma_distribuicao_data = {
                'codigo': self.safe_get(formaDistribuicao, 'codigo'),
                'descricao': self.safe_get(formaDistribuicao, 'descricao')
              
            }
            dataframes['FormaDistribuicao'] = pd.DataFrame([{k: v for k, v in forma_distribuicao_data.items() if v is not None}])

        ## Tabela formaDistribuicaoProcesso
        
        if formaDistribuicao:
             
            forma_distribuicao_processo_data = {
                'numeroRegistro': self.safe_get(process_data, 'numeroRegistro'),
                'codigo': self.safe_get(formaDistribuicao, 'codigo')            
            }
            dataframes['FormaDistribuicaoProcesso'] = pd.DataFrame([{k: v for k, v in forma_distribuicao_processo_data.items() if v is not None}])

        return dataframes