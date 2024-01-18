import frontmatter
from pathlib import Path
import json
import toml

BASE_PATH = Path("../../matrix.org")
ECOSYSTEM_PATH = BASE_PATH / "content/ecosystem/"

output_json = {"client": [], "provider": [], "sdk": [], "integration": [], "server": []}

clients_path = (ECOSYSTEM_PATH / "clients").glob("*.md")
id = 0
for file in clients_path:
    filename = file.stem
    if filename == "_index":
        continue
    with open(file) as f:
        client = frontmatter.load(f)
        client_json = client.metadata["extra"]
        client_json["id"] = id
        client_json["name"] = filename
        client_json["description"] = client.content
        output_json["client"].append(client_json)
        id += 1

sdks_path = ECOSYSTEM_PATH / "sdks" / "sdks.toml"
sdks = toml.load(sdks_path)
id = 0
for sdk in sdks["sdks"]:
    sdk_json = sdk
    sdk_json["id"] = id
    output_json["sdk"].append(sdk_json)
    id += 1


integrations_path = ECOSYSTEM_PATH / "integrations" / "integrations.toml"
integrations = toml.load(integrations_path)
id = 0
for integration in integrations["integrations"]:
    integration_json = integration
    integration_json["id"] = id
    output_json["integration"].append(integration_json)
    id += 1

providers_path = ECOSYSTEM_PATH / "hosting" / "providers.toml"
providers = toml.load(providers_path)
id = 0
for provider in providers["providers"]:
    provider_json = provider
    provider_json["id"] = id
    del provider_json["image"]
    output_json["provider"].append(provider_json)
    id += 1

servers_path = ECOSYSTEM_PATH / "servers" / "servers.toml"
servers = toml.load(servers_path)
id = 0
for server in servers["servers"]:
    server_json = server
    server_json["id"] = id
    output_json["server"].append(server_json)
    id += 1

with open("../knowledge_base_data.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)
