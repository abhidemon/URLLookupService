from app.url_info_db import get_url_info, update_url_info, insert_url_info


# Testing the code
def test_get_url_info():
    info = get_url_info("http://google.com")
    print (info)

def test_update_url_info():
    res = update_url_info(url='somefakesite.com', malware_info='NOT_MALWARE')

def test_insert_url_info():
    resp = insert_url_info("somefakesite.com", "MALWARE")
    print(resp)

def test_combined_functionality():
    insert_url_info("mynewsite.com", "MALWARE")
    insert_url_info("mynewsite2.com", "NOT_MALWARE")
    
    info = get_url_info("mynewsite.com")
    assert info=="MALWARE"

    info2 = get_url_info("mynewsite2.com")
    assert info2 == "NOT_MALWARE"






