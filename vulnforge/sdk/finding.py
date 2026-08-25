from dataclasses import dataclass

@dataclass
class SecurityFinding:
    title: str
    severity: str
    description: str
    remediation: str = ""
    confidence: str = "MEDIUM"
