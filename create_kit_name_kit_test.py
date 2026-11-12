import sender_stand_request
import data 

def positive_assert(kit_body):
    response=sender_stand_request.post_new_user(data.user_body)
    auth_token=sender_stand_request.get_token(response)
    response=sender_stand_request.post_new_client_kit(kit_body,auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"] 

def negative_assert(kit_body):
    response=sender_stand_request.post_new_user(data.user_body)
    auth_token=sender_stand_request.get_token(response)
    response=sender_stand_request.post_new_client_kit(kit_body,auth_token)

    assert response.status_code == 400

###tests
def test_dopustimoe_kolichestvo_simvolov_1():
    kit_body = {
        "name": "М"
    }
    positive_assert(kit_body)


def test_dopustimoe_kolichestvo_simvolov_511():
    kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body)

def test_kolichestvo_simvolov_menshe_dopustimogo_0():
    kit_body = { "name": ""}
    negative_assert(kit_body)
    

def test_kolichestvo_simvolov_bolshe_dopustimogo_512():
    kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert(kit_body)

def test_razresheny_anglickie_bukvy():
    kit_body = {  "name":"QWErty"}
    positive_assert(kit_body)
    
def test_razresheny_russkie_bukvy():
    kit_body = {  "name":"Мария"}
    positive_assert(kit_body)

def test_razresheny_spechsimvoly():
    kit_body = {"name": '"№%@",'}
    positive_assert(kit_body)

def test_razresheny_probely():
    kit_body = {"name":  "Человек и КО" }
    positive_assert(kit_body)
    
def test_razresheny_chifry():
    kit_body = {"name":  "123" }
    positive_assert(kit_body)

def test_parametr_ne_peredan_v_zaprose():
    kit_body = { }
    negative_assert(kit_body)

def test_peredan_drugoy_tip_parametra():
    kit_body = {"name": 123}
    negative_assert(kit_body)
