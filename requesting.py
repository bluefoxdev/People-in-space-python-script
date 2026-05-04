import requests

def safe_request(request: str):
    try:
        output = requests.get(request).json()
    except Exception as e:
        print(f'Error occured: "{e}"\nwith request: "{request}"')
    
    return output
