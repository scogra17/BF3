import functools 
from flask import Blueprint, request, jsonify, abort, make_response
from pytz import timezone 
from datetime import datetime
import time

bp = Blueprint('wallclock', __name__, url_prefix='/wallclock')

@bp.errorhandler(400)
def handle_bad_request(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)

def get_formatted_time(tz=timezone("UTC")): 
	# retrieve wall-clock time
	current_wall_clock_epoch = time.clock_gettime(time.CLOCK_REALTIME)
	# convert wall-clock epoch to datetime and apply timezone transformation
	current_datetime = datetime.fromtimestamp(current_wall_clock_epoch, tz)	
	
	return current_datetime.strftime("%H:%M:%S")


@bp.route('/api/v1.0/time', methods=['POST'])
def get_time():
	if not request.json:
		# Default to UTC if no payload provided
		tz_name = "UTC"
	else:
		# Default to UTC if no tz provided in payload
		tz_name = request.json.get('tz', "UTC")

	try: 
		tz = timezone(tz_name)
	except:
		# Return an error if a timezone is provided but does not exist
		abort(400)
	
	respDict = {"time": get_formatted_time(tz)}

	return respDict
