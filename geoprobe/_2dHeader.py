"""Provides a dictonary containing the name, offset, type, and default value 
for each known value in a GeoProbe 2DData header"""

__license__   = "MIT License <http://http://www.opensource.org/licenses/mit-license.php>"
__copyright__ = "2009, Free Software Foundation"
__author__    = "Joe Kington <jkington@wisc.edu>"

"""Reversed engineered Jan 18, 2010 by Joe Kington.  GeoProbe 2DData (.2dd) files consist of 
a 8472 Byte header followed by "numTraces" traces stored as uint8's each with a 12 byte header.

Trace format:
    A GeoProbe 2DData file stores amplitude values as a series of "traces" in the z-direction
    (rather than a regular grid). Each trace has a 12 Byte header (format: >3f) consisting of:
    1) The model X-coordinate for the trace, 2) The model Y-coordinate for the trace, and 
    3) The trace number (stored as a float for some weird reason?)
    This is followed by "numSamples" uint8's containing the amplitude values
"""


#--Header Definition--------------------------------------------------------------
#    default:None indicates that the vaule must be obtained from the input data
headerLength = 8472 #In bytes
headerDef = {
        'version':          {'offset':0,    'type':'32s',   'default':'#GeoProbe 2DData V1.0 binary\n' },      
        '_numTraces':       {'offset':32,   'type':'>I',    'default':None },       # Number of x-values. This is _numTraces to allow the property data2d.numTraces, which returns data2d.grid.shape[0]
        '_numSamples':      {'offset':36,   'type':'>I',    'default':None },       # Number of z-values. (see above)
        'name':             {'offset':40,   'type':'128s',  'default':'Unknown'},   # Name of the line
        'startTime':        {'offset':168,  'type':'>f',    'default':None },       # Start time of the traces
        'endTime':          {'offset':172,  'type':'>f',    'default':None },       # End time of the traces
        'sampleRate':       {'offset':176,  'type':'>f',    'default':None },       # Sample rate of the traces
        'x0':               {'offset':180,  'type':'>f',    'default':0    },       # X-axis calibration factor (e.g. x = i*dx + x0, where i is the index value)
        'y0':               {'offset':184,  'type':'>f',    'default':0    },       # Y-axis calibration factor
        'z0':               {'offset':188,  'type':'>f',    'default':0    },       # Z-axis calibration factor
        'v0':               {'offset':192,  'type':'>f',    'default':0    },       # Voxel value calibration factor
        'v0User':           {'offset':196,  'type':'>f',    'default':0    },       # User-specified voxel value calibration factor (No idea what that means!)
        'dx':               {'offset':200,  'type':'>f',    'default':1    },       # X-axis scaling factor
        'dy':               {'offset':204,  'type':'>f',    'default':1    },       # Y-axis scaling factor
        'dz':               {'offset':208,  'type':'>f',    'default':1    },       # Z-axis scaling factor
        'dv':               {'offset':212,  'type':'>f',    'default':1    },       # Voxel value scaling factor
        'dvUser':           {'offset':216,  'type':'>f',    'default':1    },       # User-specified voxel value scaling factor (No idea what that means!)
        'xUnit':            {'offset':220,  'type':'16s',   'default':'Unknown' },  # Physical units for the X-axis
        'yUnit':            {'offset':236,  'type':'16s',   'default':'Unknown' },  # Physical units for the Y-axis
        'zUnit':            {'offset':252,  'type':'16s',   'default':'Unknown' },  # Physical units for the Z-axis
        'vUnit':            {'offset':268,  'type':'16s',   'default':'Unknown' },  # Physical units for voxels
        'xDescrip':         {'offset':284,  'type':'16s',   'default':'Unknown' },  # X-axis description
        'yDescrip':         {'offset':300,  'type':'16s',   'default':'Unknown' },  # Y-axis description
        'zDescrip':         {'offset':316,  'type':'16s',   'default':'Unknown' },  # Z-axis description
        'vDescrip':         {'offset':332,  'type':'16s',   'default':'Unknown' },  # Voxel description
        'smoothingFactor':  {'offset':348,  'type':'>f',    'default':0.0 },        # No idea what this really is...
        'georef':           {'offset':352,  'type':'>12d',  'default':[0,0,1,0,1,1,0,1,1,0,0,1] },    # 3 sets of points for georeferencing. Order: worldX1, worldX2, worldX3, worldY1, worldY2, worldY3, modelY1, modelY2, modelY3, modelX1, modelX2, modelX3
        'createdByUser':    {'offset':448,  'type':'32s',   'default':None },       # File last modified by username
        'creationDate':     {'offset':480,  'type':'>I',    'default':None },       # Unix-style timestamp of last modified on date
        'lastModifiedUser': {'offset':484,  'type':'32s',   'default':None },       # File last modified by username
        'lastModifiedDate': {'offset':516,  'type':'>I',    'default':None },       # Unix-style timestamp of last modified on date
        'histogram':        {'offset':520,  'type':'>255Q', 'default':255*(0,) },   # Histogram of amplitude values, bins are 0-255 (or -127 to +127) 
        '_unknown':         {'offset':2560, 'type':'5140B', 'default':5140*(0,) },  # Appears to be padding...
        'comments':         {'offset':7700, 'type':'772s',  'default':'Created by python-geoprobe' }  # Arbitrary comments.
}
