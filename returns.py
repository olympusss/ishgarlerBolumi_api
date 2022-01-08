class Returns:
    INSERTED        = {"error" : False, "body" : "INSERTED"}
    NOT_INSERTED    = {"error" : True, "body" : "NOT INSERTED"}
    BODY_NULL       = {"error" : True, "body" : "NULL"}
    UPDATED         = {"error" : False, "body" : "UPDATED"}
    NOT_UPDATED     = {"error" : True, "body" : "NOT_UPDATED"}
    DELETED         = {"error" : True, "body" : "DELETED"}
    NOT_DELETED     = {"error" : True, "body" : "NOT_DELETED"}
    TOKEN_NOT_FOUND = {"error" : True, "body" : "TOKEN_NOT_FOUND"}
    
    def object(obj):
        return {"error" : False, "body" : obj}
    
    def id(obj):
        return {"error" : False, "id" : obj}