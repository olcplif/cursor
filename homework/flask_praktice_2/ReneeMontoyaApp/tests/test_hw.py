import pytest
import json

from .conftest import *


def test_plant_post_001(client, plant_data):
    res = client.post("/api/v1/plants", json=plant_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_plants_002(client):
    res = client.get("/api/v1/plants")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_plant_003(client):
    res = client.get('/api/v1/plants/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_plant_004(client, upd_plant_data):
    res = client.put("/api/v1/plants/5", json=upd_plant_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_plant_destroy_005(client):
    res = client.delete('/api/v1/plants/8')
    assert res.status_code == 204
    res = client.get('/api/v1/plants/8')
    assert res.status_code == 404


def test_employee_post_006(client, employee_data):
    res = client.post("/api/v1/employees", json=employee_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_employees_007(client):
    res = client.get("/api/v1/employees")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_employee_008(client):
    res = client.get('/api/v1/employees/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_employee_009(client, upd_employee_data):
    res = client.put("/api/v1/employees/6", json=upd_employee_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_employees_destroy_010(client):
    res = client.delete('/api/v1/employees/8')
    assert res.status_code == 204
    res = client.get('/api/v1/employees/8')
    assert res.status_code == 404


def test_salon_post_011(client, salon_data):
    res = client.post("/api/v1/salons", json=salon_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_salons_012(client):
    res = client.get("/api/v1/salons")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_salon_013(client):
    res = client.get('/api/v1/salons/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_salon_014(client, upd_salon_data):
    res = client.put("/api/v1/salons/3", json=upd_salon_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_salons_destroy_015(client):
    res = client.delete('/api/v1/salons/8')
    assert res.status_code == 204
    res = client.get('/api/v1/salons/8')
    assert res.status_code == 404


def test_menu_item_post_016(client, menu_item_data):
    res = client.post("/api/v1/menu-items", json=menu_item_data)
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_menu_items_017(client):
    res = client.get("/api/v1/menu-items")
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_get_single_menu_item_018(client):
    res = client.get('/api/v1/menu-items/1')
    assert res.status_code == 200
    assert (b'Test' in res.data)


def test_update_menu_item_019(client, upd_menu_item_data):
    res = client.put("/api/v1/menu-items/3", json=upd_menu_item_data)
    assert res.status_code == 200
    assert (b'NEW_Text' in res.data)


def test_menu_item_destroy_020(client):
    res = client.delete('/api/v1/menu-items/8')
    assert res.status_code == 204
    res = client.get('/api/v1/menu-items/8')
    assert res.status_code == 404
