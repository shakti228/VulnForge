from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib


@dataclass
class Finding:
    title: str
    severity: str
    description: str
    remediation: str = ""
    confidence: str = "MEDIUM"
    finding_id: str = ""
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

        if not self.finding_id:
            raw = f"{self.title}:{self.description}"
            self.finding_id = hashlib.sha256(
                raw.encode()
            ).hexdigest()[:12].upper()

    def to_dict(self):
        return asdict(self)


class Plugin(ABC):
    name = "Unnamed Plugin"
    version = "0.1.0"

    @abstractmethod
    def run(self) -> list[Finding]:
        raise NotImplementedError
