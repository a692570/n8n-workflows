# 🧠 n8n Workflow Collection

This repository contains a collection of **n8n workflows** gathered from multiple sources, including:

* Workflows exported from the [n8n.io](https://n8n.io) website and community forum
* Publicly shared examples found across the web (GitHub, blogs, etc.)

The goal is to provide a useful resource for inspiration, learning, and reuse in your own n8n projects.

---

## 📂 Folder Structure

* Each `.json` file represents a single exported workflow.
* Files are named either based on their original title or source.
* You may also find `.txt` files that were converted into `.json` (see below).

---

## 🔄 TXT to JSON Conversion

Some workflows were originally saved as `.txt` files or copied from online sources. A script was used to:

* Detect `.txt` files
* Attempt to parse them as JSON or structured key-value pairs
* Convert them to valid `.json` format

If you’re looking to run the conversion yourself, check out `convert_txt_to_json.py` included in this repo.

## 🗂 Renaming Workflows

A helper script `rename_workflows.py` is provided to standardize file names.
It reads the `name` field from each workflow JSON and renames the file to a
sanitized version of that value (or falls back to the first node name when the
workflow has no title).

Run the script with:

```bash
python rename_workflows.py
```

After running the script, review and commit the renamed files so the repository
stays consistent.

---

## 🛠 Usage Instructions

To import a workflow into your own n8n instance:

1. Open your [n8n Editor UI](https://docs.n8n.io/hosting/editor-ui/)
2. Click on the **menu** (☰) in the top right → `Import workflow`
3. Choose a `.json` file from this folder
4. Click "Import" to load the workflow

Make sure to review and modify credentials or webhook URLs as needed before running.

---

## 🤝 Contribution

Found a cool workflow or created your own?
Feel free to contribute by adding it to this collection!

Just make sure to:

* Name the file descriptively
* Include a short comment at the top with the original source if applicable

---

## ⚠️ Disclaimer

All workflows here are shared **as-is**.
Always inspect and test them in a safe environment before using them in production.

---

