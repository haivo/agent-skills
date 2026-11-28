using Store.Api.Entities;


namespace Store.Api.Services;

public interface IProductService
{
    List<Product> GetAll();
    Product? GetById(int id);
    Product Create(Product product);
}

public class ProductService : IProductService
{
    private readonly List<Product> _products =
    [
        new Product { Id = 1, Name = "Keyboard", Price = 49.99m },
        new Product { Id = 2, Name = "Mouse", Price = 19.99m }
    ];
    public List<Product> GetAll() => _products;
    public Product? GetById(int id) => _products.FirstOrDefault(p => p.Id == id);
    
    public Product Create(Product product)
    {
        product.Id = _products.Count == 0 ? 1 : _products.Max(p => p.Id) + 1;
        _products.Add(product);
        return product;
    }
}
