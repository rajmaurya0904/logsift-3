import yaml

d = yaml.safe_load(open(".github/workflows/ci.yml"))
steps = d["jobs"]["test"]["steps"]
for s in steps:
    print(s.get("name", s.get("uses")))
assert d["jobs"]["test"]["runs-on"] == "ubuntu-latest"
print("OK")