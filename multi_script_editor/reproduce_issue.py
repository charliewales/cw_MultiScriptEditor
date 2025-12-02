import sys
import os

# Add project root to sys.path
project_root = r'c:/Apps/Python/multi_script_editor'
sys.path.insert(0, project_root)

try:
    import jedi
    print(f"Jedi version: {jedi.__version__}")

    # Test f-string (Python 3.6+)
    source = '''
name = "World"
msg = f"Hello {name}"
msg.up'''

    print("Attempting completion with f-string...")
    # Line 4, column len('msg.up')
    # New API
    script = jedi.Script(code=source)
    completions = script.complete(line=4, column=len('msg.up'))

    print(f"Found {len(completions)} completions")
    for c in completions:
        print(f"- {c.name}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
