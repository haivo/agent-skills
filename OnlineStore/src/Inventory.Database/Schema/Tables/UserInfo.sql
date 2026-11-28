CREATE TABLE [dbo].[UserInfo] (
    [Id]               BIGINT         IDENTITY (1, 1) NOT NULL,
    [FirstName]        VARCHAR (50)   NOT NULL,
    [LastName]         VARCHAR (50)   NOT NULL,
    [UserName]         VARCHAR (50)   NOT NULL,
    [Email]            VARCHAR (50)   NOT NULL,
    [Password]         VARCHAR (20)   NOT NULL,
    [CreatedDate]      DATETIME       CONSTRAINT [DF_UserInfo_CreatedDate] DEFAULT (getdate()) NOT NULL,
    [InUse]            BIT            CONSTRAINT [DF_UserInfo_InUse] DEFAULT ((0)) NULL,
    [Expired]          DATETIME       NULL,
    [Token]            TEXT           NULL,
    [AuthenticationId] INT            NULL,
    [PrivatedKey]      VARCHAR (100)  NULL,
    [PublicKey]        NVARCHAR (300) NULL,
    [PasswordSalt]     BINARY (200)   NULL,
    [PasswordHash]     BINARY (200)   NULL,
    CONSTRAINT [PK_UserInfo] PRIMARY KEY CLUSTERED ([Id] ASC)
);


GO

