import pytest

def test_wallclock(client):
	# test valid payload
	assert client.post('wallclock/api/v1.0/time', data={'tz': 'UTC'}).status_code == 200
	# test empty payload
	assert client.post('wallclock/api/v1.0/time', data={}).status_code == 200
