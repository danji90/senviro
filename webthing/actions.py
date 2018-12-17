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
                    'unit': 'percent',
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
                    'unit': 'percent',
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
