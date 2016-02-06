import facebook

cmumeets_access_token = 'CAALfpk6SpC4BAJmpfpwW6f7QkG01BbB020uAOAsa3a24ZBZC5M3zw8EhqxcMvZAGPCFKwiPgiMnFyVqJKELZAwDZBwkZAWLNFpZBeY5kZAOTEnnzh1oUkAtvMJoDjea3iWtUshzU3AZBsovLSanoXU7ZBLSVWx9HHTMO2atSDy4e7ziN7QLjBCxHfDjRxeC7f5MF3nL8WuI3fSigZDZD'

def get_profile_pic(id, access_token = cmumeets_access_token):
    graph = facebook.GraphAPI(access_token=access_token,version='2.5')
    return graph.get_connections(graph.get_object('{}'.format(id))['id'],'picture')['url']

def get_friends(access_token = cmumeets_access_token, id='me'):
    graph = facebook.GraphAPI(access_token=access_token,version='2.5')
    return graph.get_connections(graph.get_object(id)['id'],'friends')['data']

def get_profile_pics(access_token = cmumeets_access_token):
    graph = facebook.GraphAPI(access_token=access_token,version='2.5')
    ret = {}
    ret[graph.get_object('me')['name']] = graph.get_connections(graph.get_object('me')['id'],'picture')['url']
    for friend in get_friends(access_token = access_token):
        ret[friend['name']] = get_profile_pic(friend['id'])
    return ret
