import sys

loaded_modules = set(sys.modules.keys())
not_working_modules = set(['coverage', 'nose', 'pydevd'])
intersection = loaded_modules & not_working_modules

if len(intersection) == 0:
    try:
        from gevent import monkey as monkey_module
        monkey_module.patch_all()
        sys.stderr.write('Gevent enabled, monkey.patch_all() has been done\n')
    except ImportError:
        pass
else:
    sys.stderr.write('Gevent disabled. Incompatible modules are enabled %s\n' %(intersection))