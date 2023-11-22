import json 
from django.http import JsonResponse

# JsonResponseJsonRespon
def api_home(request, *arg, **kwargs):
    body=request.body
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    print(data)
    data['headers']=request.headers
    data['content_type']=request.content_type
    return JsonResponse(data)