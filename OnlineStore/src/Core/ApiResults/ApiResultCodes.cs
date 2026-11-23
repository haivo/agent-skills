using System;
using System.Collections.Generic;
using System.Text;

namespace Store.Core.ApiResults
{
    public class ApiResultCodes
    {
        public const string InvalidRequest = "invalid_request";
        public const string InvalidJson = "invalid_json";
        public const string Unauthorized = "unauthorized";
        
        public const string RestrictedResource = "restricted_resource";
        public const string ObjectNotFound = "object_not_found";
        public const string Error = "error";
    }
}
