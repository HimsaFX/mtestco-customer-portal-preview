"""Generate public AVA handoff from the live preview receipt and curated context."""
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://himsafx.github.io/mtestco-customer-portal-preview/testing-build.json'

def render(receipt, context):
    sha = receipt.get('applicationSource', '')
    if not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise ValueError('Live receipt has no valid application source SHA')
    run = receipt.get('verificationRun')
    if not isinstance(run, int) or isinstance(run, bool):
        raise ValueError('Live receipt has no verification run')
    fingerprint = hashlib.sha256((json.dumps(receipt, sort_keys=True) + context).encode()).hexdigest()
    return f'''# AVA shared project status

Stable source: https://raw.githubusercontent.com/HimsaFX/mtestco-customer-portal-preview/main/AVA_STATUS.md

## Published preview receipt

- Preview: https://himsafx.github.io/mtestco-customer-portal-preview/
- Published application source: `{sha}`
- Receipt-reported verified build: `{receipt.get('verifiedBuild')}`
- Receipt-reported verification run: `{run}`
- Testing-only flag: `{receipt.get('testingOnly')}`
- Production-deployment flag: `{receipt.get('productionDeployment')}`
- Evidence: {URL}

These values come from the live preview receipt. They do not independently prove every feature, backend change, or test passed. Compare the dated work notes below with this version; newer local work is not automatically published.

{context.strip()}

<!-- status-input-sha256: {fingerprint} -->
'''

if __name__ == '__main__':
    request = Request(URL, headers={'Cache-Control': 'no-cache', 'User-Agent': 'AVA-status-sync'})
    with urlopen(request, timeout=30) as response:
        receipt = json.load(response)
    context = (ROOT / 'AVA_CONTEXT.md').read_text(encoding='utf-8')
    result = render(receipt, context)
    target = ROOT / 'AVA_STATUS.md'
    if not target.exists() or target.read_text(encoding='utf-8') != result:
        target.write_text(result, encoding='utf-8', newline='\n')
        print('Updated AVA_STATUS.md from the live preview receipt.')
    else:
        print('AVA status is current; no write needed.')

