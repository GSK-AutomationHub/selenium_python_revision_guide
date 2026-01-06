'''
How do you use PyTest in CI/CD pipelines?
👉 In real teams, you don’t run tests locally only → you hook PyTest into your CI/CD:
Jenkins, GitLab, GitHub Actions, Azure DevOps etc.

✅ This automates:
Test execution on every push/merge
Report generation
Pass/fail feedback to developers

✅ Generic Example
# Jenkins Groovy Pipeline for PyTest with HTML Report
Declarative Pipeline Stages:
    1️⃣ Checkout code
    2️⃣ Set up Python
    3️⃣ Install dependencies
    4️⃣ Run PyTest with HTML report
    5️⃣ Archive the HTML report

# Groovy Declarative Pipeline Example
pipeline {
    agent any

    environment {
        // Use Python virtual env location if needed
        VENV = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo "Setting up Python environment..."
                sh """
                    python -m venv ${VENV}
                    source ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-html
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running PyTest with HTML report..."
                sh """
                    source ${VENV}/bin/activate
                    pytest --html=reports/result.html --self-contained-html
                """
            }
        }

        stage('Archive Report') {
            steps {
                echo "Archiving HTML report..."
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
                junit allowEmptyResults: true, testResults: '**/TEST-*.xml'
                // Note: Use --junitxml=reports/result.xml if you want JUnit too
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
            cleanWs()
        }
    }
}

✅ Key Points:
✅ agent any → Runs on any available Jenkins agent.
✅ Virtual environment → Optional but recommended for isolated Python deps.
✅ pytest --html → Generates the self-contained HTML report.
✅ archiveArtifacts → Stores the HTML report in Jenkins so you can view/download it.
✅ junit → Optionally publish JUnit XML if you run PyTest with --junitxml.

project_root/
 ├── tests/
 ├── requirements.txt
 ├── Jenkinsfile   # (this pipeline)

# Scripted Pipeline — PyTest with HTML Report
node {
    // Define virtual environment directory
    def VENV = ".venv"

    try {
        stage('Checkout') {
            echo "Checking out code..."
            checkout scm
        }

        stage('Setup Python') {
            echo "Creating virtual environment and installing dependencies..."
            sh """
                python -m venv ${VENV}
                source ${VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest pytest-html
            """
        }

        stage('Run Tests') {
            echo "Running PyTest and generating HTML report..."
            sh """
                source ${VENV}/bin/activate
                pytest --html=reports/result.html --self-contained-html
            """
        }

        stage('Archive Reports') {
            echo "Archiving HTML report..."
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            // If you want JUnit style, add:
            // sh "pytest --junitxml=reports/result.xml"
            // junit 'reports/result.xml'
        }

    } catch (err) {
        echo "Pipeline failed: ${err}"
        throw err
    } finally {
        echo "Cleaning up workspace..."
        cleanWs()
    }
}

✅ Key Highlights:
✅ node { ... } — Scripted pipelines always wrap steps in a node block to run on a Jenkins agent.
✅ try/catch/finally — good practice to handle errors and ensure cleanup.
✅ Uses archiveArtifacts to keep HTML report.
✅ You can switch to junit if you output a --junitxml.

# ✅ Scripted vs Declarative — when to use which?
| 🔹                | **Scripted**                        | **Declarative**               |
| ----------------- | ----------------------------------- | ----------------------------- |
| ✅ **Syntax**      | Groovy code-like                    | YAML-like structure           |
| ✅ **Flexibility** | Max control, good for dynamic logic | Simpler for typical pipelines |
| ✅ **Readability** | More verbose                        | Easier for teams              |
| ✅ **Plugins**     | Same                                | Same                          |


CI config file for GitHub Actions:

# .github/workflows/python-tests.yml
name: Python Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-html
      - name: Run tests
        run: pytest --html=reports/result.html --self-contained-html
✅ Real Automation Example — Jenkins
Freestyle or Pipeline Job:

1️⃣ Add build step:

bash
Copy
Edit
pip install -r requirements.txt
pytest tests/ --html=reports/result.html --self-contained-html
2️⃣ Use JUnit XML:

bash
Copy
Edit
pytest tests/ --junitxml=reports/result.xml
3️⃣ Configure Jenkins to publish JUnit results + archive HTML.

✅ What to say in interview
“I integrate PyTest with CI/CD by adding it as a build step. I use HTML and JUnit reports so that tools like Jenkins, GitLab, or GitHub Actions can display results and fail builds on test failures. This ensures continuous test feedback.”


'''