-- =============================================
-- Author:		<HVo>
-- Create date: <04/02/2021>
-- Description:	<Get list of PublicKey>
-- =============================================
CREATE PROCEDURE [dbo].[Jwt_Get_PublicKeys] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT PublicKey FROM dbo.UserInfo WHERE AuthenticationId = 2 AND PublicKey IS NOT NULL
END

GO

