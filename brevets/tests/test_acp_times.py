import nose    # Testing framework
import requests
import logging
import arrow  # Import the Arrow library
from acp_times import open_time, close_time

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
log = logging.getLogger(__name__)

# Your test cases go here

def test_insert_into_db():
    # Sample data for testing
    data = {
        'km': 200,
        'dist': 200,
        'time': '2023-01-01T12:00'
    }
    
    # Send a POST request to insert data into the database
    response = requests.post('http://localhost:5001/_calc_times', params=data)
    
    # Check if the insertion was successful (status code 200)
    assert response.status_code == 200

def test_retrieve_from_db():
    data = {
        'km': 200,
        'dist': 200,
        'time': '2023-01-01T12:00'
    }
    
    # Insert data into the database for testing retrieval
    requests.post('http://localhost:5001/_calc_times', params=data)
    
    # Send a GET request to retrieve data from the database
    response = requests.get('http://localhost:5001/_calc_times', params=data)
    
    # Check if the retrieval was successful (status code 200)
    assert response.status_code == 200

def test_open_time_0_km():
    brevet_start_time = arrow.get("2023-01-01T00:00", 'YYYY-MM-DDTHH:mm')
    assert open_time(0, 200, brevet_start_time) == brevet_start_time

def test_open_time_200_km():
    brevet_start_time = arrow.get('2023-01-01T12:00')
    actual = open_time(200, 200, brevet_start_time).format('YYYY-MM-DDTHH:mm')
    expected = '2023-01-01T17:52'
    assert actual == expected, f'Actual: {actual}, Expected: {expected}'

def test_close_time_0_km():
    brevet_start_time = arrow.get("2023-01-01T00:00", 'YYYY-MM-DDTHH:mm')
    assert close_time(0, 200, brevet_start_time).format('YYYY-MM-DDTHH:mm') == '2023-01-01T01:00'

def test_close_time_200_km():
    brevet_start_time = arrow.get('2023-01-01T12:00')
    actual = close_time(200, 200, brevet_start_time).format('YYYY-MM-DDTHH:mm')
    expected = '2023-01-02T01:20'
    assert actual == expected, f'Actual: {actual}, Expected: {expected}'

def test_open_time_invalid_distance():
    brevet_start_time = arrow.get("2023-01-01T00:00", 'YYYY-MM-DDTHH:mm')
    assert open_time(2500, 200, brevet_start_time) == "Error!"



