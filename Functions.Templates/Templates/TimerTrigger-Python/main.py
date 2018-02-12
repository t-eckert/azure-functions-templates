import datetime

def main(myTimer: dict, logger):

    time_stamp = str(datetime.datetime.now())

    if myTimer['isPastDue']:
        logger.info('Python is running late!')
    
    logger.info(f'Python timer trigger function ran! {time_stamp}')