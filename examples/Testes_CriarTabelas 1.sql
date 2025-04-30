--Validar campos Json, identificando  qtde itens por processo e datatype

/*
D�vida:
1. Ao agregar os assuntos do processo numa �nica linha, ver como ser� apresentado quando este for sigiloso
2. Identificar o que pode ser obrigat�rio ou n�o. Aqueles que identifiquei Nulo, j� informei no script
3. Quando campo nulo, n�o identifiquei datatype, categorizei como Varchar(10) e indiquei "--*****" no scritp
*/

CREATE TABLE Processo (
    numeroRegistro BIGINT PRIMARY KEY,
    numeroRegistroFormatado VARCHAR(25),
    codigoClasse INT,
	numeroProcessoClasse INT, --**************** VALIDAR  - CLASSE
	qtdVolumes INT,
    qtdApensos INT,
    dataRegistroProtocolo DATE,
    dataAutuacao DATE,
    justicaGratuita BIT,
    originario BIT,
    segredoJustica BIT,
    agravoSTF BIT,
    criminal BIT,
    criminalCorte BIT,
	prioridade VARCHAR(10) NULL, --*****
    codigoCompetencia INT,
    numeroUnico BIGINT,
	numeroUnicoFormatado VARCHAR(50),
    codigoClasseAnterior INT,--**************** VALIDAR - CLASSE
    numeroClasseAnterior INT,--**************** VALIDAR - CLASSE
	numeroRegistroVinculante VARCHAR(10) NULL, --*****
	codigoOrigem  VARCHAR(10) FOREIGN KEY REFERENCES Origem(Codigo),
	tipo CHAR(1),
    processoFisico BIT,
    processoEletronico BIT,
    preferencial BIT,
    sigiloso BIT,
	nivelSigilo VARCHAR(10) NULL, --*****
	pais VARCHAR(100) NULL, --*****
	codigoDestino INT,
	codigoStatus INT,
	numerosConexo VARCHAR(10) NULL,
	nomeLocalOrigem VARCHAR(10) NULL,
	numeroOrigemProtocolo VARCHAR(50),
	observacaoProcesso VARCHAR(MAX) NULL,
	pedidoLiminar BIT, 
	recolheuCusta VARCHAR(10) NULL,
	nome VARCHAR(255),
    nomeCompleto VARCHAR(255),
    nomeUf VARCHAR(50),
    uf VARCHAR(2),
	parteAutora VARCHAR(255),
	tipoParteAutora VARCHAR(50),
	parteRe VARCHAR(255),
	tipoParteRe VARCHAR(50),
	ministro VARCHAR(10) NULL, --*****
	codigoAssuntoCNJ INT, --***** SERIA O ASSUNTO PRINCIPAL --VALIDAR
	local VARCHAR(10) NULL, --*****
	documentos VARCHAR(10) NULL, --*****
	representativoControversia BIT,
	repetitivo BIT,
	valorCausa VARCHAR(10) NULL, --*****
	dataSituacao date 
);

CREATE TABLE TipoDocumentoDecisao (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NULL --TEM VALOR NULO 
);

CREATE TABLE Decisao (
    codigo BIGINT PRIMARY KEY,
    numeroPeticao BIGINT NULL,
    tipoDespacho VARCHAR(10) NULL, --*****
	codigoTipoDocumento INT FOREIGN KEY REFERENCES TipoDocumentoDecisao(codigo) ,
    ministro VARCHAR(255) NULL,
    dataConfirmacaoPublicacao DATETIME2,
    nome VARCHAR(255) NULL,
    seqInteiroTeor BIGINT NULL,
    julgamentoEletronico BIT,
    indTipoEditor VARCHAR(50) NULL,
    decisao BIT 
);

CREATE TABLE ProcessoDecisao (
    numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
    codigoDecisao BIGINT FOREIGN KEY REFERENCES Decisao(codigo)
);

CREATE TABLE Peticoes (
    numero BIGINT PRIMARY KEY,
    dataProtocolo DATETIME2,
    descTipoPeticao VARCHAR(255),
    partePeticionante VARCHAR(255),
    status VARCHAR(500)
);

CREATE TABLE ProcessoPeticoes (
    numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
    numeropeticao BIGINT FOREIGN KEY REFERENCES Peticoes(numero)
);

