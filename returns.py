class Returns:
    INSERTED     = {"error" : False, "body" : "INSERTED"}
    NOT_INSERTED = {"error" : True, "body" : "NOT INSERTED"}
    BODY_NULL    = {"error" : True, "body" : "NULL"}
    UPDATED      = {"error" : False, "body" : "UPDATED"}
    NOT_UPDATED  = {"error" : True, "body" : "NOT_UPDATED"}