pipeline {
    agent none
    stages {
        stage('Deploy') {
            agent {
                label 'deployagent'
            }
            steps {
                script {
                    sh 'repoUrl = "${GIT_URL}"'
                    sh 'repoName = $repoUrl.tokenize('/').last().replaceAll('.git', '')'
                    sh 'kubectl create namespace perf-${repoName}-${BUILD_ID}'
                }
            }
        }
        stage('Perf test') { // Dump logs & Threads
            agent {
                label 'testagent'
            }
            steps {
                script {
                        
                        sh 'mkdir perf_report/'
                        sh 'locust --headless --users 5 --tag get --html perf_report/report.html --spawn-rate 1 --run-time 5 -H http://localhost:8100'
                }
                
            }
        }
        stage('Destroy') { // If the infra does not get destroyed, the log of the rest of its existance must be dumped also
            agent {
                label 'testagent'
            }
            steps {
                input message: 'Do you want to destroy the infra now ? If you choose no, the infra will be destroyed after 3 days.', ok: 'Yes', submitterParameter: 'APPROVER' //submitterParameter adds a link to a submit page 
                echo 'Destroying...'
            }
        }
    }
    post {
        always {
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'perf_report', reportFiles: 'report.html', reportName: 'Perf Report', reportTitles: 'Perf Report', useWrapperFileDirectly: true])
        }
    }
}