class CheckRegistry:
    def __init__(self):
        self._checks = []

    def register(self, name, function):
        if not callable(function):
            raise TypeError("Check must be callable.")
        self._checks.append((name, function))

    def run(self, metadata):
        results = []

        for name, function in self._checks:
            findings = function(metadata)

            if findings:
                results.extend(findings)

        return results

    def names(self):
        return [name for name, _ in self._checks]
