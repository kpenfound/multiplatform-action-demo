import os
ci = os.getenv('CI_PLATFORM')
location = 'local'
if ci:
  location = ci
print('Hello from multiplatform-action-demo in', location)