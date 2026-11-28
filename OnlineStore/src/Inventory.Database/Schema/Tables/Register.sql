CREATE TABLE [dbo].[Register] (
    [Id]                   BIGINT         IDENTITY (1, 1) NOT NULL,
    [StreetNumber]         NVARCHAR (10)  NULL,
    [StreetName]           NVARCHAR (200) NULL,
    [Zipcode]              NVARCHAR (10)  NULL,
    [City]                 NVARCHAR (100) NULL,
    [State]                NVARCHAR (2)   NULL,
    [UserName]             NVARCHAR (100) NOT NULL,
    [Password]             NVARCHAR (100) NOT NULL,
    [Phone]                NVARCHAR (20)  NULL,
    [SocialSecurityNumber] NVARCHAR (10)  NULL,
    [Email]                NVARCHAR (200) NULL,
    CONSTRAINT [PK_Register] PRIMARY KEY CLUSTERED ([Id] ASC)
);


GO

