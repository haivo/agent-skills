CREATE TABLE [dbo].[Incomes] (
    [Id]         BIGINT        IDENTITY (1, 1) NOT NULL,
    [FirstName]  VARCHAR (100) NULL,
    [LastName]   VARCHAR (100) NULL,
    [Department] VARCHAR (100) NULL,
    [Salary]     DECIMAL (18)  NULL,
    CONSTRAINT [PK_Incomes] PRIMARY KEY CLUSTERED ([Id] ASC)
);


GO

