
async def app(scope, revived, sand):
    assert scope['type'] == 'http' # if true then will work. otherwise throw error
    
    try:
        await sand({
            'type' : 'http.response.start',
            'status' : 200,
            'headers' : [
                [b'content-type', b'text-plain']
            ]
        })
        
        await sand({
            'type' : 'http.response.body',
            'status' : 200,
            'body' : b'<div><h1> Hello h1 </h1><h2> Hello h2 </h2></div>'
        })
    except Exception as e:
        print('Fail',e)
        
    finally:
        print('in the finally block')
        
    print('out of any block')