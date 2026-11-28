CREATE TABLE [dbo].[AuthenticationType] (
    [Id]      BIGINT        IDENTITY (1, 1) NOT NULL,
    [Type]    VARCHAR (50)  NULL,
    [Desc]    VARCHAR (200) NULL,
    [Created] DATETIME      CONSTRAINT [DF_AuthenticationType_Created] DEFAULT (getdate()) NOT NULL,
    CONSTRAINT [PK_AuthenticationType] PRIMARY KEY CLUSTERED ([Id] ASC)
);


GO

