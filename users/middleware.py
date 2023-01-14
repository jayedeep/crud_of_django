def mymiddleware(get_response):
    print(">>>>>first time initialize")
    def my_function(request):
        print(">>>> Before View called")
        response = get_response(request)
        print("<<<< After View Called ")
        return response
    return my_function

class ClassBasedCustomMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
        print(">>>one time initialize")
    
    def __call__(self,request):
        print(">>>>before request")
        response=self.get_response(request)
        print("><<<<after request")
        return response
