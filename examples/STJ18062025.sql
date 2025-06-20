USE [master]
GO
/****** Object:  Database [STJ]    Script Date: 18/06/2025 18:54:58 ******/
CREATE DATABASE [STJ]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'STJ', FILENAME = N'S:\UserDBData\DataFiles\STJ.mdf' , SIZE = 7282688KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'STJ_log', FILENAME = N'S:\UserDBLog\LogFiles\STJ_log.ldf' , SIZE = 6365184KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [STJ] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [STJ].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [STJ] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [STJ] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [STJ] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [STJ] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [STJ] SET ARITHABORT OFF 
GO
ALTER DATABASE [STJ] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [STJ] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [STJ] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [STJ] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [STJ] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [STJ] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [STJ] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [STJ] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [STJ] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [STJ] SET  DISABLE_BROKER 
GO
ALTER DATABASE [STJ] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [STJ] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [STJ] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [STJ] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [STJ] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [STJ] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [STJ] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [STJ] SET RECOVERY FULL 
GO
ALTER DATABASE [STJ] SET  MULTI_USER 
GO
ALTER DATABASE [STJ] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [STJ] SET DB_CHAINING OFF 
GO
ALTER DATABASE [STJ] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [STJ] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [STJ] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [STJ] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'STJ', N'ON'
GO
ALTER DATABASE [STJ] SET QUERY_STORE = ON
GO
ALTER DATABASE [STJ] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [STJ]
GO
/****** Object:  User [usr_harpia]    Script Date: 18/06/2025 18:54:59 ******/
CREATE USER [usr_harpia] FOR LOGIN [usr_harpia] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [MP\jose.filho]    Script Date: 18/06/2025 18:54:59 ******/
CREATE USER [MP\jose.filho] FOR LOGIN [MP\jose.filho] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [MP\FilomenaSalles]    Script Date: 18/06/2025 18:54:59 ******/
CREATE USER [MP\FilomenaSalles] FOR LOGIN [MP\FilomenaSalles] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [jose]    Script Date: 18/06/2025 18:54:59 ******/
CREATE USER [jose] FOR LOGIN [jose] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [MP\jose.filho]
GO
ALTER ROLE [db_owner] ADD MEMBER [MP\FilomenaSalles]
GO
ALTER ROLE [db_owner] ADD MEMBER [jose]
GO
/****** Object:  Table [dbo].[Assunto]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Assunto](
	[codigo] [int] NOT NULL,
	[descAssunto] [varchar](255) NULL,
	[descricao] [varchar](255) NULL,
	[descricaoCompleta] [varchar](max) NULL,
	[codigoAreaEspecializacao] [int] NULL,
	[nomeAreaEspecializacao] [varchar](50) NULL,
	[segredoJustica] [bit] NULL,
	[ramoDireito] [varchar](255) NULL,
	[IndAtivo] [char](1) NULL,
	[flgPrincipal] [char](1) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Classe]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Classe](
	[codigo] [int] NOT NULL,
	[sigla] [varchar](10) NULL,
	[codigoClasseEmbargada] [int] NULL,
	[nome] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[controle]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[controle](
	[registro] [bigint] NULL,
	[ano] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Deslocamento]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Deslocamento](
	[codigo] [bigint] NOT NULL,
	[numeroRegistro] [bigint] NULL,
	[localEntradaSeq] [int] NULL,
	[localSaidaSeq] [int] NULL,
	[dataEntrada] [datetime2](7) NULL,
	[dataSaida] [datetime2](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Destino]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Destino](
	[codigo] [int] NOT NULL,
	[descricao] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Fases]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Fases](
	[codigo] [int] NOT NULL,
	[numeroRegistro] [bigint] NULL,
	[dataHoraFase] [datetime2](7) NULL,
	[textoFase] [varchar](max) NULL,
	[descricaoSimplificada] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FormaDistribuicao]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FormaDistribuicao](
	[codigo] [int] NOT NULL,
	[descricao] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FormaDistribuicaoProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FormaDistribuicaoProcesso](
	[numeroRegistro] [bigint] NULL,
	[codigo] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Local]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Local](
	[codigoLocal] [int] NOT NULL,
	[nomeLocal] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[codigoLocal] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LocalProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LocalProcesso](
	[numeroRegistro] [bigint] NULL,
	[codigoLocal] [bigint] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MinistroRelator]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MinistroRelator](
	[numMinistro] [int] NOT NULL,
	[nomeMinistro] [varchar](255) NULL,
	[sexoMinistro] [varchar](1) NULL,
	[codigoTipoMinistro] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[numMinistro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NAOUSAR_AssuntoProcesso_NAOUSAR]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NAOUSAR_AssuntoProcesso_NAOUSAR](
	[numeroRegistro] [bigint] NULL,
	[codigo] [int] NULL,
	[codigoAreaEspecializacao] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NAOUSAR_MinistroRelatorProcesso_NAOUSAR]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NAOUSAR_MinistroRelatorProcesso_NAOUSAR](
	[numeroRegistro] [bigint] NULL,
	[numMinistro] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NumerosOrigemProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NumerosOrigemProcesso](
	[numeroRegistro] [bigint] NULL,
	[numerosOrigem] [varchar](255) NOT NULL,
	[numOrdem] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrgaoJulgador]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrgaoJulgador](
	[codigo] [varchar](10) NOT NULL,
	[nome] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrgaoJulgadorProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrgaoJulgadorProcesso](
	[numeroRegistro] [bigint] NULL,
	[codigo] [varchar](10) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrgaoProcessante]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrgaoProcessante](
	[codigo] [varchar](10) NOT NULL,
	[nome] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrgaoProcessanteProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrgaoProcessanteProcesso](
	[numeroRegistro] [bigint] NULL,
	[codigo] [varchar](10) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Origem]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Origem](
	[codigo] [varchar](10) NOT NULL,
	[nome] [varchar](255) NULL,
	[sigla] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Partes]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Partes](
	[codigoOAB] [varchar](10) NULL,
	[nome] [varchar](255) NULL,
	[cpfCnpj] [varchar](20) NULL,
	[codigo] [int] NOT NULL,
	[tipo] [varchar](10) NULL,
	[codTipoEnte] [varchar](10) NULL,
	[sexoParte] [char](1) NULL,
	[mpsp] [bit] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Peticoes]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Peticoes](
	[numero] [bigint] NOT NULL,
	[dataProtocolo] [datetime2](7) NULL,
	[descTipoPeticao] [varchar](255) NULL,
	[partePeticionante] [varchar](255) NULL,
	[status] [varchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[numero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Processo]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Processo](
	[numeroRegistro] [bigint] NOT NULL,
	[numeroRegistroFormatado] [varchar](25) NULL,
	[codigoClasse] [int] NULL,
	[numeroProcessoClasse] [int] NULL,
	[qtdVolumes] [int] NULL,
	[qtdApensos] [int] NULL,
	[dataRegistroProtocolo] [date] NULL,
	[dataAutuacao] [date] NULL,
	[justicaGratuita] [bit] NULL,
	[originario] [bit] NULL,
	[segredoJustica] [bit] NULL,
	[agravoSTF] [bit] NULL,
	[criminal] [bit] NULL,
	[criminalCorte] [bit] NULL,
	[prioridade] [varchar](10) NULL,
	[codigoCompetencia] [int] NULL,
	[numeroUnico] [varchar](25) NULL,
	[numeroUnicoFormatado] [varchar](50) NULL,
	[codigoClasseAnterior] [int] NULL,
	[numeroClasseAnterior] [int] NULL,
	[numeroRegistroVinculante] [varchar](25) NULL,
	[codigoOrigem] [varchar](10) NULL,
	[tipo] [char](1) NULL,
	[processoFisico] [bit] NULL,
	[processoEletronico] [bit] NULL,
	[preferencial] [bit] NULL,
	[sigiloso] [bit] NULL,
	[nivelSigilo] [varchar](10) NULL,
	[pais] [varchar](100) NULL,
	[codigoDestino] [int] NULL,
	[codigoStatus] [int] NULL,
	[numerosConexo] [varchar](10) NULL,
	[nomeLocalOrigem] [varchar](255) NULL,
	[numeroOrigemProtocolo] [varchar](50) NULL,
	[observacaoProcesso] [varchar](max) NULL,
	[pedidoLiminar] [bit] NULL,
	[recolheuCusta] [varchar](10) NULL,
	[nome] [varchar](255) NULL,
	[nomeCompleto] [varchar](255) NULL,
	[nomeUf] [varchar](50) NULL,
	[uf] [varchar](2) NULL,
	[parteAutora] [varchar](255) NULL,
	[tipoParteAutora] [varchar](50) NULL,
	[parteRe] [varchar](255) NULL,
	[tipoParteRe] [varchar](50) NULL,
	[ministro] [int] NULL,
	[codigoAssuntoCNJ] [int] NULL,
	[local] [varchar](10) NULL,
	[documentos] [varchar](10) NULL,
	[representativoControversia] [bit] NULL,
	[repetitivo] [bit] NULL,
	[valorCausa] [varchar](10) NULL,
	[dataSituacao] [date] NULL,
	[codigoRelator] [int] NULL,
	[codigoAssunto] [nchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[numeroRegistro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProcessoDecisao]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProcessoDecisao](
	[codigo] [bigint] NOT NULL,
	[numeroPeticao] [varchar](50) NULL,
	[tipoDespacho] [varchar](10) NULL,
	[codigoTipoDocumento] [int] NULL,
	[ministro] [varchar](255) NULL,
	[dataConfirmacaoPublicacao] [datetime2](7) NULL,
	[nome] [varchar](255) NULL,
	[seqInteiroTeor] [bigint] NULL,
	[julgamentoEletronico] [bit] NULL,
	[indTipoEditor] [varchar](50) NULL,
	[decisao] [bit] NULL,
	[numeroRegistro] [bigint] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProcessoFavorito]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProcessoFavorito](
	[numeroRegistro] [bigint] NULL,
	[numeroRegistroFavorito] [int] NULL,
	[seqProcessoFavorito] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProcessoPartes]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProcessoPartes](
	[numeroRegistro] [bigint] NULL,
	[codigoParte] [bigint] NULL,
	[siglaTipoParte] [varchar](50) NULL,
	[descricaoTipoParte] [varchar](255) NULL,
	[codTipoParte] [varchar](10) NULL,
	[seqParteProcesso] [bigint] NULL,
	[indicadorAutorReu] [char](1) NULL,
	[descricaoTipoParteFem] [varchar](255) NULL,
	[numeroOrdemParte] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProcessoPeticoes]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProcessoPeticoes](
	[numeroRegistro] [bigint] NULL,
	[numeropeticao] [bigint] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Status]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Status](
	[codigo] [int] NOT NULL,
	[descricao] [varchar](50) NULL,
	[tramitando] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TipoDistribuicao]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TipoDistribuicao](
	[codigo] [int] NOT NULL,
	[descricao] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TipoDistribuicaoProcesso]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TipoDistribuicaoProcesso](
	[numeroRegistro] [bigint] NULL,
	[codigo] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TipoDocumentoDecisao]    Script Date: 18/06/2025 18:54:59 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TipoDocumentoDecisao](
	[codigo] [int] NOT NULL,
	[descricao] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Partes] ADD  DEFAULT ('FALSE') FOR [mpsp]
GO
ALTER TABLE [dbo].[Deslocamento]  WITH CHECK ADD FOREIGN KEY([localSaidaSeq])
REFERENCES [dbo].[Local] ([codigoLocal])
GO
ALTER TABLE [dbo].[Deslocamento]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[Fases]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[FormaDistribuicaoProcesso]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[NAOUSAR_AssuntoProcesso_NAOUSAR]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[NAOUSAR_MinistroRelatorProcesso_NAOUSAR]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[NumerosOrigemProcesso]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[OrgaoJulgadorProcesso]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[OrgaoProcessanteProcesso]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[Processo]  WITH CHECK ADD  CONSTRAINT [FK_Processo_codigoOrigem] FOREIGN KEY([codigoOrigem])
REFERENCES [dbo].[Origem] ([codigo])
GO
ALTER TABLE [dbo].[Processo] CHECK CONSTRAINT [FK_Processo_codigoOrigem]
GO
ALTER TABLE [dbo].[ProcessoDecisao]  WITH CHECK ADD FOREIGN KEY([codigoTipoDocumento])
REFERENCES [dbo].[TipoDocumentoDecisao] ([codigo])
GO
ALTER TABLE [dbo].[ProcessoDecisao]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[ProcessoFavorito]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
ALTER TABLE [dbo].[TipoDistribuicaoProcesso]  WITH CHECK ADD FOREIGN KEY([numeroRegistro])
REFERENCES [dbo].[Processo] ([numeroRegistro])
GO
USE [master]
GO
ALTER DATABASE [STJ] SET  READ_WRITE 
GO
