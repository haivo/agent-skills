using System;
using System.Collections.Generic;
using System.Text;

namespace Store.Core.ApiResults
{
    public class ApiResult<T> : ApiResultBase, IApiResult<T>
    {
        public T? Data { get; set; }
        public ApiResult() : base() { }

        public static ApiResult<T> Ok(T data) => new () { Data = data };
    }

    public class  ApiResult : ApiResult<object>
    {
        
    }
}
