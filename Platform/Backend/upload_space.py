import os
import sys
import shutil
import tempfile
from huggingface_hub import HfApi, create_repo

token = os.getenv("HF_TOKEN", "")
if not token and len(sys.argv) > 1:
    token = sys.argv[1]

if not token:
    print("[ERROR] Token required as argument or environment variable.")
    sys.exit(1)

space_id = "Balajikrishnan031/Keffi-Backend"
api = HfApi()

print("==========================================================")
print(f"[HF SPACE UPLOAD] Deploying to Target Space: {space_id}")
print("==========================================================")

# Step 1: Ensure Space repo exists
try:
    create_repo(repo_id=space_id, token=token, repo_type="space", space_sdk="docker", exist_ok=True)
    print(f"[1/3] Hugging Face Space '{space_id}' is active.")
except Exception as e:
    print(f"[1/3] Space setup note: {e}")

# Step 2: Prepare clean staging directory
backend_dir = os.path.abspath(os.path.dirname(__file__))

temp_stage = tempfile.mkdtemp(prefix="keffi_clean_space_")
print(f"[2/3] Preparing clean production backend package in {temp_stage}...")

# Copy all backend python files and Dockerfile
for root, dirs, files in os.walk(backend_dir):
    rel_path = os.path.relpath(root, backend_dir)
    target_dir = os.path.join(temp_stage, rel_path) if rel_path != "." else temp_stage
    os.makedirs(target_dir, exist_ok=True)
    
    for f in files:
        if f in ["upload_space.py"]:
            continue
        if f.endswith(".py") or f in ["Dockerfile", "requirements.txt", "Modelfile_Keffi"]:
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))

# Generate clean Space README.md
space_readme = """---
title: Keffi Mental Health Support Companion Backend
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
app_port: 7860
---

# Keffi Mental Health Support Companion - Production Backend API

Single consolidated FastAPI backend service providing psychoeducational CBT/DBT/ACT reflective conversation, 4-layered crisis detection safety net, dynamic mood tracking, PHQ-9 & GAD-7 clinical scale assessments, and real ML emotion classification.
"""
with open(os.path.join(temp_stage, "README.md"), "w", encoding="utf-8") as f:
    f.write(space_readme)

# Step 3: Upload clean folder
print(f"[3/3] Uploading production backend to Hugging Face Space for live global multi-user access...")
api.upload_folder(
    folder_path=temp_stage,
    repo_id=space_id,
    repo_type="space",
    token=token,
    delete_patterns="*",
    ignore_patterns=["upload_space.py", "__pycache__", "*.pyc", ".venv", "venv", ".pytest_cache", "*.db", "*.sqlite3", ".env"]
)

# Cleanup temp folder
shutil.rmtree(temp_stage, ignore_errors=True)

print(f"\n[SUCCESS] Production backend live on Hugging Face Space!")
print(f"[LINK] Space Repository URL: https://huggingface.co/spaces/{space_id}")
print(f"[LIVE API] Live Production API URL: https://balajikrishnan031-keffi-backend.hf.space")
