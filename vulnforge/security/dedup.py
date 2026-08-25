import hashlib

def deduplicate_findings(findings):
    result = []
    seen = set()

    for finding in findings:
        raw = "|".join([
            str(finding.get("title", "")),
            str(finding.get("severity", "")),
            str(finding.get("description", "")),
        ])
        key = hashlib.sha256(raw.encode()).hexdigest()

        if key not in seen:
            seen.add(key)
            result.append(dict(finding))

    return result
