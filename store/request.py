import requests
def ech():
    print('2-=')
    response=requests.get("https://google.com")
    print(response.status_code)
    
print(3)
if __name__=="__main__":
    print('1-=')
    ech()
