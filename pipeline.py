import os

TEMPLATE_PATH = "templates/github_actions_template.yml"
OUTPUT_DIR = "output"

def get_user_input():
    print("🔧 CI/CD Pipeline Builder for GitHub Actions")
    python_version = input("Enter Python version (e.g., 3.10): ").strip()
    return {"python_version": python_version}

def generate_pipeline(config):
    with open(TEMPLATE_PATH, "r") as template_file:
        template = template_file.read()

    for key, value in config.items():
        template = template.replace(f"${{{key}}}", value)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "ci_pipeline.yml")
    with open(output_path, "w") as output_file:
        output_file.write(template)

    print(f"✅ Pipeline generated at: {output_path}")

if __name__ == "__main__":
    config = get_user_input()
    generate_pipeline(config)


