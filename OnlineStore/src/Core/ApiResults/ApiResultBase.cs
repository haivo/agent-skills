using System;
using System.Collections.Generic;
using System.Text;

namespace Store.Core.ApiResults
{
    public abstract class ApiResultBase
    {
        public string? Code { get; set; }
        public bool Success { get; set; }
        public IEnumerable<ValidationError> Errors { get; set; }
        public string? Message { get; set; }

        public ApiResultBase()
        {
            Success = true;
            Errors = new List<ValidationError>();
        }

        public static ApiResult Error (string message = "Oops! Something went wrong. Please try again later.") => new () { Success = false, Code = ApiResultCodes.Error, Message = message };
    }
}
