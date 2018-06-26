import logging
import mylib

def main():
    # logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()

