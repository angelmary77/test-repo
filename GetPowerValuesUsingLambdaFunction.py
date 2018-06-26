import logging
"""z = lambda x,y:x+y
print z(1,2)"""

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info('Started')
logging.info('doing calculation')
squares1=list(map(lambda x: x ** 2, [10,20,30,40]))
print squares1

numbers=[1,2,3,4]
squares2=list(map(lambda x:pow(x,2), numbers))
print squares2
logging.warning('finished')
