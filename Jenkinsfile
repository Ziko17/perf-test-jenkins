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
                script {
                     docker.image('locustio/locust').inside("--entrypoint=''") {
                             sh 'locust --headless --users 5 --spawn-rate 1 --run-time 5 -H http://localhost:8100'
                 }
            }
        }
        }
        stage('Destroy') { // If the infra does not get destroyed, the log of the rest of its existance must be dumped also
            steps {
                input message: 'Do you want to destroy the infra now ? If you choose no, the infra will be destroyed after 3 days.', ok: 'Yes', submitterParameter: 'APPROVER' //submitterParameter adds a link to a submit page 
                echo 'Destroying...'
            }
        }
}
}