--REVER ESTRUTURA E TABELAS RELACIONADAS A PARTE
--(UMA PARTE (CPF) PODE TER TIPO DIFERENTE EM PROCESSOS
--TALVEZ CRIAR TABELA COM TIPO PARTE
--VALIDAR 

CREATE TABLE Partes (
    siglaTipoParte VARCHAR(50) NULL,
    indicadorAutorReu CHAR(1) NULL,
	codigoTipoParte VARCHAR(10) NULL,
	codigoOAB VARCHAR(10) NULL,
    nome VARCHAR(255) NOT NULL,
    cpfCnpj VARCHAR(20) UNIQUE,
    codigo INT PRIMARY KEY,
	seqParteProcesso BIGINT, --***** S� APARECE QUANDO TIPO PARTE
	tipo VARCHAR(10), 
	codTipoEnte VARCHAR(10) NULL,
	descricaoTipoParte VARCHAR(255) NULL,
	numeroOrdemParte INT,
    descricaoTipoParteFem VARCHAR(255) NULL,
	sexoParte CHAR(1) NULL  
);

CREATE TABLE ProcessoPartes (
	numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigoParte INT FOREIGN KEY REFERENCES Partes(codigo)
);

CREATE TABLE Fases (
    codigo INT PRIMARY KEY,
    numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
	dataHoraFase DATETIME2,
    textoFase VARCHAR(MAX),
    descricaoSimplificada VARCHAR(MAX) --TEM VALOR BRANCO AO INV�S DE NULO
);

CREATE TABLE Local (
    codigoLocal INT PRIMARY KEY, 
	nomeLocal VARCHAR(255) NOT NULL
);

CREATE TABLE LocalProcesso (
    numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigoLocal INT NOT NULL
);

CREATE TABLE Deslocamento (
    codigo BIGINT PRIMARY KEY, -- Identificador �nico do deslocamento
    numeroRegistro BIGINT FOREIGN KEY REFERENCES Processo(numeroRegistro),
	localEntradaSeq INT FOREIGN KEY REFERENCES Local(codigoLocal),
    localSaidaSeq INT FOREIGN KEY REFERENCES Local(codigoLocal),
    dataEntrada DATETIME2 NULL,
    dataSaida DATETIME2 NULL ---Nem sempre existe dataSaida. 
);

CREATE TABLE ProcessoFavorito (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	numeroRegistroFavorito INT NOT NULL,
	seqProcessoFavorito int NOT NULL
);

CREATE TABLE MinistroRelatorProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	numMinistro INT NOT NULL
);

CREATE TABLE MinistroRelator (
    numMinistro INT PRIMARY KEY,
    nomeMinistro VARCHAR(255) NOT NULL,
    sexoMinistro VARCHAR(1) NOT NULL,
    codigoTipoMinistro VARCHAR(10) NOT NULL
);

CREATE TABLE NumerosOrigemProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	numerosOrigem VARCHAR(255) NOT NULL--DataType vai depender da formata��o
	);

CREATE TABLE Classe (
    codigo INT PRIMARY KEY,
    sigla VARCHAR(10) NULL,
	codigoClasseEmbargada INT NULL,
	nome VARCHAR(255) NULL   
);

CREATE TABLE Status (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(50) NULL,
	tramitando BIT NULL 
);

CREATE TABLE Destino (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL    
);

CREATE TABLE AssuntoProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigo INT NOT NULL,
	codigoAreaEspecializacao INT NOT NULL --se codigo assunto N�O se repetir por area ELIMINAR daqui
);

CREATE TABLE Assunto (
    codigo INT PRIMARY KEY,
	descAssunto VARCHAR(255)  NULL,
	descricao VARCHAR(255) NULL, --*****
	descricaoCompleta VARCHAR(MAX)  NULL,
    codigoAreaEspecializacao INT,
	nomeAreaEspecializacao VARCHAR(50)  NULL,
	segredoJustica BIT NULL --H� assuntos como segredo justi�a
	);
	
CREATE TABLE Origem (
    codigo VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sigla VARCHAR(10) NOT NULL
);

CREATE TABLE OrgaoJulgadorProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigo VARCHAR(10) NOT NULL
);


CREATE TABLE OrgaoJulgador (
    codigo VARCHAR(10) PRIMARY KEY, --*****
	nome VARCHAR(255) NOT NULL
);

CREATE TABLE OrgaoProcessanteProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigo VARCHAR(10) NOT NULL
);

CREATE TABLE OrgaoProcessante (
    codigo VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE FormaDistribuicaoProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigo INT NOT NULL
);

CREATE TABLE FormaDistribuicao (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE TipoDistribuicaoProcesso (
    numeroRegistro BIGINT  FOREIGN KEY REFERENCES Processo(numeroRegistro),
	codigo INT NOT NULL
);

CREATE TABLE TipoDistribuicao (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL
);





