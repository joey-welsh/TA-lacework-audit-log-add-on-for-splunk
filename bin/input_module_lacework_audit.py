# encoding = utf-8
import datetime
import requests
import json

'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''


def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # token = definition.parameters.get('token', None)
    # start_time = definition.parameters.get('start_time', None)
    # end_time = definition.parameters.get('end_time', None)
    # type = definition.parameters.get('type', None)
    # log_host = definition.parameters.get('log_host', None)
    # limit = definition.parameters.get('limit', None)
    pass


def collect_events(helper, ew):
    """Implement your data collection logic here

    # The following examples get the arguments of this input.
    # Note, for single instance mod input, args will be returned as a dict.
    # For multi instance mod input, args will be returned as a single value.
    opt_token = helper.get_arg('token')
    opt_start_time = helper.get_arg('start_time')
    opt_end_time = helper.get_arg('end_time')
    opt_type = helper.get_arg('type')
    opt_log_host = helper.get_arg('log_host')
    opt_limit = helper.get_arg('limit')
    # In single instance mode, to get arguments of a particular input, use
    opt_token = helper.get_arg('token', stanza_name)
    opt_start_time = helper.get_arg('start_time', stanza_name)
    opt_end_time = helper.get_arg('end_time', stanza_name)
    opt_type = helper.get_arg('type', stanza_name)
    opt_log_host = helper.get_arg('log_host', stanza_name)
    opt_limit = helper.get_arg('limit', stanza_name)

    # get input type
    helper.get_input_type()

    # The following examples get input stanzas.
    # get all detailed input stanzas
    helper.get_input_stanza()
    # get specific input stanza with stanza name
    helper.get_input_stanza(stanza_name)
    # get all stanza names
    helper.get_input_stanza_names()

    # The following examples get options from setup page configuration.
    # get the loglevel from the setup page
    loglevel = helper.get_log_level()
    # get proxy setting configuration
    proxy_settings = helper.get_proxy()
    # get account credentials as dictionary
    account = helper.get_user_credential_by_username("username")
    account = helper.get_user_credential_by_id("account id")
    # get global variable configuration
    global_userdefined_global_var = helper.get_global_setting(
        "userdefined_global_var")

    # The following examples show usage of logging related helper functions.
    # write to the log for this modular input using configured global log level or INFO as default
    helper.log("log message")
    # write to the log using specified log level
    helper.log_debug("log message")
    helper.log_info("log message")
    helper.log_warning("log message")
    helper.log_error("log message")
    helper.log_critical("log message")
    # set the log level for this modular input
    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
    helper.set_log_level(log_level)

    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, method, parameters=None, payload=None,
                                        headers=None, cookies=None, verify=True, cert=None,
                                        timeout=None, use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()

    # The following examples show usage of check pointing related helper functions.
    # save checkpoint
    helper.save_check_point(key, state)
    # delete checkpoint
    helper.delete_check_point(key)
    # get checkpoint
    state = helper.get_check_point(key)

    # To create a splunk event
    helper.new_event(data, time=None, host=None, index=None,
                     source=None, sourcetype=None, done=True, unbroken=True)
    """

    '''
    # The following example writes a random number as an event. (Multi Instance Mode)
    # Use this code template by default.
    import random
    data = str(random.randint(0,100))
    event = helper.new_event(source=helper.get_input_type(
    ), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
    ew.write_event(event)
    '''

    '''
    # The following example writes a random number as an event for each input config. (Single Instance Mode)
    # For advanced users, if you want to create single instance mod input, please use this code template.
    # Also, you need to uncomment use_single_instance_mode() above.
    import random
    input_type = helper.get_input_type()
    for stanza_name in helper.get_input_stanza_names():
        data = str(random.randint(0,100))
        event = helper.new_event(source=input_type, index=helper.get_output_index(
            stanza_name), sourcetype=helper.get_sourcetype(stanza_name), data=data)
        ew.write_event(event)
    '''
    # YourLacework in https://YourLacework.lacework.net/api/v2/ContainerRegistries/{type}/{subtype}
    lacework_prefix = helper.get_arg('lacework_customer_url_prefix')
    retrieval_interval = int(helper.get_arg('interval'))

    url = "https://{}.lacework.net/api/v2/AuditLogs".format(lacework_prefix)

    # Retrieve the checkpoint
    helper.log_info("last_time =" + str(helper.get_check_point('last_time')))

    last_endtime_checked = helper.get_check_point('last_time')

    if last_endtime_checked == None:
        # Start with 30 days ago
        last_endtime_checked = (datetime.datetime.now() -
                                datetime.timedelta(seconds=2592000))
        # .strftime("%y/%m/%d")
        # Get the next amount of time from that, probably 1 hour with of data
        # once done, update the checkpoints
        #helper.save_check_point("last_time", (last_endtime_checked + datetime.timedelta(
            #seconds=2592000)).strftime("%Y-%m-%dT%H:%M:%SZ"))
    else:
        # Parse the existing time
        last_endtime_checked = (datetime.datetime.now() -
                                datetime.timedelta(seconds=retrieval_interval))
        #helper.save_check_point("last_time", (last_endtime_checked + datetime.timedelta(seconds=retrieval_interval)).strftime("%Y-%m-%dT%H:%M:%SZ"))

    # The endtime we last checked will turn into the new start time
    start_time = last_endtime_checked.strftime("%Y-%m-%dT%H:%M:%SZ")
    helper.log_info("start_time = "+ start_time)
    # The new end time will be on day past the start_time
    end_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    helper.log_info("end_time = "+ str(end_time))
    #end_time = (last_endtime_checked + datetime.timedelta(seconds=retrieval_interval)
                #).strftime("%Y-%m-%dT%H:%M:%SZ")
    helper.save_check_point("last_time", (last_endtime_checked).strftime("%Y-%m-%dT%H:%M:%SZ"))
    
    # Get a secret key
    secret_key = helper.get_arg('secret_key')
    key_id = helper.get_arg('keyId')

    access_url = "https://{}.lacework.net/api/v2/access/tokens".format(
        lacework_prefix)
    access_data = {
        'keyId': key_id,
        'expiryTime': 60
    }
    access_headers = {
        'X-LW-UAKS': secret_key,
        'Content-Type': 'application/json'
    }

    secret_key_request = requests.post(
        access_url, data=json.dumps(access_data), headers=access_headers)
    secret_result = secret_key_request.json()
    auth_token = secret_result['token']

    # Get audit logs
    audit_log_params = {
        'startTime': start_time,
        'endTime': end_time
    }
    audit_log_headers = {
        'Authorization': "Bearer {}".format(auth_token),
        'Content-Type': "application/json"
    }
    audit_log_request = requests.get(
        url, params=audit_log_params, headers=audit_log_headers)

    request_json = audit_log_request.json()
    helper.log_info(request_json)
    data = request_json['data']

    # Ingest the events into splunk
    for event in data:
        timestamp = event['createdTime']
        epoch = datetime.datetime.strptime(
            timestamp, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        event = helper.new_event(json.dumps(event), time=epoch)
        ew.write_event(event)
