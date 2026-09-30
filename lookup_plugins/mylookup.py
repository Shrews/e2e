from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        results = ["test lookup"]

        # generate a deprecation warning for _available_variables
        myvars = self._templar._available_variables

        # generate a deprecation warning for _loader
        myloader = self._templar._loader

        # generate a deprecation warning for environment
        myenv = self._templar.environment

        return results
