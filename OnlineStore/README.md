# OnlineStore

Learning project: an online store built step by step (Web API, then microservices, then a Vue front end).

## Structure

```
OnlineStore.slnx
src/Store.Api/            ASP.NET Core Web API (.NET 10)
  Controllers/            HTTP endpoints
  Entities/               Database classes (Product, Order, ...)
  Dtos/                   Request and response shapes
  Data/                   EF Core DbContext and migrations
  Services/               Business logic
  Middleware/             Error handling and other pipeline pieces
tests/Store.Api.Tests/    xUnit tests
```

## Commands

```
dotnet build
dotnet run --project src/Store.Api     # http://localhost:5140
dotnet test
```
