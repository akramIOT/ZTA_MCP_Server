"""
##  ZTA Paradigm based MCP Server Authentication Setup

### 1. OAuth2
- Set environment variable `OAUTH2_SECRET_KEY`.
- Send token in `Authorization: Bearer <token>` header.

### 2. Certificate-based Auth
- Send client certificate via `X-Client-Cert` header (for mock testing).
- For production, integrate with mTLS.

### 3. API Key Auth
- Set env `VALID_API_KEYS` (comma-separated keys).
- Send `X-API-Key: <your_key>` in the header.
"""
