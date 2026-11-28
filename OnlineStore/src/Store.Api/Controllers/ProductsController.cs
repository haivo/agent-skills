using Microsoft.AspNetCore.Mvc;
using Store.Api.Entities;
using Store.Api.Services;

namespace Store.Api.Controllers
{
    [ApiController]
    [Route("api/products")]
    public class ProductsController(IProductService service) : ControllerBase
    {
        [HttpGet]
        public ActionResult<List<Product>> GetAll() => Ok(service.GetAll());

        [HttpGet("{id:int}")]
        public ActionResult<Product> GetById(int id)
        {
            var product = service.GetById(id);
            return product is null ? NotFound() : Ok(product);
        }

        [HttpPost]
        public ActionResult<Product> Create (Product product)
        {
            var created = service.Create(product);
            return CreatedAtAction(nameof(GetById), new { id = created.Id }, created);
        }
        
    }
}
