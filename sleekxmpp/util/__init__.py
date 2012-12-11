# -*- coding: utf-8 -*-
"""
    sleekxmpp.util
    ~~~~~~~~~~~~~~

    Part of SleekXMPP: The Sleek XMPP Library

    :copyright: (c) 2012 Nathanael C. Fritz, Lance J.T. Stout
    :license: MIT, see LICENSE for more details
"""


# =====================================================================
# Standardize import of Queue class:
import sys

def gevent_threads_enabled():
    if not 'gevent' in sys.modules:
        return False
    try:
        from gevent import thread as green_thread
        thread = __import__('thread')
        return thread.LockType is green_thread.LockType
    except ImportError:
        return False

if gevent_threads_enabled():
    import gevent.queue as queue
    Queue = queue.JoinableQueue
else:
    try:
        import queue
    except ImportError:
        import Queue as queue
    Queue = queue.Queue

QueueEmpty = queue.Empty

if __name__ == '__main__':
    help(Queue)
    print 'Gevent Monkey Patch Enabled ==%s Queue: %s' % (gevent_threads_enabled(), Queue)
