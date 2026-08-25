import hashlib

def finding_id(finding):
    raw = "|".join([
        finding.get("title", ""),
        finding.get("severity", ""),
        finding.get("description", ""),
    ])
    return hashlib.sha256(raw.encode()).hexdigest()[:12].upper()

def add_ids(findings):
    result = []
    for finding in findings:
        item = dict(finding)
        item["finding_id"] = finding_id(item)
        result.append(item)
    return result
