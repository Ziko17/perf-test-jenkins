pipeline {
    agent {
        label 'perf'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Perf test') { // Dump logs & Threads
            steps {
                echo 'Deploying...'
            }
        }
        stage('Do you want to destroy the infra now ? If you choose no, the infra will be destroyed after 3 days.') { // If the infra does not get destroyed, the log of the rest of its existance must be dumped also
            steps {
                input message: 'Do you want to destroy the infrastructure created ?', ok: 'Yes', submitterParameter: 'APPROVER'
                echo 'Destroying ordered by $APPROVER...'
            }
        }
    }
}