# Classes

class tempShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'tempShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('AirTemperature', self.input['AirTemperature'])

class humShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'humShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Humidity', self.input['Humidity'])

class pressureShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'pressureShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('AtmosphericPressure', self.input['AtmosphericPressure'])

class precShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'precShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Precipitation', self.input['Precipitation'])

class windDirShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'windDirShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('WindDirection', self.input['WindDirection'])

class windSpeedShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'windSpeedShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('WindSpeed', self.input['WindSpeed'])

class soilTempShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'soilTempShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('SoilTemperature', self.input['SoilTemperature'])

class soilHumShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'soilHumShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('SoilHumidity', self.input['SoilHumidity'])

class batteryShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'batteryShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Battery', self.input['Battery'])


# Available actions

self.add_available_action(
    'tempShift',
    {
        'label': 'tempShift',
        'description': 'Temperature change',
        'input': {
            'type': 'object',
            'required': [
                'AirTemperature'
            ],
            'properties': {
                'AirTemperature': {
                    'type': 'number',
                    'unit': 'degrees Celsius',
                },
            },
        },
    },
    tempShiftAction)

self.add_available_action(
    'humShift',
    {
        'label': 'humShift',
        'description': 'Humidity change',
        'input': {
            'type': 'object',
            'required': [
                'Humidity'
            ],
            'properties': {
                'Humidity': {
                    'type': 'number',
                    'unit': 'percent',
                },
            },
        },
    },
    humShiftAction)

self.add_available_action(
    'pressureShift',
    {
        'label': 'humShift',
        'description': 'Atmospheric Pressure change',
        'input': {
            'type': 'object',
            'required': [
                'AtmosphericPressure'
            ],
            'properties': {
                'AtmosphericPressure': {
                    'type': 'number',
                    'unit': 'pascal',
                },
            },
        },
    },
    pressureShiftAction)

self.add_available_action(
    'precShift',
    {
        'label': 'humShift',
        'description': 'Precipitation change',
        'input': {
            'type': 'object',
            'required': [
                'Precipitation'
            ],
            'properties': {
                'Precipitation': {
                    'type': 'number',
                    'unit': 'millimeters',
                },
            },
        },
    },
    precShiftAction)

self.add_available_action(
    'windDirShift',
    {
        'label': 'humShift',
        'description': 'Wind direction change',
        'input': {
            'type': 'object',
            'required': [
                'WindDirection'
            ],
            'properties': {
                'WindDirection': {
                    'type': 'intger',
                    'unit': 'null',
                },
            },
        },
    },
    windDirShiftAction)

self.add_available_action(
    'windSpeedShift',
    {
        'label': 'windSpeedShift',
        'description': 'Wind speed change',
        'input': {
            'type': 'object',
            'required': [
                'WindSpeed'
            ],
            'properties': {
                'WindSpeed': {
                    'type': 'number',
                    'unit': 'meters per second',
                },
            },
        },
    },
    windSpeedShiftAction)

self.add_available_action(
    'soilTempShift',
    {
        'label': 'soilTempShift',
        'description': 'Soil temperature change',
        'input': {
            'type': 'object',
            'required': [
                'SoilTemperature'
            ],
            'properties': {
                'SoilTemperature': {
                    'type': 'number',
                    'unit': 'degrees celsius',
                },
            },
        },
    },
    soilTempShiftAction)

self.add_available_action(
    'soilHumShift',
    {
        'label': 'soilHumShift',
        'description': 'Soil humidity change',
        'input': {
            'type': 'object',
            'required': [
                'SoilHumidity'
            ],
            'properties': {
                'SoilHumidity': {
                    'type': 'number',
                    'unit': 'percent'
                },
            },
        },
    },
    soilHumShiftAction)

self.add_available_action(
    'batteryShift',
    {
        'label': 'batteryShift',
        'description': 'Battery percentage change',
        'input': {
            'type': 'object',
            'required': [
                'Battery'
            ],
            'properties': {
                'Battery': {
                    'type': 'number',
                    'unit': 'percent'
                },
            },
        },
    },
    batteryShiftAction)

self.add_available_event(
    'tempChange',
    {
        'description':
        'The lamp has exceeded its safe operating temperature',
        'type': 'number',
        'unit': 'degree celsius',
        })
