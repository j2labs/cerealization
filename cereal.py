import time

###
### Test Environment
###

import cPickle
import simplejson
import json
import cjson # python-cjson in pypi
import ujson
import tnetstrings # http://tnetstrings.org/tnetstrings.py
import tnetstring

### Make cjson's interface match the others
cjson.dumps = cjson.encode
cjson.loads = cjson.decode
tnetstrings.dumps = tnetstrings.dump
tnetstrings.loads = tnetstrings.parse

### Prepare data structures
data_as_dict = {
    'foo': 'bar',
    'food': 'barf',
    'good': 'bars',
    'dood': 'wheres your car?',
    'wheres your car': 'dude?',
}
data_as_json = json.dumps(data_as_dict)
data_as_pickled = cPickle.dumps(data_as_dict)
data_as_tnetstrings = tnetstrings.dumps(data_as_dict)
data_as_tnetstring = data_as_tnetstrings

### 
num_loop_iterations = 1000000

### List of JSON implementations to test
mods = [json, simplejson, cjson, ujson, cPickle, tnetstrings, tnetstring]


### Time dumping from native to JSON
print 'Dumping:'
for mod in mods:
    start = time.time()
    for i in xrange(num_loop_iterations):
        mod.dumps(data_as_dict)
    print '  %s: %s' % (mod.__name__, (time.time() - start))


### Time loading from JSON into native
print 'Loading:'
for mod in mods:
    data = data_as_json
    if mod.__name__ == "cPickle":
        data = data_as_pickled
    elif mod.__name__ == "tnetstrings":
        data = data_as_tnetstrings
    elif mod.__name__ == "tnetstring":
        data = data_as_tnetstring
        
    start = time.time()
    for i in xrange(num_loop_iterations):
        mod.loads(data)
    print '  %s: %s' % (mod.__name__, (time.time() - start))
