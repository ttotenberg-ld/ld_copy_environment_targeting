# Copy Flag Targeting Settings
This utility copies flag targeting settings from one LaunchDarkly environment to another. It uses the [Copy Flag Settings](https://apidocs.launchdarkly.com/tag/Feature-flags#operation/copyFeatureFlag) REST API call.

All `includedActions` are enabled, meaning your flags will copy everything from the source environment to destination environment, including:
- updateOn
- updatePrerequisites
- updateTargets
- updateRules
- updateFallthrough
- updateOffVariation

Rate limits are handled in utils/apiHandler.py.

## Usage
1. `pip install requests`
1. In `main.py`, replace the `API_KEY`, `PROJECT_KEY`, `SOURCE_ENVIRONMENT`, and `DESTINATION_ENVIRONMENT` with your values
1. Run it! (I'd recommend testing out on lower level environments first. This is an unsupported friday side project.)
