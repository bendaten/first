import urllib2


class FirstUtils(object):

    @staticmethod
    def is_internet_on():

        """
        Check if connected to the internet to enable email validation

        :return:
        :rtype: bool
        """
        try:
            urllib2.urlopen('http://216.58.192.142', timeout=1)
            return True
        except urllib2.URLError as ex:
            print str(ex)
            return False
