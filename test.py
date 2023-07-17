from scrubhelper import scrub
from pprint import pprint

data = {
  'raw': {
      'test': [
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
          {
              'label': 'value'
          },
      ]
  }
}

d = scrub('raw.test[].label', data, lambda: 'test')

pprint(d)