def deploy_script = 'NO SCR'

pipeline {
    agent {
        label "arm-cpu"
    }

    stages {
        stage('Build Image') {
            agent {
                dockerfile {
                    filename 'dockerfile'
                    reuseNode true
                }
            }
            steps {
                script {
                    deploy_script = load 'script/runner.groovy'
                    sh deploy_script.ssh_scr(params, env)
                }
            }
        }
    }
}
