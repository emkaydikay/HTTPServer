import urllib.request
import json

def post_data_Update():
    print("POST request: Updating next data to HTTPServer......")
    url = "http://localhost:8000"

    values = {
        "product_No": "ABC",
        "name": "MAIN",
        "latestVersion": "ABCD002",
        "Remark": "Release"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = json.dumps(values).encode("utf-8")
    print("Sent data to HTTPServer\n",data)

    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        print("Data received from HTTPServer\n",res.decode())
    except Exception as e:
        print(e)

def get_data_request():
    #
    # read the data from the URL and print it
    #
    import urllib.request
    # open a connection to a URL using urllib
    print("GET request: Getting latest data from HTTPServer......")
    webUrl  = urllib.request.urlopen('http://localhost:8000')

    #get the result code and print it
    print ("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print (data)
######MAIN#####
get_data_request()
post_data_Update()
