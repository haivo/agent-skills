# OnlineStore

Learning project: an online store built step by step (Web API, then microservices, then a Vue front end).

## Structure

```
OnlineStore.slnx
src/
  Api/                    ASP.NET Core Web API (.NET 10)
    Modules/              HTTP endpoints, one module per feature
    Middlewares/          Error handling and other pipeline pieces
    AuthHandlers/         Authentication and authorization handlers
    Extensions/           Startup and helper extension methods
  Application/            Use cases (CQRS)
    Features/             Commands and queries, one folder per feature
    Modules/              Module interface shared with the API
    Extensions/
  Core/                   No dependencies on other projects
    Entities/             Database classes (Product, Order, ...)
    ApiResults/           Standard API response shapes
    PagingApiResult/      Paged response shapes
  Infrastructure/         Database access
    Persistent/           EF Core DbContext
    Extensions/           Registration of infrastructure services
  Test/                   xUnit tests
    Extensions/
  Playwright/             End-to-end tests (Node)
    tests/
```

Project references: Api -> Application, Infrastructure. Application -> Core. Infrastructure -> Core. Test -> Application, Infrastructure.

## Commands

```
dotnet build
dotnet run --project src/Api     # http://localhost:5140
dotnet test
```

Playwright (first time: `npm install` then `npx playwright install` inside `src/Playwright`):

```
npm test
```
