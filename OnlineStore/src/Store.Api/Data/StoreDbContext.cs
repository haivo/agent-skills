using Microsoft.EntityFrameworkCore;
using Store.Api.Entities;

namespace Store.Api.Data
{
    public class StoreDbContext(DbContextOptions<StoreDbContext> options) : DbContext(options)
    {
        public DbSet<Product> Products => Set<Product>();

        protected override void OnModelCreating(ModelBuilder b)
        {
            b.Entity<Product>(e =>
            {
                e.Property(p => p.Name).HasMaxLength(200).IsRequired();
                e.Property(p => p.Price).HasPrecision(18, 2);
            });
        }
    }
}
