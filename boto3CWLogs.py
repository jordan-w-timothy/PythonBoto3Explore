import boto3
#Create a boto3 client
cw = boto3.client('logs')
##Define the logGroup Name
lgName = "/ecs/log4jex-task-definition"

def getLogStreams(logGrpName):
    ##Retrieve logStreams from CloudWatch
    logStreamResp = cw.describe_log_streams(
        logGroupName = logGrpName
    )
    print(logStreamResp)

    streamNames = []
    ##Loop over returned logStreams and add Name to streamNames Array
    for ls in logStreamResp['logStreams']:
        streamNames.append(ls['logStreamName'])

    return streamNames
        

def getLogEvents(logStreamName):
    ##Retrieve logEvents for specified logStream.
    logEventResp = cw.get_log_events(
        logGroupName = lgName,
        logStreamName = logStreamName
    )
    return logEventResp

# print(getLogStreams(lgName))
lsNames = getLogStreams(lgName)
logEvents = getLogEvents(lsNames[0])
print('\n')
print(logEvents)

##Parse of each log event
for logEvent in logEvents['events']:
    print("TimeStamp: " + str(logEvent['timestamp']) + '\n')
    print("Message: " + logEvent['message'] + '\n')