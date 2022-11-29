import os
gh = os.getenv('GITHUB_ACTIONS')
cci = os.getenv('CIRCLECI')
location = 'local'
if gh:
  location = 'github actions'
if cci:
  location = 'cirlceci'
print('Hello from multiplatform-action-demo in', location)