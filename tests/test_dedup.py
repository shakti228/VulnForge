from vulnforge.security.dedup import deduplicate_findings

def test_deduplication():
    finding = {
        "title": "Test",
        "severity": "LOW",
        "description": "Same finding",
    }

    result = deduplicate_findings([finding, finding])
    assert len(result) == 1
