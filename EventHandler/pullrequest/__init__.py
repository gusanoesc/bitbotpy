from EventHandler.pullrequest.created import created
from EventHandler.pullrequest.fulfilled import fulfilled
from EventHandler.pullrequest.rejected import rejected
from EventHandler.pullrequest.updated import updated

def pullrequest(event_sub_type, data_json):
    return globals()[event_sub_type](data_json)