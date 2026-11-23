using System;
using System.Collections.Generic;
using System.Text;

namespace Store.Core.ApiResults
{
    public interface IApiResult
    {
    }

    public interface IApiResult<T> : IApiResult
    {}   
}
