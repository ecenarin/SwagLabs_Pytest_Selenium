# ✅ Selenium Python Automation Framework – Technical Rationale

This document explains **what** this project includes, **why** each part was added, and **how** it contributes to building a robust, scalable and secure test automation framework.

---

## 🚀 Purpose of the Framework
To build a **simple yet production-grade Selenium UI automation framework** using Python, that:

- Runs reliably in CI (GitHub Actions)
- Supports secure secrets handling
- Is easy to extend and maintain
- Enables test data abstraction and reuse
- Works across environments (e.g., dev, staging)

---

## 📁 Project Structure and Justification

### `tests/`
Holds the actual test cases. Using `pytest` naming conventions allows automatic test discovery. Each test:
- Uses fixture-based browser injection (`make_driver`)
- Reads test data from YAML files for flexibility

### `src/pageobjects/`
Implements the **Page Object Model (POM)** to promote reusability and readability. Each page:
- Has locators and page-specific methods
- Encapsulates actions like login, logout, form fill, etc.

### `config/`
Centralized configuration via YAML files:
- `data.yaml`: stores test data (user credentials, expected messages)
- `caps.yaml`: browser capabilities (headless, resolution, etc.)
- `key.properties`: local encryption key for secrets (excluded via `.gitignore`)

### `utils/`
Helper modules:
- `helpers.py`: shared logic like YAML loading
- `crypto.py`: secrets encryption/decryption
- `logger.py`: logs decorated functions and page actions

---

## ⚙️ Test Runner – `pytest`
Chosen for:
- Clean syntax and flexibility
- Rich fixture support
- Plugin ecosystem (e.g. for reporting, reruns)

Test command example:
```bash
poetry run pytest --junit-xml=reports/test-results.xml -v
```

---

## 🔁 Environment & Secrets Handling
### Why?
To keep test code **environment-agnostic** and avoid hardcoded credentials.

### How?
- Environments are defined via `.env` file or `properties.py`
- Secrets are encrypted using `secure-test-automation` Python package
- Secret decryption key is stored **only locally** in `key.properties`
- Remote execution uses Vault for secrets (Jenkins, GitHub, etc.)

Example:
```python
@pytest.fixture
def get_password():
    secure = Secure()
    read = YAMLReader.read("data.yaml", to_simple_namespace=True)
    return secure.decrypt_password(read.users.john.details.password)
```

---

## 🌐 CI Integration – GitHub Actions
CI workflows ensure the framework runs reliably in automation pipelines.

- `run_tests_ubuntu.yaml`: daily test runs + manual trigger
- `lint.yaml`: code quality enforcement via `ruff`
- `upload-artifact`: saves test results and screenshots on failure

Benefits:
- Continuous feedback
- Prevents regressions
- Enables headless browser execution

---

## 🧹 Linting – Ruff
Linting rules enforce clean, PEP8-compliant, maintainable code.  
Run with:
```bash
ruff check .
```
Configured via `.ruff.toml` for full control over rules, ignores, and exclusions.

---

## 🧪 Demo Target
Tests can be run against:
- Live application (if configured via `DEV_URL` / `STAG_URL`)
- Public demo site: [https://demoqa.com/text-box](https://demoqa.com/text-box)

---

## 📦 Why Poetry?
- Dependency management & virtualenv isolation
- Lockfile ensures reproducibility across machines/CI
- Easy publishing if this framework is converted to a package

---

## 🧠 Summary
This framework balances:
- 🧼 Clean architecture (POM, config separation)
- 🔒 Security (encrypted secrets)
- 🤖 CI automation (GitHub Actions)
- 💡 Flexibility (YAML test data, multiple environments)

It’s not just for demo – it’s designed to scale and run safely in real pipelines.

---

> Built with care for quality, clarity, and CI-readiness.
