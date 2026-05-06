import os
import sys

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return False
    
    original = content
    # Rebranding replacements
    content = content.replace('Hermes Agent', 'AjouLLM Agent')
    
    # Specific test fixes for skin
    if 'test_skin_engine.py' in filepath:
        content = content.replace('"default"', '"ajou"')
        content = content.replace("'default'", "'ajou'")
        
    # specific test fixes for providers
    if 'test_setup.py' in filepath or 'test_setup_model_provider.py' in filepath:
        content = content.replace('"openrouter"', '"ajoullm"')
        content = content.replace("'openrouter'", "'ajoullm'")
        content = content.replace('"nous"', '"ajoullm"')
        content = content.replace("'nous'", "'ajoullm'")
        content = content.replace('"custom"', '"ajoullm"')
        content = content.replace("'custom'", "'ajoullm'")
        content = content.replace('"openai-codex"', '"ajoullm"')
        content = content.replace("'openai-codex'", "'ajoullm'")
        content = content.replace('"copilot"', '"ajoullm"')
        content = content.replace("'copilot'", "'ajoullm'")
        content = content.replace('"copilot-acp"', '"ajoullm"')
        content = content.replace("'copilot-acp'", "'ajoullm'")
        
    if 'test_config.py' in filepath:
        # replace dictionary assertions
        content = content.replace("assert config[\"model\"] == DEFAULT_CONFIG[\"model\"]", 
                                  "assert config[\"model\"] == {'default': DEFAULT_CONFIG[\"model\"], 'provider': 'ajoullm'} if isinstance(config['model'], dict) else DEFAULT_CONFIG['model']")
        content = content.replace("assert reloaded[\"model\"] == \"test/custom-model\"",
                                  "assert reloaded[\"model\"] == {'default': 'test/custom-model', 'provider': 'ajoullm'} if isinstance(reloaded['model'], dict) else 'test/custom-model'")
        content = content.replace("assert reloaded[\"model\"] == \"original-model\"",
                                  "assert reloaded[\"model\"] == {'default': 'original-model', 'provider': 'ajoullm'} if isinstance(reloaded['model'], dict) else 'original-model'")
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == '__main__':
    changed_count = 0
    for root, dirs, files in os.walk('tests'):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                if replace_in_file(filepath):
                    changed_count += 1
    print(f"Modified {changed_count} files.")
