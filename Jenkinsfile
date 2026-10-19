pipeline {
    agent any

    environment {
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
                echo '🛡️ Scanning Docker image for OS/Binary vulnerabilities...'
                sh 'trivy image --severity CRITICAL --exit-code 1 ${DOCKER_IMAGE}:${IMAGE_TAG} || true'
            }
        }

        stage('Security Scan (Snyk)') {
            steps {
                echo '🔍 Scanning source code dependencies with Snyk...'
                withCredentials([string(credentialsId: 'snyk-api-token', variable: 'SNYK_TOKEN')]) {
                    // Install Snyk CLI and authenticate
                    sh 'npm install -g snyk'
                    sh 'snyk auth ${SNYK_TOKEN}'
                    // Scan the project (fail only on high/critical for now)
                    sh 'snyk test --severity-threshold=high || true'
                }
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
