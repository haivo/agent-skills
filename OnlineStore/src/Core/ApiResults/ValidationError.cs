using System;
using System.Collections.Generic;
using System.Text;

namespace Store.Core.ApiResults
{
    public class ValidationError
    {
        public string? Field { get; set; }
        public string? Message { get; set; }    
    }
}
