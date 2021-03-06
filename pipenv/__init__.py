from .cli import cli

PYTHON_VERSIONS = (
    ('Python 3.6.0', 'documentation released on 23 December 2016.'),
    ('Python 3.5.2', 'documentation released on 27 June 2016.'),
    ('Python 3.5.1', 'documentation released on 07 December 2015.'),
    ('Python 3.5.0', 'documentation released on 13 September 2015.'),
    ('Python 3.4.5', 'documentation released on 26 June 2016.'),
    ('Python 3.4.4', 'documentation released on 06 December 2015.'),
    ('Python 3.4.3', 'documentation released on 25 February 2015.'),
    ('Python 3.4.2', 'documentation released on 4 October 2014.'),
    ('Python 3.4.1', 'documentation released on 18 May 2014.'),
    ('Python 3.4.0', 'documentation released on 16 March 2014.'),
    ('Python 3.3.6', 'documentation released on 11 October 2014.'),
    ('Python 3.3.5', 'documentation released on 9 March 2014.'),
    ('Python 3.3.4', 'documentation released on 9 February 2014.'),
    ('Python 3.3.3', 'documentation released on 17 November 2013.'),
    ('Python 3.3.2', 'documentation released on 15 May 2013.'),
    ('Python 3.3.1', 'documentation released on 7 April 2013.'),
    ('Python 3.3.0', 'documentation released on 29 September 2012.'),
    ('Python 3.2.6', 'documentation released on 11 October 2014.'),
    ('Python 3.2.5', 'documentation released on 15 May 2013.'),
    ('Python 3.2.4', 'documentation released on 7 April 2013.'),
    ('Python 3.2.3', 'documentation released on 10 April 2012.'),
    ('Python 3.2.2', 'documentation released on 4 September 2011.'),
    ('Python 3.2.1', 'documentation released on 10 July 2011.'),
    ('Python 3.2', 'documentation released on 20 February 2011.'),
    ('Python 3.1.5', 'documentation released on 9 April 2012.'),
    ('Python 3.1.4', 'documentation released on 11 June 2011.'),
    ('Python 3.1.3', 'documentation released on 27 November 2010.'),
    ('Python 3.1.2', 'documentation released on 21 March 2010.'),
    ('Python 3.1.1', 'documentation released on 17 August 2009.'),
    ('Python 3.1', 'documentation released on 27 June 2009.'),
    ('Python 3.0.1', 'documentation released on 13 February 2009.'),
    ('Python 3.0', 'documentation released on 3 December 2008.'),
    ('Python 2.7.13', 'documentation released on 17 December 2016'),
    ('Python 2.7.12', 'documentation released on 26 June 2016.'),
    ('Python 2.7.11', 'documentation released on 5 December 2015.'),
    ('Python 2.7.10', 'documentation released on 23 May 2015.'),
    ('Python 2.7.9', 'documentation released on 10 December 2014.'),
    ('Python 2.7.8', 'documentation released on 1 July 2014.'),
    ('Python 2.7.7', 'documentation released on 31 May 2014.'),
    ('Python 2.7.6', 'documentation released on 10 November 2013.'),
    ('Python 2.7.5', 'documentation released on 15 May 2013.'),
    ('Python 2.7.4', 'documentation released on 6 April 2013.'),
    ('Python 2.7.3', 'documentation released on 9 April 2012.'),
    ('Python 2.7.2', 'documentation released on 11 June 2011.'),
    ('Python 2.7.1', 'documentation released on 27 November 2010.'),
    ('Python 2.7', 'documentation released on 4 July 2010.'),
    ('Python 2.6.9', 'documentation released on 29 October 2013.'),
    ('Python 2.6.8', 'documentation released on 10 April 2012.'),
    ('Python 2.6.7', 'documentation released on 3 June 2011.'),
    ('Python 2.6.6', 'documentation released on 24 August 2010.'),
    ('Python 2.6.5', 'documentation released on 19 March 2010.'),
    ('Python 2.6.4', 'documentation released on 25 October 2009.'),
    ('Python 2.6.3', 'documentation released on 2 October 2009.'),
    ('Python 2.6.2', 'documentation released on 14 April 2009.'),
    ('Python 2.6.1', 'documentation released on 4 December 2008.'),
    ('Python 2.6', 'documentation released on 1 October 2008.'),
    ('Python 2.5.4', 'documentation released on 23 December 2008.'),
    ('Python 2.5.3', 'documentation released on 19 December 2008.'),
    ('Python 2.5.2', 'documentation released on 21 February 2008.'),
    ('Python 2.5.1', 'documentation released on 18 April 2007.'),
    ('Python 2.5', 'documentation released on 19 September 2006.'),
    ('Python 2.4.4', 'documentation released on 18 October 2006.'),
    ('Python 2.4.3', 'documentation released on 29 March 2006.'),
    ('Python 2.4.2', 'documentation released on 28 September 2005.'),
    ('Python 2.4.1', 'documentation released on 30 March 2005.'),
    ('Python 2.4', 'documentation released on 30 November 2004.'),
    ('Python 2.3.5', 'documentation released on 8 February 2005.'),
    ('Python 2.3.4', 'documentation released on 27 May 2004.'),
    ('Python 2.3.3', 'documentation released on 19 December 2003.'),
    ('Python 2.3.2', 'documentation released on 3 October 2003.'),
    ('Python 2.3.1', 'documentation released on 23 September 2003.'),
    ('Python 2.3', 'documentation released on 29 July 2003.'),
    ('Python 2.2.3', 'documentation released on 30 May 2003.'),
    ('Python 2.2.2', 'documentation released on 14 October 2002.'),
    ('Python 2.2.1', 'documentation released on 10 April 2002.'),
    ('Python 2.2p1', 'documentation released on 29 March 2002.'),
    ('Python 2.2', 'documentation released on 21 December 2001.'),
    ('Python 2.1.3', 'documentation released on 8 April 2002.'),
    ('Python 2.1.2', 'documentation released on 16 January 2002.'),
    ('Python 2.1.1', 'documentation released on 20 July 2001.'),
    ('Python 2.1', 'documentation released on 15 April 2001.'),
    ('Python 2.0.1', 'documentation released on 22 June 2001.'),
    ('Python 2.0', 'documentation released on 16 October 2000.'),
    ('Python 1.6', 'documentation released on 5 September 2000.'),
    ('Python 1.5.2p2', 'documentation released on 22 March 2000.'),
    ('Python 1.5.2p1', 'documentation released on 6 July 1999.'),
    ('Python 1.5.2', 'documentation released on 30 April 1999.'),
    ('Python 1.5.1p1', 'documentation released on 6 August 1998.'),
    ('Python 1.5.1', 'documentation released on 14 April 1998.'),
    ('Python 1.5', 'documentation released on 17 February 1998.'),
    ('Python 1.4', 'documentation released on 25 October 1996.'),
)

if __name__ == '__main__':
    cli()
