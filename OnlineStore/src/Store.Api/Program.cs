using Microsoft.EntityFrameworkCore;
using Store.Api.Data;
using Store.Api.Services;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
//Add by HVo 11/28/26
builder.Services.AddSingleton<IProductService, ProductService>();
builder.Services.AddDbContext<StoreDbContext>(option => 
    option.UseSqlServer(builder.Configuration.GetConnectionString("OnlineStore")));
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
