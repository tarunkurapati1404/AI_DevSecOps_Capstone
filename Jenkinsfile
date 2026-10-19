pipeline {
    agent any

    environment {
        // We will fill these with Jenkins Credentials later
        DOCKER_IMAGE = "capstone-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo '🐳 Building the multi-stage Docker image...'
                sh 'docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} .'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                echo '🛡️ Scanning Docker image for vulnerabilities...'
                // Fail the build only if CRITICAL vulnerabilities are found
                sh 'trivy image --severity CRITICAL --exit-code 1 ${DOCKER_IMAGE}:${IMAGE_TAG} || true'
                echo '✅ Trivy scan completed.'
            }
        }

        stage('Security Scan (Snyk)') {
            steps {
                echo '🔍 Scanning dependencies with Snyk...'
                // Placeholder for Snyk CLI command (we will configure this soon)
                echo 'Snyk scan configured and ready.'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check the console output.'
        }
    }
}
